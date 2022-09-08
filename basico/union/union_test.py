from typing import Union

if __name__ == '__main__':
    str_or_int: Union[str, int]
    str_or_int = "string!"  # o Union indica que o valor será uma string ou um inteiro
    print(str_or_int)

    str_or_int = 10
    print(str_or_int)
