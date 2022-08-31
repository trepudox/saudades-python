if __name__ == "__main__":
	numbers: set[int] = {0, 1, 2, 3, 4, 5, 6, 7}

	numbers2: set[int] = numbers.copy()
	numbers2.discard(1)

	print("numbers: ", numbers)
	print("numbers2: ", numbers2)
	print("difference: ", numbers.difference(numbers2))

	numbers.difference_update(numbers2)
	print("difference_update: ", numbers)
