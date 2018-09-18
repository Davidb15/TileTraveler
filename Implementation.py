# 2 function föll, annað athugar hvaða input væri valid til þess að slá inn í direction útfrá location
# Direction fallið athugar hvort inputið sé valid og skilar eftirfarandi niðurstöðu frá því

# 1. The second implementation was a lot easier than the first one, using functions to do this kind of an assignment
# is a lot easier, it was also very easy to have already written up the code before doing the second assignment
# 2. The second implementation is a lot more readable because there is almost to text inside the main while loops. There
# is only the function calls and and if and else statement
# 3. I was able to solve the valid text because it was a lot easier with functions, and it also helped a lot doing just
# one algorithm for moving direction instead of having for every single if statement in the first assignment
# I can see the big difference because there are like 60 lines less in assignement 2 than in assignment 1.

north = '(N)orth'
east = '(E)ast'
west = '(W)est'
south = '(S)outh'
travel = 'You can travel: '
i = 1
j = 1
valid = ''
text = ''
def valid_input(valid,location,text):
    if location == '11':
        text = travel + north + '.'
        valid = 'nN'
        return valid,text

    elif location == '12':
        text = travel + north + ' or ' + east + ' or ' + south + '.'
        valid = 'nNeEsS'
        return valid,text

    elif location == '13':
        text = travel + east + ' or ' + south + '.'
        valid = 'eEsS'
        return valid,text

    elif location == '21':
        text = travel + north + '.'
        valid = 'nN'
        return valid,text

    elif location == '22':
        text = travel + south + ' or ' + west + '.'
        valid = 'sSwW'
        return valid,text

    elif location == '23':
        text = travel + east + ' or ' + west + '.'
        valid = 'eEwW'
        return valid,text

    elif location == '33':
        text = travel + south + ' or ' + west + '.'
        valid = 'SswW'
        return valid,text

    elif location == '32':
        text = travel + north + ' or ' + south + '.'
        valid = 'nNSs'
        return valid,text

    else:
        text = 'Victory!'
        valid = ''
        return valid,text

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

        valid, text = valid_input(valid,location,text)
        print(text)

        if text == 'Victory!':
            i = 5
            j = 5

        else:
            i, j = find_direction(valid,i,j)