if __name__ == '__main__':
    t: tuple[int, int, int, int, int] = (1, 2, 3, 3, 4)
    print(t)

    print(t.count(1))
    print(t.count(3))

    print(t.index(4))
