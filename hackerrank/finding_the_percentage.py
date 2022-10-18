# https://www.hackerrank.com/challenges/finding-the-percentage/
def average(grades: list[int] | list[float]) -> float:
	grades_sum: int = sum(grades)
	grades_length: int = grades.__len__()
	return grades_sum / grades_length


if __name__ == '__main__':
	n = int(input())
	student_marks = {}
	for _ in range(n):
		name, *line = input().split()
		scores = list(map(float, line))
		student_marks[name] = scores
	query_name = input()

	print("%.2f" % average(student_marks[query_name]))
