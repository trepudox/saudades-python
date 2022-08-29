class Pessoa:
	def __init__(self, nome: str, idade: int):
		self.__nome = nome
		self.__idade = idade

	@property
	def nome(self):
		return self.__nome

	@nome.setter
	def nome(self, new_nome):
		self.__nome = new_nome

	@property
	def idade(self):
		return self.__idade

	@idade.setter
	def idade(self, new_idade):
		self.__idade = new_idade

	def __str__(self):
		return f"{self.nome}:{self.idade}"


if __name__ == '__main__':
	marco = Pessoa("Marco", 20)
	print(f"Nome: {marco.nome}")
	print(f"Idade: {marco.idade}")
	print(f"Marco: {marco}")
