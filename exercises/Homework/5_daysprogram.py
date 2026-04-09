import SayDays

while True:
    year, month, day = map(int, input("년 월 일 띄어쓰기로 구분하여 입력 : ").split())

    temp = SayDays.SayDays(year, month, day)
    print(temp.days())
    print(temp.days_left())
    print(temp.weekday())
    print(temp.weekday_name())
    