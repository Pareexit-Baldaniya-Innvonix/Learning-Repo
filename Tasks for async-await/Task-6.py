# Task-6: Create a program that runs async function (in thread) and normal function then waits for thread to finish
import asyncio
import threading
import time
from typing import Callable, Coroutine, Any


# running async functon in thread
def async_in_thread(async_func: Callable[[], Coroutine[Any, Any, None]]) -> None:
    asyncio.run(async_func())  # creates new event loop for thread


# async function
async def async_task() -> None:
    print("async_task started...")
    await asyncio.sleep(2)
    print("async_task (async thread) done!")


# normal function
def normal_task() -> None:
    print("normal_task started...")
    time.sleep(1)
    print("normal_task (main) done!")


def main() -> None:
    # thread to run the async function
    thread = threading.Thread(target=async_in_thread, args=(async_task,))
    thread.start()

    time.sleep(0.1)
    normal_task()

    thread.join()
    print("All tasks completed!")


if __name__ == "__main__":
    main()
