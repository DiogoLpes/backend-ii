import multiprocessing
import time
from typing import List

def binary_search(elements: List[int], target: int) -> bool:
    ordered_list = sorted(elements)
    left, right = 0, len(ordered_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if ordered_list[mid] == target:
            return True
        if target < ordered_list[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False


def run_sequential(data: List[int], target: int, iterations: int) -> float:
    start = time.time()
    for _ in range(iterations):
        binary_search(data, target)
    return time.time() - start


def run_multiprocessing(data: List[int], target: int, iterations: int) -> float:
    params = [(data, target)] * iterations
    start = time.time()
    with multiprocessing.Pool() as pool:
        pool.starmap(binary_search, params)
    return time.time() - start


if __name__ == "__main__":
    data = list(range(100))
    target = 100
    iterations = 1000

    print("--- Starting Sequential ---")
    sequential_time = run_sequential(data, target, iterations)
    print(f"Sequential Time: {sequential_time:.4f} seconds\n")

    print("--- Starting Multiprocessing ---")
    multiprocessing_time = run_multiprocessing(data, target, iterations)
    print(f"Multiprocessing Time: {multiprocessing_time:.4f} seconds")
