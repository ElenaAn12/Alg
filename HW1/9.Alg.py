# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Первое число: '))
b = int(input('Воторе число: '))
c = int(input('Третье число: '))

if a < b < c or c < a < b:
    print(b)
elif a < c < b:
    print(c)
else:
    print(a)

# ---------- Тоже Верно
# if b < a < c or c < a < b:
#     print(a)
# elif a < b < c or c < b < a:
#     print(b)
# else:
#     print(c)
