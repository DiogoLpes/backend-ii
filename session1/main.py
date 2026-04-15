import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def linear_search(elements:list,target:int) -> bool:
	for element in elements:
		if target == element:
			return True
	logging.warning(f"Element {target} not found in list.")
	return False

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
	logging.warning(f"Element {target} not found in list.")
	return False


def factorial(n:int) -> int:
	if n == 0:
		return 1
	return n * factorial(n-1)
	
if __name__ == "__main__":
	lst_element = [0,1,10,100,1_1000,10_000,100_000,1_000_000]
	
	# for el in lst_element:
	# 	start = time.perf_counter()
	# 	logging.info(f"Searching for element {el-1} in list of size {el}.")
	# 	elements = list(range(el))
	# 	target = el-1
	# 	result = linear_search(elements, target)
	# 	end = time.perf_counter()
	# 	logging.info(f"Element {target} found in list: {result}")
	# 	logging.info(f"Time taken: {end - start} seconds")
	
	for el in lst_element:
		start = time.perf_counter()
		logging.info(f"Searching for element {el-1} in list of size {el}.")
		elements = list(range(el))
		target = el-1
		result = binary_search(elements, target)
		end = time.perf_counter()
		logging.info(f"Element {target} found in list: {result}")
		logging.info(f"Time taken: {end - start} seconds")