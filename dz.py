import math

# 1 задание
number1 = int(input("Введите 1 число:"))
number2 = int(input("Введите 2 число:"))
number3 = int(input("Введите 3 число:"))
sum = number1 + number2 + number3
mult = number1 * number3 * number2
print("Сумма:", sum)
print("Произведение:", mult)

# 2 задание
salary = int(input())
credit = int(input())
debt = int(input())
rest = salary - (credit + debt)
print("У вас осталось:", rest)

# 3 задание
side_1 = int(input())
side_2 = int(input())
area = (side_1 * side_2)*0.5
print("Площадь ромба=", area)

# 4 задание
print("To \n be or not to be")

# 5 задание
print('"Life is what happens\n when\n  you`re busy making other plans"\n   John Lennon')

# еще задания:
# 1задание
d = int(input())
ls = d * 3.14
print("Длина окружности равна:", ls)

# 2 задание
radius = int(input())
S = 3.14*(radius*radius)
Length = 2 * 3.14 * radius
print("Длина:", Length, "\nПлощадь", S)

# 3 задание
a = int(input())
b = int(input())
if (a >= 0 and b >= 0):
    result = a*b
    print("Результат:", math.sqrt(result))

# 4 задание
Length_ = float(input())
rad = Length_/(2*3.14)
square = 3.14 * (rad**2)
print("радиус =", rad)
print("площадь=", square)

# 5 задание
x = int(input())
y = 3 * x**2 - 6*x - 7
print("Ответ:", y)

# 6 задание
z = int(input())
c = 4*(z-3)-7*(z-3)+2
print("Ответ:", c)
