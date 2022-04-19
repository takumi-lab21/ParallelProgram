import time
from concurrent.futures import ProcessPoolExecutor as PPE
from concurrent.futures import ThreadPoolExecutor as TPE
import random
import asyncio

def aiomeasure(func):
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        response = await func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(elapsed_time)
        return response
    return wrapper

def measure(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        response = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(elapsed_time)
        return response
    return wrapper

def calc(x):
    r = 0
    for i in range(10**7):
        if random.random() < 0.99:
            r += i % x
    return r

async def aiocalc(x):
    r = 0
    for i in range(10**7):
        if random.random() < 0.99:
            r += i % x
    return r

@measure
def main_normal():
    print("normal")
    r = [calc(i) for i in range(1, 16)]
    print(r)

@aiomeasure
async def main_aio():
    print("main_aio")
    r = await asyncio.gather(*[aiocalc(i) for i in range(1, 16)])
    print(r)

@measure
def main_ppe():
    print("ppe")
    with PPE(max_workers=16) as exe:
        r = [r for r in exe.map(calc, list(range(1, 16)))]
    print(r)

@measure
def main_tpe():
    with TPE(max_workers=16) as exe:
        r = [r for r in exe.map(calc, list(range(1, 16)))]
    print(r)


if __name__ == "__main__":
    main_normal() # 24.747608371000002
    asyncio.run(main_aio()) # 26.40497156
    main_ppe() # 11.178272829
    main_tpe() # 23.395420027

