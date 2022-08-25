from functools import reduce


def square(x: int):
	return x ** 2


def even(x: int):
	return x % 2 == 0


def subtract(x: int, y: int):
	return x - y


if __name__ == '__main__':
	numbers = [x for x in range(21)]
	print(f"Numbers: {numbers}")

	squares = list(map(lambda x: square(x), numbers))
	print(f"Square of numbers: {squares}")

	evens = list(filter(lambda x: even(x), numbers))
	print(f"Even numbers: {evens}")

	sum_result = sum(numbers)
	print(f"Sum result: {sum_result}")

	subtraction_result = reduce(lambda x, y: subtract(x, y), numbers)
	print(f"Subtraction result: {subtraction_result}")
