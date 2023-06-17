# Display of a Rational number
# Формулы
# Сложение
# a/b + c/d = (a * d + b * c) / (b * d)
# Вычитание
# a/b - c/d = (a * d - b * c) / (b * d)
# Умножение
# a/b * c/d = (a * c) / (b * d)
# Деление
# a/b / c/d = (a * d) / (b * c)
# Равенство
# a/b = c/d, если a * d = c * b
#
# Реализуйте абстракцию для работы с рациональными числами, используя пары:
#
# Конструктор make(numer, denom)
# Селекторы numer() (числитель) и denom() (знаменатель)
# Функцию to_string(), возвращающую строковое представление рационального числа. Например для дроби 3/4 созданной так make(3, 4), строковым представлением будет 3 / 4
# Предикат is_equal(), проверяющую равенство двух рациональных чисел. Например is_equal(make(1, 2), make(2, 4))
# Функцию add(), выполняющую сложение дробей
# Функцию sub(), выполняющую вычитание дробей
# Функцию mul(), выполняющую умножение дробей
# Функцию div(), выполняющую деление дробей
# Обратите внимание, что результатом любой арифметической операции над рациональным числом будет рациональное число.
#
# rat1 = make(2, 3)
# rat12 = make(4, 6)
# rat2 = make(7, 2)
# to_string(rat12)  # '4 / 6'
# is_equal(rat1, rat12)  # True
# add(rat1, rat2)  # 25/6
# sub(rat2, rat1)  # 17/6
# mul(rat1, rat2)  # 14/6
# div(rat1, rat2)  # 4/21

# BEGIN (write your solution here)
def make(numer, denom):
    return cons(numer, denom)


def numer(rat):
    return car(rat)


def denom(rat):
    return cdr(rat)


def to_string(rat):
    return f'{numer} / {denom}'


def is_equal(rat1, rat2):
    a = numer(rat1)
    b = denom(rat1)
    c = numer(rat2)
    d = denom(rat2)
    return (a * d) == (c * b)


def add(rat1, rat2):
    a = numer(rat1)
    b = denom(rat1)
    c = numer(rat2)
    d = denom(rat2)
    return ((a * b) + (b * c)) / (b * d)


def sub(rat1, rat2):
    a = numer(rat1)
    b = denom(rat1)
    c = numer(rat2)
    d = denom(rat2)
    return ((a * d) - (b * c)) / (b * d)


def mul(rat1, rat2):
    a = numer(rat1)
    b = denom(rat1)
    c = numer(rat2)
    d = denom(rat2)
    return (a * c) / (b * d)


def div(rat1, rat2):
    a = numer(rat1)
    b = denom(rat1)
    c = numer(rat2)
    d = denom(rat2)
    return (a * d) / (b * c)
# END
