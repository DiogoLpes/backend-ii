import multiprocessing
import time
import sys

# Aumentar o limite para suportar números gigantes
sys.set_int_max_str_digits(0)

def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

if __name__ == "__main__":
    # 1. TESTE SEQUENCIAL 
    print("--- Starting Sequential ---")
    start = time.time()
    for i in range(500, 1500): # Números maiores para o CPU "sofrer" um pouco
        factorial(i)
    print(f"Sequential Time: {time.time() - start:.4f} seconds\n")
        
    # 2. TESTE MULTIPROCESSING (A forma correta de comparar)
    print("--- Starting Multiprocessing ---")
    start_mp = time.time()
    
    # Em vez de um processo manual, usamos o Pool para gerir os núcleos
    with multiprocessing.Pool() as pool:
        # O pool.map divide a range(500, 1500) entre todos os teus núcleos
        pool.map(factorial, range(500, 1500))
        
    print(f"Multiprocessing Time: {time.time() - start_mp:.4f} seconds")