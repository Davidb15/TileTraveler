north = '(N)orth'
east = '(E)ast'
west = '(W)est'
south = '(S)outh'
travel = 'You can travel: '

for i in range(1,4):
    for j in range(1,4):
        location = str(i) + str(j)
        
    if location == 11:
        move = str(input(travel + north + '.'))

    elif location == 12:
        move = str(input(travel + north + ' or ' + east + ' or ' + south + '.'))

    elif location == 13:
        move = str(input(travel + east + ' or ' + south + '.'))

    elif location == 21:
        move = str(input(travel + north + '.'))

    elif location == 22:
        move = str(input(travel + south + ' or ' + west + '.'))

    elif location == 23:
        move = str(input(travel + east + ' or ' + west + '.'))

    elif location == 31:
        move = str(input(travel + south + ' or ' + west + '.'))

    elif location == 32:
        move = str(input(travel + north + ' or ' + south + '.'))

    else:
        print('Victory!')

        