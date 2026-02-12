# Task-6: Create a program that runs async function (in thread) and normal function then waits for thread to finish
import asyncio
import threading
import time
from typing import Callable, Coroutine, Any


# running async functon in thread
def async_in_thread(async_func: Callable[[], Coroutine[Any, Any, None]]) -> None:
    asyncio.run(async_func())


# async function
async def async_task() -> None:
    print("async_task started...")
    await asyncio.sleep(2)
    print("async_task done!")


# normal function
def normal_task() -> None:
    print("normal_task started...")
    time.sleep(1)
    print("normal_task done!")


async def main() -> None:
    # thread
    thread: threading.Thread = threading.Thread(
        target=async_in_thread, args=(async_task,)
    )
    thread.start()

    await asyncio.sleep(0.1)
    normal_task()

    thread.join()
    print("All tasks done!")


if __name__ == "__main__":
    asyncio.run(main())
