def sep(message: str) -> None:
	print("\n", "-" * 15, message, "-" * 15)


if __name__ == '__main__':
	dictionary: dict[int, str] = {1: "a", 2: "b", 3: "c", 4: "d"}
	print(dictionary.setdefault(1, "default"))  # caso a chave exista, ela retornará
	print(dictionary.setdefault(10, "default"))  # caso não exista, setará o valor mencionado
	print(dictionary)

	dictionary[5] = "valor"  # está settando o "valor" na chave 5
	print(dictionary)

	sep("KEYS")
	for key in dictionary.keys():
		print(f"{key}")

	sep("VALUES")
	for value in dictionary.values():
		print(f"{value}")

	sep("ITEMS")
	for key, value in dictionary.items():
		print(f"{key}: {value}")

	print(dictionary.popitem())  # retorna uma tupla com o último par de chave e valor
