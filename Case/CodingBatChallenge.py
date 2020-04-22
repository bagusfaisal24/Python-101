## sleep_in
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        print('sleepin', True)
    else:
        print('sleepin', False)

sleep_in(False, True)


## monkey trouble
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        print('monkey trouble', True)
    elif not a_smile and not b_smile:
        print('monkey trouble', True)
    else:
        print('not trouble', False)

monkey_trouble(True, False)


## sum_double
def sum_double(a, b):
    if a != b:
        print('sum', a + b)
    elif a == b:
        print('sum double', (a + b) * 2)

sum_double(2, 2)


## dif21
def dif21(n):
    if n < 21:
        print('dif21', 21 - n)
    else:
        print('dif21', (n - 21) * 2)

dif21(2)
dif21(10)
dif21(21)
dif21(25)
## Sumber codingbat.com
