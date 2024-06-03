from random import randint



x = randint(1, 10)
while True:
    input_text = int(input('введите любое число:'))
    if input_text > x:
        print('Ваше число больше нужного')
    elif input_text < x:
        print('Ваше число меньше нужного')
    elif input_text == x:
        print('Вы мыслите как компьютер!')
        break
print('Отличная работа')