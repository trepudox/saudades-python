def first_list() -> list[int]:
	return [x for x in range(15)]


def second_list() -> list[int]:
	return [x if x % 2 == 0 else 0 for x in range(15)]


def third_list() -> list[int]:
	return [x + 1 if x % 2 == 0 else -1 for x in range(15)]


def fourth_list(iterable: list) -> list[str]:
	return [s for s in iterable if "a" in s]


def fifth_list(iterable: list) -> list[str]:
	return [s for s in iterable if "a" not in s]


def matrix() -> list[list[int]]:
	return [[x + 1 for x in range(5)] for _ in range(5)]


if __name__ == '__main__':
	fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

	print(first_list())
	print(second_list())
	print(third_list())
	print(fourth_list(fruits))
	print(fifth_list(fruits))
	print(matrix())
