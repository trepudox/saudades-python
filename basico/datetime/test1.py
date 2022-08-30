import datetime


def separator():
	print("-----------------------------")


if __name__ == '__main__':
	separator()

	print("Date:")
	print(f"date.today(): {datetime.date.today()}")
	created_date = datetime.date(2002, 7, 1)
	print(f"created_date: {created_date}")
	print(f"created_date.replace(day=31): {created_date.replace(day=31)}")

	separator()

	print("Time:")
	created_time = datetime.time(hour=5, minute=20)
	print(created_time)

	separator()

	print("Datetime:")
	print(datetime.datetime.combine(date=created_date, time=created_time))
