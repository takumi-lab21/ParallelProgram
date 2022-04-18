# loopの中でコルーチン関数を実行する

import asyncio

async def hello_world():
    print("Hello World!")


loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
