# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/
def func(arr: list[int]) -> None:
    max_item: int = max(arr)
    final_arr: list[int] = [i for i in arr if i != max_item]
    runner_up: int = max(final_arr)

    print(runner_up)


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    func(array)
