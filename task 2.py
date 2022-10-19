class Numbers(Exception):
    def __init__(self, txt):
        self.txt = txt

num1 = input('введите число 1')
num2 = input('введите число 2')
try:
    num1 = int(num1)
    num2 = int(num2)
    if num2 == 0:
        raise Numbers('на ноль делить нельзя')
except (ValueError, Numbers) as err:
    print('err')
else:
    print(num1 / num2)
finally:
    print('конец')

