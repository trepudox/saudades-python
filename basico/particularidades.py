def separator() -> None:
	print("\n", "-" * 30, "\n")


def unpacking_variables() -> None:
	separator()
	# é possível "desempacotar" um iterável ao inicializar variáveis
	# na mesma quantidade de itens do iterável
	# OBS.: é possível usar essa feature nos loops for
	tupla: tuple[int, int] = (10, 99)
	a, b = tupla
	print("a: ", a, "b: ", b)

	try:
		x, y, z = tupla
		print("Esse print não será executado, pois será lançado um erro na execução acima")
	except ValueError:
		pass


def for_loop_with_enumerate() -> None:
	separator()
	# quando é preciso de um index ao usar o for loop
	# em um iterável podemos usar o enumerate(), junto
	# do recurso de unpacking:
	for index, element in enumerate(range(0, 200, 10)):
		print(f"{index}: {element}")


if __name__ == '__main__':
	unpacking_variables()
	for_loop_with_enumerate()
