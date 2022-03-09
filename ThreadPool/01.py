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
    _max_workers = 3
    _futures = {}
    _results = {}
    with ThreadPoolExecutor(max_workers=_max_workers) as executor:
        for ind in range(0,10):
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
