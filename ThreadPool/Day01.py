"""
ThreadPoolExecutorによる並列処理の実装
- add_done_callbackにより、各futureの終了時に起動する関数を登録できる
- functools.partialを利用することで任意の引数を指定できる
- wait関数は、引数に渡したfutureが終了するまで待機する。複数のfeatureを渡した場合は、
  全てが終了するまで待機する。
"""

from concurrent.futures import ThreadPoolExecutor, wait, Future
import functools
import time


def process(ind:int):
    print(ind)
    time.sleep(1)
    return f"I'm {ind}th process"
    
def callback(results:dict, index: int, future: Future):
    results[index] = future.result()

def main():
    _max_workers = 5
    _futures = {}
    _results = {}
    with ThreadPoolExecutor(max_workers=_max_workers) as executor:
        for ind in range(0,5):
            _futures[ind] = executor.submit(
                functools.partial(
                    process,
                    ind=ind
                ),
            )
            _futures[ind].add_done_callback(functools.partial(callback, _results, ind))
    wait(_futures.values())
    print("End Process")

if __name__ == "__main__":
    main()
