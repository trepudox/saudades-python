if __name__ == '__main__':
    string = "oi"

    # type() retorna o tipo do objeto
    print(type(string))  # == print(str)

    # dir() lista os metodos disponiveis
    print(dir(str))

    # retorna a documentacao do metodo
    help(str.join)

    # retorna a documentacao da classe
    help(str)
