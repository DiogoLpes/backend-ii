import multiprocessing
import time

def binary_search(elements:list, target:int) -> bool:
    ordered_list = sorted(elements)
    while ordered_list:
        index = int(len(ordered_list)) // 2
        number = ordered_list[index]
        if target == ordered_list[index]:
            print(f"Found element {target} in index {index}")
            return True
        if target < ordered_list[index]:
            ordered_list = ordered_list[:index]
        else:
            ordered_list = ordered_list[index+1:]
    print(f"Element {target} not found in list.")
    return False

if __name__ == "__main__":
    # 1. TESTE SEQUENCIAL 
    print("--- Starting Sequential ---")
    start = time.time()
    for i in range(1000): 
        binary_search(list(range(100)), 100)
    print(f"Sequential Time: {time.time() - start:.4f} seconds\n")
        
    # 2. TESTE MULTIPROCESSING (A forma correta de comparar)
    print("--- Starting Multiprocessing ---")
    start_mp = time.time()
    
    # Em vez de um processo manual, usamos o Pool para gerir os núcleos
    with multiprocessing.Pool() as pool:
        # O pool.map divide a range() entre todos os teus núcleos
        pool.map(binary_search(list(range(100)), 100), range(1000))
        
    print(f"Multiprocessing Time: {time.time() - start_mp:.4f} seconds")