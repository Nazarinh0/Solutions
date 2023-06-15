# Реализуйте абстракцию (набор функций) для работы с прямоугольником, стороны которого всегда параллельны осям.
# Прямоугольник может располагаться в любом месте координатной плоскости.

# При такой постановке задачи достаточно знать только три параметра для однозначного задания прямоугольника на плоскости:
# координаты левой-верхней точки, ширину и высоту.
# Зная их, мы всегда можем построить прямоугольник одним единственным способом.

# Основной интерфейс:

# make (конструктор) - создаёт прямоугольник. принимает параметры: левую-верхнюю точку, ширину и высоту.
# Селекторы get_start_point, get_width и get_height
# Вспомогательные функции для выполнения расчетов:

# get_square - возвращает площадь прямоугольника (a * b).
# get_perimeter - возвращает периметр прямоугольника (2 * (a + b)).
# contains_the_origin - проверяет, принадлежит ли центр координат прямоугольнику (не лежит на границе прямоугольника, а находится внутри). 
# Чтобы в этом убедиться, достаточно проверить, что все вершины прямоугольника лежат в разных квадрантах (их можно вычислить в момент проверки).


# BEGIN
def make(point, width, height):
    return cons(point, cons(width, height))


def get_start_point(rectangle):
    return car(rectangle)


def get_height(rectangle):
    return cdr(cdr(rectangle))


def get_width(rectangle):
    return car(cdr(rectangle))


def get_square(rectangle):
    return get_height(rectangle) * get_width(rectangle)


def get_perimeter(rectangle):
    return 2 * (get_height(rectangle) + get_width(rectangle))


def contains_the_origin(rectangle):
    point1 = get_start_point(rectangle)
    x = get_x(point1) + get_width(rectangle)
    y = get_y(point1) - get_height(rectangle)
    point2 = make_point(x, y)

    return get_quadrant(point1) == 2 and get_quadrant(point2) == 4
# END
