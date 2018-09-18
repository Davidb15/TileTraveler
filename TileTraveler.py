north = '(N)orth'
east = '(E)ast'
west = '(W)est'
south = '(S)outh'
travel = 'You can travel: '
i = 1
j = 1

while i < 4:
    while j < 4:
        location = str(i) + str(j)
        
        if location == '11':
            print(travel + north + '.')
            direction = str(input("Direction: "))
            if direction in 'nN':
                j = 2
            else:
                print("Not a valid direction")

        elif location == '12':
            print(travel + north + ' or ' + east + ' or ' + south + '.')
            direction = str(input("Direction: "))
            if direction in 'nN':
                j = 3 
            elif direction in 'sS':
                j = 1
            elif direction in 'eE':
                i = 2
            else:
                print("Not a valid direction")

        elif location == '13':
            print(travel + east + ' or ' + south + '.')
            direction = str(input("Direction: "))
            if direction in 'eE':
                i = 2
            elif direction in 'sS':
                j = 2
            else:
                print("Not a valid direction")

        elif location == '21':
            print(travel + north + '.')
            direction = str(input("Direction: "))
            if direction in 'nN':
                j = 2
            else:
                print("Not a valid direction")

        elif location == '22':
            print(travel + south + ' or ' + west + '.')
            direction = str(input("Direction: "))
            if direction in 'sS':
                j = 1
            elif direction in 'wW':
                i = 1
            else:
                print("Not a valid direction")

        elif location == '23':
            print(travel + east + ' or ' + west + '.')
            direction = str(input("Direction: "))
            if direction in 'eE':
                i = 3
            elif direction in 'wW':
                i = 1
            else:
                print("Not a valid direction")

        elif location == '33':
            print(travel + south + ' or ' + west + '.')
            direction = str(input("Direction: "))
            if direction in 'sS':
                j = 2
            elif direction in 'wW':
                i = 2
            else:
                print("Not a valid direction")

        elif location == '32':
            print(travel + north + ' or ' + south + '.')
            direction = str(input("Direction: "))
            if direction in 'sS':
                j = 1
            elif direction in 'nN':
                j = 3
            else:
                print("Not a valid direction")
                
        else:
            print('Victory!')
            j = 5
            i = 5