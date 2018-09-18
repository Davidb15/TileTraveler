#function fallið mitt tekur in hvaða stafir eru valid og þannig finn ég breytinguna á i og j
#i og j breytast þá eftir því sem er gert í function fallinu.

north = '(N)orth'
east = '(E)ast'
west = '(W)est'
south = '(S)outh'
travel = 'You can travel: '
i = 1
j = 1
def find_direction(valid,i,j):
    while True:
        direction = str(input("Direction: "))
        if direction in valid:
            if direction in 'sS':
                j -= 1
                return i,j
            elif direction in 'nN':
                j += 1
                return i,j
            elif direction in 'wW':
                i -= 1
                return i,j
            else:
                i += 1
                return i,j
        else:
            print("Not a valid direction!")


while i < 4:
    while j < 4:
        location = str(i) + str(j)

        if location == '11':
            print(travel + north + '.')
            valid = 'nN'
            i, j = find_direction(valid,i,j)

        elif location == '12':
            print(travel + north + ' or ' + east + ' or ' + south + '.')
            valid = 'nNeEsS'
            i, j = find_direction(valid,i,j)

        elif location == '13':
            print(travel + east + ' or ' + south + '.')
            valid = 'eEsS'
            i, j = find_direction(valid,i,j)

        elif location == '21':
            print(travel + north + '.')
            valid = 'nN'
            i, j = find_direction(valid,i,j)

        elif location == '22':
            print(travel + south + ' or ' + west + '.')
            valid = 'sSwW'
            i, j = find_direction(valid,i,j)

        elif location == '23':
            print(travel + east + ' or ' + west + '.')
            valid = 'eEwW'
            i, j = find_direction(valid,i,j)

        elif location == '33':
            print(travel + south + ' or ' + west + '.')
            valid = 'SswW'
            i, j = find_direction(valid,i,j)

        elif location == '32':
            print(travel + north + ' or ' + south + '.')
            valid = 'nNSs'
            i, j = find_direction(valid,i,j)

        else:
            print('Victory!')
            j = 5
            i = 5