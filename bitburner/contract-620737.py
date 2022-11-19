import re


def f() -> list[str]:
    sequencia: str = "736770654"
    symbols: list[str] = ["+", "-", "*", ""]
    numbers: list[str] = list(sequencia)

    l = [[n+s if nIndex != len(numbers) - 1 else n for s in symbols] for nIndex, n in enumerate(numbers)]

    l2 = [e0+e1+e2+e3+e4+e5+e6+e7+e8 for e0 in l[0]
          for e1 in l[1]
          for e2 in l[2]
          for e3 in l[3]
          for e4 in l[4]
          for e5 in l[5]
          for e6 in l[6]
          for e7 in l[7]
          for e8 in l[8]]

    l3 = [exp for exp in l2 if re.match(r".*\D0\d.*", exp) is None and eval(exp) == 30]

    return l3


if __name__ == '__main__':
    result: list[str] = f()
    result_string = result.__str__().replace("'", "")
    print(result_string)
