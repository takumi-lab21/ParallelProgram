# loopの中でコルーチン関数を実行する
import time
import asyncio

async def child_process_1(seconds):
    print("Hello! I'm child_process_1")
    await asyncio.sleep(seconds)
    print("End! I'm child_process_1")
    

async def child_process_2(seconds):
    print("Hello! I'm child_process_2")
    await asyncio.sleep(seconds)
    print("End! I'm child_process_2")

async def main_process(mode):
    if mode == "task":
        task_1 = asyncio.create_task(child_process_1(1))
        task_2 = asyncio.create_task(child_process_2(1))
    elif mode == "coroutine":
        task_1 = child_process_1(1)
        task_2 = child_process_2(1)

    await task_1
    await task_2
    

asyncio.run(main_process("task"))
