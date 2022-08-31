class Pessoa:
	def __init__(self, nome: str, idade: int) -> None:
		self.__nome: str = nome
		self.__idade: int = idade

	@property
	def nome(self) -> str:
		return self.__nome

	@nome.setter
	def nome(self, new_nome: str) -> None:
		self.__nome = new_nome

	@property
	def idade(self) -> int:
		return self.__idade

	@idade.setter
	def idade(self, new_idade: int) -> None:
		self.__idade = new_idade

	def __str__(self) -> str:
		return f"{self.nome}:{self.idade}"

	def __len__(self) -> int:
		return self.__idade


class Funcionario(Pessoa):
	def __init__(self, nome: str, idade: int, salario_hora: int) -> None:
		super().__init__(nome, idade)
		self.__salario_hora: int = salario_hora

	@property
	def salario(self) -> int:
		return self.__salario_hora

	@salario.setter
	def salario(self, new_salario_hora: int) -> None:
		self.__salario_hora = new_salario_hora

	def calcular_salario(self, horas_trabalhadas: int) -> int:
		return self.__salario_hora * horas_trabalhadas

	def __str__(self) -> str:
		return f"{super().__str__()} - Salario/Hora R$ {self.__salario_hora}"


if __name__ == '__main__':
	print("-----------------------------")

	marco: Pessoa = Pessoa("Marco", 20)
	print(f"Nome: {marco.nome}")
	print(f"Idade: {marco.idade}")
	print(f"Marco: {marco}")
	print(f"Marco type: {type(marco)}")

	print("-----------------------------")

	marco2: Funcionario = Funcionario("Marco", 200, 15)
	print(f"Nome: {marco2.nome}")
	print(f"Idade: {marco2.idade}")
	print(f"Salario em 8 horas: {marco2.calcular_salario(8)}")
	print(f"Marco2: {marco2}")

	print(f"Marco2 type: {type(marco2)}")
	print(f"Marco2 is Pessoa? {isinstance(marco2, Funcionario)}")
	print(f"Marco2 is Funcionario? {isinstance(marco2, Funcionario)}")

	print("-----------------------------")

	print("len(marco):", len(marco))  # para obter a len de algum objeto, implementar a função __len__()
	print("len(marco2):", len(marco2))
