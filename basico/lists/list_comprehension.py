def first_list():
	return [x + 1 for x in range(15)]


def second_list():
	return [x + 1 if x % 2 == 0 else -1 for x in range(15)]


# def third_list(iterable: Iterable[_T]):


if __name__ == '__main__':
	fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

	print(first_list())
	print(second_list())
	# print(third_list())
