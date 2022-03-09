import asyncio
from time import sleep, time


def blocker(txt):
    sleep(3)
    return 'aaa' + txt


def async_sample(loop):
    start = time()
    results = loop.run_until_complete(asyncio.gather(
        loop.run_in_executor(None, blocker, '1'),
        loop.run_in_executor(None, blocker, '2'),
        loop.run_in_executor(None, blocker, '3'),
    ))
    time_took = time() - start

    print('time took', time_took)
    print(results)


async def async_sample2(loop):
    start = time()
    f1 = loop.run_in_executor(None, blocker, '1')
    f2 = loop.run_in_executor(None, blocker, '2')
    f3 = loop.run_in_executor(None, blocker, '3')

    print([
        await f1,
        await f2,
        await f3,
    ])
    time_took = time() - start
    print('time took', time_took)


def sync_sample():
    sync_start = time()
    sync_results = [
        blocker('1'),
        blocker('2'),
        blocker('3'),
    ]
    sync_time_took = time() - sync_start
    print(sync_time_took)
    print(sync_results)


from functools import partial


def promisify(loop, executor=None):

    def _promisified(func):

        def __inner(*a, **kw):
            return loop.run_in_executor(executor, partial(func, *a, *kw))

        return __inner

    return _promisified


loop = asyncio.get_event_loop()


@promisify(loop)
def promisified_blocker(txt):
    sleep(3)
    return 'aaa' + txt


async def promisify_sample():
    start = time()
    f1 = promisified_blocker('1')
    f2 = promisified_blocker('2')
    f3 = promisified_blocker('3')
    print([
        await f1,
        await f2,
        await f3,
    ])
    # print(await asyncio.gather(
    #     promisified_blocker('1'),
    #     promisified_blocker('2'),
    #     promisified_blocker('3'),
    # ))
    time_took = time() - start
    print('time took', time_took)


if __name__ == '__main__':
    # async_sample(loop)
    # print('-' * 10)
    # loop.run_until_complete(async_sample2(loop))
    # print('-' * 10)
    # sync_sample()
    #

    loop.run_until_complete(promisify_sample())

    loop.close()
