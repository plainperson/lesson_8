class Date:
    def __init__(self, day, month, year):
        self.d = day
        self.m = month
        self.y = year

    @classmethod
    def set_numbers(cls, data):
        day, month, year = data.split('-')
        day = int(day)
        month = int(month)
        year = int(year)
        return cls(day, month, year)

    @staticmethod
    def get_numbers(obj):
        while True:
            if obj.d > 31:
                return f'такой даты не существует'
            if obj.m > 12:
                return f'такой даты не существует'
            if obj.y < 0:
                return f'такой даты не существует'

N1 = '02-12-2010'

v1 = Date.set_numbers(N1)
print(v1.m)
print(Date.get_numbers(v1))