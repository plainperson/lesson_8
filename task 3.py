# class Num_list(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# data = input('enter number: ')
# try:
#     data = int(data)
#     if type(data) == str:
#         raise Num_list('not a number')
#
# except (ValueError, Num_list) as err:
#     print(err)
# else:
#     print('num:', data)
# finally:
#     print('end')


class NotNumber(ValueError):
    pass

my_list = []
while True:
    try:
        element = input('Введите элемент списка:')
        if element == 'stop':
            break
        if not element.isdigit():
            raise NotNumber(element)
        else:
            my_list.append(int(element))
    except NotNumber as err:
        print('error')
print(my_list)


