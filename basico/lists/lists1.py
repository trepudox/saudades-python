if __name__ == '__main__':
	fruits: list[str] = ["apple", "banana", "orange", "cherry", "pineapple", "kiwi", "mango"]

	fruits.sort(key=lambda x: len(x))  # sort com lambda as key
	print(fruits)

	fruits.sort(reverse=True, key=lambda x: len(x))  # sort reverso com lambda as key
	print(fruits)

	fruits2: list[str] = fruits.copy()
	fruits2.append("ANOTHER FRUIT")
	print("fruits:", fruits)
	print("fruits2 after copy() and append('ANOTHER FRUIT'):", fruits2)

	print('fruits.index("apple"):', fruits.index("apple"))  # depois de ordenada

	fruits2.extend(fruits2)  # basicamente um append() de outra lista
	print("fruits2.extend(fruits2) == ", fruits2)

	fruits.clear()
	print("fruits.clear() ==", fruits)
