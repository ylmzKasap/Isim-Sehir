def table_it(aList):
    longest = 0
    for i in range(len(aList)):
        if len(aList[i]) > longest:
            longest = len(aList[i])

    lengths = []
    for i in range(len(aList)):
        longestl = 0
        for ii in range(len(aList[i])):
            if len(str(aList[i][ii])) > longestl:
                longestl = len(str(aList[i][ii]))
        lengths += [longestl]

    listWidth = len(aList)
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

        for j in range(listWidth):
            if lengths[j] > 10:
                print((' ' * (lengths[j]+2) + '|'), end='')
            else:
                print((' ' * 10 + '|'), end='')

        print('\n|', end='')

        for ii in range(listWidth):
            try:
                if lengths[ii] > 10:
                    print(str(aList[ii][item]).center(lengths[ii]+2, ' ') + '|', end='')
                else:
                    print(str(aList[ii][item]).center(10, ' ') + '|', end='')

            except IndexError:
                if lengths[ii] > 10:
                    print(' ' * (lengths[ii]+2) + '|', end='')
                else:
                    print(' ' * 10 + '|', end='')

        print('\n|', end='')

        for j in range(listWidth):
            if lengths[j] > 10:
                print((' ' * (lengths[j]+2) + '|'), end='')
            else:
                print((' ' * 10 + '|'), end='')

        print('\n', end='')

        for k in range(listWidth):
            print(('—' * 11), end='')
            if lengths[k] > 10:
                print('—'*(lengths[i]-8), end='')
        item += 1
        print('—', end='')
    print()

