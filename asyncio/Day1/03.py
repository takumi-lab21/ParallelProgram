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

async def main_process():
    await child_process_1(1)
    await child_process_2(1)

loop = asyncio.get_event_loop()
loop.create_task(child_process_1(1))
loop.run_until_complete(child_process_2(1))
