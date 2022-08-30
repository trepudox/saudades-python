class Celular:
	ano = 2022  # atributo estático

	def __init__(self):
		pass


if __name__ == "__main__":
	obj = Celular()  # a classe só possui um atributo estático, chamado ano
	obj.ano = 2010  # aqui, sobrescrevo o atributo estática, agora o objeto possui um atributo de instância chamado ano
	print(f"Celular.ano: {Celular.ano}")
	print(f"obj.ano: {obj.ano}")

	try:
		print(obj.nome)
	except AttributeError:
		print("Deu erro! Celular não tem o atributo 'nome'!")
	# print(obj.nome) lança um erro, pois esse atributo não existe

	obj.nome = "motorola"  # mas após settar o atributo
	print(obj.nome)  # o mesmo print funciona
