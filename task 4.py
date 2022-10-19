# class Office_mashines:
#     colour = 'white'
#     company = 'Samsung'
#
#
# class Printer(Office_mashines):
#     def __init__(self, year, made_in):
#         self.year = year
#         self.made_in = made_in
#
#
# class Xerox(Office_mashines):
#     def __init__(self, year, made_in):
#         self.year = year
#         self.made_in = made_in
#
#
# class Scaner(Office_mashines):
#     def __init__(self, year, made_in):
#         self.year = year
#         self.made_in = made_in
#
#
# printer1 = Printer(2020, 'Korea')
# print(printer1.made_in)
#
# xerox1 = Xerox(2022, 'China')
# print(xerox1.year)
#
# scaner1 = Scaner(2018, 'USA')
# print(scaner1.colour)



# class Office_mashines:
#     colour = 'white'
#     company = 'Samsung'
#
#
# class Printer(Office_mashines):
#     def __init__(self, name, year, made_in):
#         self.name = name
#         self.year = year
#         self.made_in = made_in
#
#     def get_info(self):
#         return f'name: {self.name} year: {self.year} made_in: {self.made_in}'
#
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
#
# printer1 = Printer('printer1', 2020, 'Korea')
# print(printer1.get_info())
# print(printer1.colour)
#
# xerox1 = Xerox('xerox1', 2018, 'China')
# print(xerox1.get_info())
# print(xerox1.company)
#
# scaner1 = Scaner('scaner1', 2021, 'USA')
# print(scaner1.get_info())
# print(scaner1.colour)



class Office_mashines:
    colour = 'white'
    company = 'Samsung'


class Printer(Office_mashines):
    def __init__(self, name, year, made_in):
        self.name = name
        self.year = year
        self.made_in = made_in

    def get_info(self):
        return f'name: {self.name} year: {self.year} made_in: {self.made_in}'


class Xerox(Office_mashines):
    def __init__(self, name, year, made_in):
        self.name = name
        self.year = year
        self.made_in = made_in

    def get_info(self):
        return f'name: {self.name} year: {self.year} made_in: {self.made_in}'


class Scaner(Office_mashines):
    def __init__(self, name, year, made_in):
        self.name = name
        self.year = year
        self.made_in = made_in

    def get_info(self):
        return f'name: {self.name} year: {self.year} made_in: {self.made_in}'


printer1 = Printer('printer1', 2020, 'Korea')
print(printer1.get_info())
print(printer1.company)

xerox1 = Xerox('xerox1', 2018, 'China')
print(xerox1.get_info())
print(xerox1.company)

scaner1 = Scaner('scaner1', 2021, 'USA')
print(scaner1.get_info())
print(scaner1.colour)
