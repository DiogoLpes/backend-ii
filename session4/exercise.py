import multiprocessing

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def compute_factorial(num):
    result = factorial(num)
    print(f"Factorial of {num} is {result}")

if __name__ == "__main__":
    numbers = [5, 6, 7, 8]
    processes = []

    for num in numbers:
        p = multiprocessing.Process(target=compute_factorial, args=(num,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()