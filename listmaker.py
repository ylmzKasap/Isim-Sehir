def list_it(list):  # Liste yapıcı
    longest = 0
    for i in range(len(list)):
        if len(list[i]) > longest:
            longest = len(list[i])

    lengths = []
    for i in range(len(list)):
        longestl = 0
        for ii in range(len(list[i])):
            if len(str(list[i][ii])) > longestl:
                longestl = len(str(list[i][ii]))
        lengths += [longestl]

    listWidth = len(list)
    listLength = longest

    for i in range(listWidth):
        print(('—' * 11), end='')
        if lengths[i] > 10:
            print('—'*(lengths[i]-8), end='')
    print('—')
    item = 0

    for i in range(listLength):
        if i == 0:
            print('|', end='')
        else:
            print('\n|', end='')

        for i in range(listWidth):
            if lengths[i] > 10:
                print((' ' * (lengths[i]+2) + '|'), end='')
            else:
                print((' ' * 10 + '|'), end='')

        print('\n|', end='')

        for ii in range(listWidth):
            try:
                if lengths[ii] > 10:
                    print(str(list[ii][item]).center(lengths[ii]+2, ' ') + '|', end='')
                else:
                    print(str(list[ii][item]).center(10, ' ') + '|', end='')

            except IndexError:
                if lengths[ii] > 10:
                    print(' ' * (lengths[ii]+2) + '|', end='')
                else:
                    print(' ' * 10 + '|', end='')

        print('\n|', end='')

        for i in range(listWidth):
            if lengths[i] > 10:
                print((' ' * (lengths[i]+2) + '|'), end='')
            else:
                print((' ' * 10 + '|'), end='')

        print('\n', end = '')

        for i in range(listWidth):
            print(('—' * 11), end='')
            if lengths[i] > 10:
                print('—'*(lengths[i]-8), end='')
        item += 1
        print('—', end= '')
    print()

list_it([['İsim'], ['Şehir'], ['Hayvan', 'Eşek', 'Dana', 'Öküz']])
