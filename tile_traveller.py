# Starting point er [1,1]
x = 11
# Skilgreina possible moves
def north(x):
    if x % 10 == 3 or x == 22 or x == 31:
        return False
    return True
def east(x):
    if x  == 12 or x == 13 or x == 23:
        return True
    return False
def south(x):
    if x % 10 == 1 or x == 23:
        return False
    return True
def west(x):
    if x  == 22 or x == 23 or x == 33:
        return True
    return False
# Possible travel options prentast eftir hvert move
def possible_travel(x):
    direction = ""
    while direction == "":
        if north(x):
            direction += "(N)orth"
        elif east(x):
            direction += "(E)ast"
        elif south(x):
            direction += "(S)outh"
        elif west(x):
            direction += "(W)est"
    if east(x) and direction != "(E)ast":
        direction += " or (E)ast"
    if south(x) and direction != "(S)outh":
        direction += " or (S)outh"
    if west(x) and direction != "(W)est":
        direction += " or (W)est"
    return direction
# Move player og input(move path)
def move(x, string):
    if string == "N":
        if north(x):
            x += 1
    if string == "E":
        if east(x):
            x += 10
    if string == "S":
        if south(x):
            x -= 1
    if string == "W":
        if west(x):
            x -= 10
# Við invalid direction prentast "Not a valid direction!" og possible travel options
def user_input():
    UI = input("Direction: ")
    UI = UI.upper()
    return UI

# Main program
#print("You can travel: " direction ".")
# Victory location [3,1]
#BLABLA