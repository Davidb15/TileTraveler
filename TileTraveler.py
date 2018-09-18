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
                if direction == 'n' or 'N':
                    j = 2
                else:
                    print("Not a valid direction")

        elif location == '12':
            print(travel + north + ' or ' + east + ' or ' + south + '.')
            direction = str(input("Direction: "))
                if direction == 'n' or 'N':
                    j = 2 
                elif direction == 's' or 'S':
                    j = 1
                elif direction == 'e' or 'E':
                    i = 2
                else:
                    print("Not a valid direction")

        elif location == '13':
            print(travel + east + ' or ' + south + '.')
            direction = str(input("Direction: "))
                if direction == 'e' or 'E':
                    i = 2
                elif direction == 's' or 'S':
                    j = 2
                else:
                    print("Not a valid direction")

        elif location == '21':
            print(travel + north + '.')
            direction = str(input("Direction: "))
                if direction == 'n' or 'N':
                    j = 2
                else:
                    print("Not a valid direction")

        elif location == '22':
            print(travel + south + ' or ' + west + '.')
            direction = str(input("Direction: "))
                if direction == 's' or 'S':
                    j = 1
                elif direction == 'w' or 'W':
                    i = 1
                else:
                    print("Not a valid direction")

        elif location == '23':
            print(travel + east + ' or ' + west + '.')
            direction = str(input("Direction: "))
                if direction == 'e' or 'E':
                    i = 3
                elif direction == 'w' or 'W':
                    i = 1
                else:
                    print("Not a valid direction")

        elif location == '33':
            print(travel + south + ' or ' + west + '.')
            direction = str(input("Direction: "))
                if direction == 's' or 'S':
                    j = 2
                elif direction == 'w' or 'W':
                    i = 2
                else:
                    print("Not a valid direction")

        elif location == '32':
            print(travel + north + ' or ' + south + '.')
            direction = str(input("Direction: "))
                if direction == 's' or 'S':
                    j = 1
                elif direction == 'n' or 'N':
                    j = 3
                else:
                    print("Not a valid direction")
                
        else:
            print('Victory!')
            j = 5
            i = 5
        