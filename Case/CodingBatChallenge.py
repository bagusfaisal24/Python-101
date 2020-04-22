## sleep_in
# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        print('sleepin', True)
    else:
        print('sleepin', False)

sleep_in(False, True)
sleep_in(True, True)
sleep_in(False, True)


## monkey trouble
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        print('monkey trouble', True)
    elif not a_smile and not b_smile:
        print('monkey trouble', True)
    else:
        print('not trouble', False)

monkey_trouble(True, False)
monkey_trouble(True, True)
monkey_trouble(False, True)


## sum_double
# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
def sum_double(a, b):
    if a != b:
        print('sum', a + b)
    elif a == b:
        print('sum double', (a + b) * 2)

sum_double(2, 2)


## dif21
# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
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
