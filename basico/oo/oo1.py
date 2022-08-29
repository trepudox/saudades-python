class Pessoa:
	def __init__(self, nome: str, idade: int):
		self.__nome = nome
		self.__idade = idade

	@property
	def nome(self):
		return self.__nome

	@nome.setter
	def nome(self, new_nome: str):
		self.__nome = new_nome

	@property
	def idade(self):
		return self.__idade

	@idade.setter
	def idade(self, new_idade: int):
		self.__idade = new_idade

	def __str__(self):
		return f"{self.nome}:{self.idade}"


class Funcionario(Pessoa):
	def __init__(self, nome: str, idade: int, salario_hora: int):
		super().__init__(nome, idade)
		self.__salario_hora = salario_hora

	@property
	def salario(self):
		return self.__salario_hora

	@salario.setter
	def salario(self, new_salario_hora: int):
		self.__salario_hora = new_salario_hora

	def calcular_salario(self, horas_trabalhadas: int):
		return self.__salario_hora * horas_trabalhadas

	def __str__(self):
		return f"{super().__str__()} - Salario/Hora R$ {self.__salario_hora}"


if __name__ == '__main__':
	marco = Pessoa("Marco", 20)
	print(f"Nome: {marco.nome}")
	print(f"Idade: {marco.idade}")
	print(f"Marco: {marco}")

	print("-----------------------------")

	marco2 = Funcionario("Marco", 20, 15)
	print(f"Nome: {marco2.nome}")
	print(f"Idade: {marco2.idade}")
	print(f"Marco Funcionario: {marco2}")
