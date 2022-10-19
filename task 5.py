# class Office_mashines:
#     colour = 'white'
#     company = 'Samsung'
#
# class Printer(Office_mashines):
#     def __init__(self, name, year, made_in):
#         self.name = name
#         self.year = year
#         self.made_in = made_in
#
#     def Send_to_Department(self):
#         n = int(input('введите количество принтеров, которые Вы хотите направить в Офис'))
#         if n <= 5:
#             print('принтеры будут направлены в финансовый отдел')
#         elif n > 5 and n <= 10:
#             print('5 принтеров будут направлены к финансистам, остальные - в кадровый отдел')
#         elif n > 10:
#             print('10 принтеров будут направлены в Офис, остальные  - на склад')
#
#     def get_info(self):
#         return f'name: {self.name} year: {self.year} made_in: {self.made_in}'
#
# class Xerox(Office_mashines):
#     def __init__(self, name, year, made_in):
#         self.name = name
#         self.year = year
#         self.made_in = made_in
#
#     def get_info(self):
#         return f'name: {self.name} year: {self.year} made_in: {self.made_in}'
#
#
# class Scaner(Office_mashines):
#     def __init__(self, name, year, made_in):
#         self.name = name
#         self.year = year
#         self.made_in = made_in
#
#     def get_info(self):
#         return f'name: {self.name} year: {self.year} made_in: {self.made_in}'
#
# printer1 = Printer('printer1', 2020, 'Korea')
# printer1.Send_to_Department()


class Office_mashines:
    colour = 'white'
    company = 'Samsung'

class Printer(Office_mashines):
    def __init__(self, name, year, made_in):
        self.name = name
        self.year = year
        self.made_in = made_in

    def Send_to_Department(self):
        n = int(input('введите количество принтеров, которые Вы хотите направить в Офис'))
        if n <= 5:
            print('принтеры будут направлены в финансовый отдел')
        elif n > 5 and n <= 10:
            print('5 принтеров будут направлены к финансистам, остальные - в кадровый отдел')
        elif n > 10:
            print('10 принтеров будут направлены в Офис, остальные  - на склад')

    def get_info(self):
        return f'name: {self.name} year: {self.year} made_in: {self.made_in}'

class Xerox(Office_mashines):
    def __init__(self, name, year, made_in):
        self.name = name
        self.year = year
        self.made_in = made_in

    def Send_to_Department(self):
        n = int(input('введите количество ксероксов, которые Вы хотите направить в Офис'))
        if n <= 5:
            print('ксероксы будут направлены в финансовый отдел')
        elif n > 5 and n <= 10:
            print('5 ксероксов будут направлены к финансистам, остальные - в кадровый отдел')
        elif n > 10:
            print('10 ксероксов будут направлены в Офис, остальные  - на склад')

    def get_info(self):
        return f'name: {self.name} year: {self.year} made_in: {self.made_in}'


class Scaner(Office_mashines):
    def __init__(self, name, year, made_in):
        self.name = name
        self.year = year
        self.made_in = made_in

    def Send_to_Department(self):
        n = int(input('введите количество сканеров, которые Вы хотите направить в Офис'))
        if n <= 5:
            print('сканеры будут направлены в финансовый отдел')
        elif n > 5 and n <= 10:
            print('5 сканеров будут направлены к финансистам, остальные - в кадровый отдел')
        elif n > 10:
            print('10 сканеров будут направлены в Офис, остальные  - на склад')

    def get_info(self):
        return f'name: {self.name} year: {self.year} made_in: {self.made_in}'

printer1 = Printer('printer1', 2020, 'Korea')
printer1.Send_to_Department()

