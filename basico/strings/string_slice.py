def slicing_strings(string: str = "string"):
    # o slice tem o primeiro parâmetro inclusivo e o segundo exlcusivo
    print(f"Slice 1: {string[0:]}")  # do começo ao final
    print(f"Slice 2: {string[::2]}")  # de 2 em 2
    print(f"Slice 2: {string[::-1]}")  # ao contrario


if __name__ == '__main__':
    slicing_strings()
