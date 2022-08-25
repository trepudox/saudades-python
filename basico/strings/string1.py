def iterating_over_string(string: str = "string"):
    for char in string:
        print(char, end=" ")


def multiple_lines_string():
    print()
    print("""Primeira linha
Segunda linha
Terceira linha""")


if __name__ == '__main__':
    iterating_over_string()
    multiple_lines_string()
