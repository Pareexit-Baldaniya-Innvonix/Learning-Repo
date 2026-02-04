# Task 5:
import time
import functools


def timer(func: callable) -> callable:

    @functools.wraps(func)
    def wrapper(*args: any, **kwargs: any) -> any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Time taken: {end_time - start_time:.4f} seconds.")
        return result

    return wrapper


@timer
def waste_time() -> None:
    time.sleep(1)
    print("Function finished!")


waste_time()
