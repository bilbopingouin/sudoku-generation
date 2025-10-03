def graph(string):
    print('=============')
    for i in range(9):
        if i % 3 == 0:
            print('-'*(3*2+9*2+1))
        for j in range(9):
            if (j % 3 == 0):
                print('| ', end='')
            c = string[j+i*9]

            if '0' == c:
                print('_', end=' ')
            else:
                print(c, end=' ')
        print('|')
