# 1 task (3.6)

print('1 task\n')

name = 'Ibrahim'
surname = 'Petrov'

print(f'Hello {name} {surname}! You just delved into Python. Great start!')

# 2 task

print('\n2 task\n')

thickness = 5
c = 'H'

# Top Cone
for i in range(thickness):
    print(f"{c * i}".rjust(thickness - 1) + c + f"{c * i}".ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print(f"{c * thickness}".center(thickness * 2) + f"{c * thickness}".center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print(f"{c * thickness * 5}".center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print(f"{c * thickness}".center(thickness * 2) + f"{c * thickness}".center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print((f"{c * (thickness - i - 1)}".rjust(thickness) + c + f"{c * (thickness - i - 1)}".ljust(thickness)).
          rjust(thickness * 6))

# 3 task

print('\n3 task\n')

title = 'hello world!'

print(title.title())

# 4 task

print('\n4 task\n')

amount = 1000600.152

if amount > 0:
    print("{0:,.2f}".format(amount))

# 5 task

print('\n5 task\n')

width = 11
height = 3 * width
symb = '-'
centerTop = '/|\\'
center = '|||'
centerBottom = '\\|/'

for i in range(1, width, 2):
    print((centerTop * i).center(height, symb))
print(((width - 2) * center).center(height, symb))
for i in range(width - 2, 0, -2):
    print((centerBottom * i).center(height, symb))
