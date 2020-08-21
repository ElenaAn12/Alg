# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

#  ------------ Не верно
letter1 = input('Введите первую букву: ')
letter2 = input('Введите вторую букву: ')
alfabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
let1 = alfabet.index(letter1) + 1
let2 = alfabet.index(letter2) + 1
dif = let2 - let1
print(f'Буква "{letter1}" {let1}-ая по счету.')
print(f'Буква "{letter2}" {let2}-ая по счету.')
print(f'Между "{letter1}" и "{letter2}" {dif} букв.')


# ---------------- Верно
letter1 = ord(input('Введите первую букву: '))
letter2 = ord(input('Введите вторую букву: '))
letter1 = letter1 - ord('a') + 1
letter2 = letter2 - ord('a') + 1
print(f'letter1 = {letter1}, letter2 = {letter2}')
print(f'{abs(letter1 - letter2) - 1} ')

# ------------------ Верно
import string
a = string.ascii_lowercase
print(a)


