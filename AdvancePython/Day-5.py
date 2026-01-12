# Day 5: Multithreading and Multiprocessing

# Task 1:
# 1. Process:
# -> it is a instance of the program
# -> they do not share the memory
# -> they are independent from each other

# 2. Thread:
# -> it's an entity in the process that can be schedule for execution
# -> a process can spawn multiple threds
# -> all threads within the process can share a same memory

# Task 2:
import threading
import time

def square(num):
    print(f"Square: {num*num}")
    time.sleep(1)

def cube(num):
    print(f"Cube: {num*num*num}")
    time.sleep(1)

t1 = threading.Thread(target = square, args = (4, ))
t2 = threading.Thread(target = cube, args = (4, ))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done!")

# Task 3:
import multiprocessing
import os

def check_task():
    print(f"task running in process id: {os.getpid()}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = check_task)
    p2 = multiprocessing.Process(target = check_task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

# Task 4:
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import os

os.makedirs("downloaded_images", exist_ok = True)

def download_image(url):
    try:
        filename = os.path.join("downloaded_images", url.split("/")[-1])
        print(f"Starting download: {url} (Thread: {threading.current_thread().name})")

        response = requests.get(url, timeout = 10)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Successfully saved to {filename}")
        else:
            print(f"Failed to download {url}: Status {response.status_code}")

    except Exception as e:
        print(f"Error downloading {url}: {e}")

image_urls = [
    "https://via.placeholder.com/600/92c952",
    "https://via.placeholder.com/600/771796",
    "https://via.placeholder.com/600/24f355",
    "https://via.placeholder.com/600/d32776",
    "https://via.placeholder.com/600/f66b97"
]

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers = 5) as executor:
        executor.map(download_image, image_urls)

    print("\nAll downloads completed!")

# Task 5:
import multiprocessing
import time

def compute_square(num):
    return num * num

if __name__ == "__main__":
    dataset = list(range(10000000))

    start_time = time.perf_counter()
    end_time = time.perf_counter()
    print(f"Sequential processing would take much longer...")

    print(f"Starting parallel computing on {multiprocessing.cpu_count()} cores...")
    start_time = time.perf_counter()

    with multiprocessing.Pool() as pool:
        results = pool.map(compute_square, dataset)

    end_time = time.perf_counter()

    print(f"Parallel processing finished in {end_time - start_time:.4f} seconds.")
    print(f"Computed {len(results)} results.")