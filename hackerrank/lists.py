# https://www.hackerrank.com/challenges/python-lists
if __name__ == '__main__':
	inputs: list[str] = [
		"insert 0 5",
		"insert 1 10",
		"insert 0 6",
		"print",
		"remove 6",
		"append 9",
		"append 1",
		"sort",
		"print",
		"pop",
		"reverse",
		"print",
	]

	lst = []
	commands: list[list[str]] = []
	for inpt in inputs:
		splitted_command = inpt.split(' ')
		commands.append(splitted_command)

	for c in commands:
		if c[0] == "print":
			print(lst)
			continue

		c_length: int = c.__len__()
		func_call: str = f"lst.{c[0]}({c[1] if c_length > 1 else ''}{',' + c[2] if c_length == 3 else ''})"
		eval(func_call)
