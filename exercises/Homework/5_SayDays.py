class SayDays:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def is_leap(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def days(self):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap(self.year):
            month_days[1] = 29

        total = 0
        for i in range(self.month - 1):
            total += month_days[i]
        total += self.day
        return total

    def days_left(self):
        if self.is_leap(self.year):
            total_days = 366
        else:
            total_days = 365
        return total_days - self.days()

    def weekday(self):
        q = self.day
        m = self.month
        y = self.year
        if m < 3:
            m += 12
            y -= 1

        K = y % 100
        J = y // 100
        h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
        return h

    def weekday_name(self):
        names = ["토요일", "일요일", "월요일", "화요일", "수요일", "목요일", "금요일"]
        return names[self.weekday()]

temp = SayDays(2026, 4, 9)
print(temp.days_left())