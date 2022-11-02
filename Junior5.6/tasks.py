#1 Task

inputs = input('Введите целое число: ')
inputsValue = int(inputs)

divThree = inputsValue % 3
divFive = inputsValue % 5

if divThree == 0:
    print('Fizz', end=' ')
if divFive == 0:
    print('Buzz', end=' ')
elif divThree != 0:
    print(inputsValue)

#2 Task

inputs = input('Введите целое число x: ')
inputsValue = int(inputs)

if inputsValue % 2 != 0:
    print('Плохо')
elif inputsValue >= 2 and inputsValue <= 5:
    print('Неплохо')
elif inputsValue >= 6 and inputsValue <= 20:
    print('Так себе')
elif inputsValue > 20:
    print('Отлично')

#3 Task

inputs = input('Введите целое число от 1 до 9 включая: ')
inputsValue = int(inputs)

if inputsValue < 1:
    print('Число введено неверно!')
elif inputsValue > 9:
    print('Число введено неверно!')

for i in range(0, inputsValue):
    print(i + 1, end='')

#4 Task

text = 'How are you? Eh, ok. Low or Lower? Ohhh.'

result = ''

for char in text:
    if char.isupper():
        result = result + char

print(result)