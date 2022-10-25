from random import randint

# 1 task (4.6)

print('1 task\n')

a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)

print(f"{a=}")
print(f"{b=}")
print(f"{c=}")

average = (a + b + c) // 3
print(f"{average=}")

# 2 task

print('\n2 task\n')

a = randint(0, 100)
b = randint(0, 100)

print(f"{a=}")
print(f"{b=}")

result = a // b
remainder = a % b
print(f"{result=}, {remainder=}")

# 3 task

print('\n3 task\n')

number = 18.722

print("1) {0:.2f}".format(number))
print("2) {0:.0f}".format(number))
print("3) {0:011}".format(number))