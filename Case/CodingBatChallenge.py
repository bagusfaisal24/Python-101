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


## parrot trouble
# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return true if we are in trouble.
def parrot_trouble(talking, hour):
    a = (talking and (hour < 7 or hour > 20))
    print(a)
    return a


parrot_trouble(True, 20)
parrot_trouble(True, 6)
parrot_trouble(False, 6)


## makes 10
# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
def makes10(a, b):
    a = (a == 10 or b == 10 or a + b == 10)
    print(a)
    return a


makes10(1, 9)
makes10(9, 10)
makes10(9, 9)


## near hundred
# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
def nearHundred(n):
    a = (abs(100 - n) <= 10 or abs(200 - n) < 10)
    print(a)
    return a


nearHundred(93)
nearHundred(90)
nearHundred(89)


## pos_ neg
# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative.

def posNeg(a, b, negative):
    if negative:
        a = (a < 0 and b < 0)
        print(a)
        return a
    else:
        a = ((a < 0 and b > 0) or (a > 0 and b < 0))
        print(a)
    return a


posNeg(1, -1, False)
posNeg(-1, 1, False)
posNeg(-4, -5, False)
posNeg(4, 1, True)
## Sumber codingbat.com
