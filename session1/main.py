import logging

logging.basicConfig(level=logging.INFO, format ='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# if __name__ == "__main__":
#     lst_el = [10, 100, 1000, 10000]
#     for n in lst_el:
#         result = factorial(n)
#         print(result)
        

def linear_search(elements:list, target:int) -> bool:
    for element in elements:
        if target == element:
            return True
    return False

def binary_search(elements:set, target:int) -> bool:
    ordered_elements = sorted(elements)
    while ordered_list:
        index = int(len(ordered_list)/2)
        number = ordered_list[index]
        if number == target:
            return True
        if target > number
            ordered_list = ordered_list[index+1:]
            continue
        ordered_list = ordered_list[:index]
    return False
    


if __name__ == "__main__":
    lst_el = [0, 10, 100, 1000, 10000]
    for el in lst_el:
        elements = list(range(el))
        target = el - 1
        result = linear_search(elements, target)
       
       
       
        print(f"Element {target} found in {elements}: {result}")