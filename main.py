
print('№1 флаг Японии')
white = '\x1b[48;5;15m'
red = '\x1b[48;5;196m'
stop = '\x1b[0m'
len = 40

def linii(color, ln):
    line = ' ' * ln
    print(color, line, stop, end='')

def flag():

    for i in range(3):
        linii(white, len)
        print()
    linii(white,14)
    print(red + ' ' * 9 + white + ' ' * 17 + stop)

    linii(white,12)
    print(red + ' ' * 13 + white + ' ' * 15 + stop)
    linii(white,12)
    print( red + ' ' * 13 + white + ' ' * 15 + stop)
    linii(white,12)
    print(red + ' ' * 13 + white + ' ' * 15 + stop)
    linii(white,12)
    print( red + ' ' * 13 + white + ' ' * 15 + stop)
    linii(white,14)
    print(red + ' ' * 9 + white + ' ' * 17 + stop)
    for i in range(3):
        linii(white, len)
        print()
flag()

print('№2 график функции y=3x')
white = '\x1b[48;5;15m'
stop = '\x1b[0m'

def f(Ox):
    print((Ox) + (white) + ' ', stop)


h = 20
w = 20

def xy(h, w):
    for i in range(h, 0, -1):
        f(' ' * i )


xy(h, w)





print('№3 узор')
white = '\x1b[48;5;15m'
stop = '\033[0m'
print(stop + ' ' * 8 + white + ' ' * 1 + stop + ' ' * 15 + white + ' ' * 1 + stop)
print(stop + ' ' * 7 + white + ' ' * 1 + stop + ' ' * 1 + white + ' ' * 1 + stop + ' ' * 13  + white + ' ' * 1 + stop + ' ' * 1 +white+ ' ' * 1 + stop)
print(stop + ' ' * 6 + white + ' ' * 1 + stop + ' ' * 3 + white + ' ' * 1 + stop + ' ' * 11  + white + ' ' * 1 + stop + ' ' * 3 +white+ ' ' * 1 + stop)
print(stop + ' ' * 5 + white + ' ' * 1 + stop + ' ' * 5 + white + ' ' * 1 + stop + ' ' * 9  + white + ' ' * 1 + stop + ' ' * 5 +white+ ' ' * 1 + stop)
print(stop + ' ' * 4 + white + ' ' * 1 + stop + ' ' * 7 + white + ' ' * 1 + stop + ' ' * 7  + white + ' ' * 1 + stop + ' ' * 7 +white+ ' ' * 1 + stop)
print(stop + ' ' * 3 + white + ' ' * 1 + stop + ' ' * 9 + white + ' ' * 1 + stop + ' ' * 5  + white + ' ' * 1 + stop + ' ' * 9 +white+ ' ' * 1 + stop)
print(stop + ' ' * 2 + white + ' ' * 1 + stop + ' ' * 11 + white + ' ' * 1 + stop + ' ' * 3  + white + ' ' * 1 + stop + ' ' * 11 +white+ ' ' * 1 + stop)
print(stop + ' ' * 1 + white + ' ' * 1 + stop + ' ' * 13 + white + ' ' * 1 + stop + ' ' * 1  + white + ' ' * 1 + stop + ' ' * 13 +white+ ' ' * 1 + stop)
print(white + ' ' * 1 + stop +' ' * 15  + white + ' ' * 1 + stop + ' ' * 15 + white + ' ' * 1 + stop + ' ' * 20  )
print(stop + ' ' * 1 + white + ' ' * 1 + stop + ' ' * 13 + white + ' ' * 1 + stop + ' ' * 1  + white + ' ' * 1 + stop + ' ' * 13 +white+ ' ' * 1 + stop)
print(stop + ' ' * 2 + white + ' ' * 1 + stop + ' ' * 11 + white + ' ' * 1 + stop + ' ' * 3  + white + ' ' * 1 + stop + ' ' * 11 +white+ ' ' * 1 + stop)
print(stop + ' ' * 3 + white + ' ' * 1 + stop + ' ' * 9 + white + ' ' * 1 + stop + ' ' * 5  + white + ' ' * 1 + stop + ' ' * 9 +white+ ' ' * 1 + stop)
print(stop + ' ' * 4 + white + ' ' * 1 + stop + ' ' * 7 + white + ' ' * 1 + stop + ' ' * 7  + white + ' ' * 1 + stop + ' ' * 7 +white+ ' ' * 1 + stop)
print(stop + ' ' * 5 + white + ' ' * 1 + stop + ' ' * 5 + white + ' ' * 1 + stop + ' ' * 9  + white + ' ' * 1 + stop + ' ' * 5 +white+ ' ' * 1 + stop)
print(stop + ' ' * 6 + white + ' ' * 1 + stop + ' ' * 3 + white + ' ' * 1 + stop + ' ' * 11  + white + ' ' * 1 + stop + ' ' * 3 +white+ ' ' * 1 + stop)
print(stop + ' ' * 7 + white + ' ' * 1 + stop + ' ' * 1 + white + ' ' * 1 + stop + ' ' * 13  + white + ' ' * 1 + stop + ' ' * 1 +white+ ' ' * 1 + stop)
print(stop + ' ' * 8 + white + ' ' * 1 + stop + ' ' * 15 + white + ' ' * 1 + stop)




print('№4 Файл')
countbolsh = 0
countmensh = 0
f = open('sequence.txt')

l = [ float(i) for i in f]
for i in range(250):
    if l[i] < 0:
        if abs(l[i]) > 5:
            countmensh += 1
        if abs(l[i]) < 5:
            countbolsh += 1
print(countbolsh,' ',countmensh)
white = '\x1b[48;5;15m'
stop = '\x1b[0m'
for g in range(countbolsh):
    if countbolsh - g > countmensh:
        print(white + ' ' * 2 + stop)
    else:
        print(white + ' ' * 2 + stop + ' ' * 3 + white + ' ' * 2 + stop )