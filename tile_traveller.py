# https://github.com/TomasIV/TileTraveller/blob/master/tile_traveller.py

# Starting point er [1,1]
x = 11


# Skilgreina hvaða átt má færast í
def north(x):
    if (x % 10 == 3) or (x == 22) or (x == 31):
        return False
    return True
def east(x):
    if x == 12 or (x == 13) or (x == 23):
        return True
    return False
def south(x):
    if (x % 10 == 1) or (x == 23):
        return False
    return True
def west(x):
    if x == 22 or (x == 23) or (x == 33):
        return True
    return False



# Possible travel options prentast eftir hvert move
def possible_travel(n, e, s, w):
    direction = ""
    while direction == "":
        if n:
            direction += "(N)orth"
        elif e:
            direction += "(E)ast"
        elif s:
            direction += "(S)outh"
        elif w:
            direction += "(W)est"
    if e and direction != "(E)ast":
        direction += " or (E)ast"
    if s and direction != "(S)outh":
        direction += " or (S)outh"
    if w and direction != "(W)est":
        direction += " or (W)est"
    return direction



# Hreyfir staðsetningu spilarans
def move(x, string, n, e, s, w):
    if string == "N":
        if n:
            x += 1
    if string == "E":
        if e:
            x += 10
    if string == "S":
        if s:
            x -= 1
    if string == "W":
        if w:
            x -= 10
    return x



def user_input():
    UI = (input("Direction: "))
    UI = UI.upper()
    return UI


#Main program
while x != 31:
    a = x
    n = north(x)
    e = east(x)
    s = south(x)
    w = west(x)
    directions = possible_travel(n, e, s, w)
    print ("You can travel: " + directions + ".")
    while x == a:
        movement = user_input()
        x = move(x, movement, n, e, s, w)
        if x == a:
            print ("Not a valid direction!")
print ("Victory!")
