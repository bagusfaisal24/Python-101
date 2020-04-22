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
