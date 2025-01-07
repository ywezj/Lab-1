
print('№1 флаг Японии')
WHITE = '\x1b[48;5;15m'
RED = '\x1b[48;5;196m'
STOP = '\x1b[0m'
LENGHT = 40

def lines(color, ln):
    line = ' ' * ln
    print(color, line, STOP, end='')
    print(f"{color}{' ' * ln}{STOP}", end='')

def flag():

    for i in range(2):
        lines(WHITE, LENGHT)
        print()

    lines(WHITE, 12)
    print(f"{RED}{' ' * 7}{WHITE}{' ' * 22}{STOP}")

    lines(WHITE, 11)
    print(f"{RED}{' ' * 11}{WHITE}{' ' * 20}{STOP}")

    lines(WHITE, 11)
    print(f"{RED}{' ' * 11}{WHITE}{' ' * 20}{STOP}")

    lines(WHITE, 11)
    print(f"{RED}{' ' * 11}{WHITE}{' ' * 20}{STOP}")

    lines(WHITE, 11)
    print(f"{RED}{' ' * 11}{WHITE}{' ' * 20}{STOP}")

    lines(WHITE, 12)
    print(f"{RED}{' ' * 7}{WHITE}{' ' * 22}{STOP}")

    for i in range(2):
        lines(WHITE, LENGHT)
        print()

flag()

print('№2 график функции y=3x')
HEIGHT = 20
WIDTH = 20

def print_line(spaces):
    print(f"{' ' * spaces}{WHITE} {STOP}")


def print_graph(height):
    for i in range(height, 0, -1):
        print_line(i)


print_graph(HEIGHT)



print('№3 узор')

print(f"{STOP}{' ' * 8}{WHITE}{' ' * 1}{STOP}{' ' * 15}{WHITE}{' ' * 1}{STOP}")
indent=7
distance=13
between=1
for i in range(7):
    print(f"{STOP}{' ' * indent}{WHITE}{' ' * 1}{STOP}{' ' * between}{WHITE}{' ' * 1}{STOP}{' ' * distance}{WHITE}{' ' * 1}{STOP}{' ' * between}{WHITE}{' ' * 1}{STOP}")
    indent-=1
    distance-=2
    between+=2
    

print(f"{WHITE}{' ' * 1}{STOP}{' ' * 15}{WHITE}{' ' * 1}{STOP}{' ' * 15}{WHITE}{' ' * 1}{STOP}{' ' * 1}")

indent=1
distance=1
between=13
for i in range(7):
    print(f"{STOP}{' ' * indent}{WHITE}{' ' * 1}{STOP}{' ' * between}{WHITE}{' ' * 1}{STOP}{' ' * distance}{WHITE}{' ' * 1}{STOP}{' ' * between}{WHITE}{' ' * 1}{STOP}")
    indent+=1
    distance+=2
    between-=2

print(f"{STOP}{' ' * 8}{WHITE}{' ' * 1}{STOP}{' ' * 15}{WHITE}{' ' * 1}{STOP}")


print('№4 Файл')
countmore = 0
countless = 0
with open('sequence.txt') as sequence:

    data = [ float(line) for line in sequence]
for i in range(250):
    if data[i] < 0:
        if abs(data[i]) > 5:
            countless += 1
        if abs(data[i]) < 5:
            countmore += 1
print(countmore,' ',countless)
for g in range(countmore):
    if countmore - g > countless:
        print(WHITE + ' ' * 2 + STOP)
    else:
        print(WHITE + ' ' * 2 + STOP + ' ' * 3 + WHITE + ' ' * 2 + STOP )
