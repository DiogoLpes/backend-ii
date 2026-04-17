import multiprocessing
import time


def compute_square(n):
    # Esta função simula uma operação pesada.
    # Ela dorme 1 segundo e depois imprime o quadrado do número.
    time.sleep(1)
    print(f"Square of {n} is {n * n}")


if __name__ == "__main__":
    # Lista de números que queremos processar em paralelo.
    numbers = [2, 3, 4, 5]
    processes = []

    # Para cada número, criamos um processo independente.
    for number in numbers:
        p = multiprocessing.Process(target=compute_square, args=(number,))
        processes.append(p)
        p.start()

    # join() faz o programa principal esperar todos os processos terminarem.
    for p in processes:
        p.join()

    print("All processes finished.")