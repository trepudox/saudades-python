import time


def sum():
    x = 0
    for i in range(100000000):
        x += 1

    return x


if __name__ == '__main__':
    init = round(time.time() * 1000)
    print(sum())
    end = round(time.time() * 1000)
    print(f"Total time: {end - init} ms")
