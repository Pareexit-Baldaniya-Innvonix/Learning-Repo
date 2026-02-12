# Task-7: Write a program that uses multiple event loop to run different async functions
import asyncio
import threading


async def task(name: str) -> None:
    print(f"{name} started...")
    await asyncio.sleep(2)
    print(f"{name} completed!")


def run_in_loop(async_func, name: str) -> None:
    loop = asyncio.new_event_loop()  # create new event loop
    asyncio.set_event_loop(loop)  # current thread's loop
    loop.run_until_complete(async_func(name))  # run async function
    loop.close()


def main() -> None:
    # different threads using seperate event loops
    thread1 = threading.Thread(target=run_in_loop, args=(task, "Loop-1"))
    thread2 = threading.Thread(target=run_in_loop, args=(task, "Loop-2"))

    thread1.start()  # start thread1
    thread2.start()  # start thread2

    thread1.join()  # wait for first thread to finish
    thread2.join()  # wait for second thread to finish

    print("All event loops completed!")


if __name__ == "__main__":
    main()
