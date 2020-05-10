import random

# roll a die
def roll():
    return random.randint(1, 6)

# fills the array with rolls. any previous rolls that should be kept are passed in list
def rollDice(x):
    dice = x
    while(len(dice) < 5):
        dice.append(roll())
    return dice

# tracks succesful rolls
def trackRolls(f, i, a, b):
    s = 0
    for i in range(0, i):
        if f(a, b):
            s+=1
    return s/i

####### Combination Probablilities ########

# keeps all of the dice that equal n
def keepNumber(x, n):
    keepers = []
    for i in x:
        if i == n:
            keepers.append(i)
    return keepers

# keeps which ever number is included in n and there is the most of. preferance to bigger numbers
def keepMostN(x, n):
    best = []
    for i in n:
        ns = keepNumber(x, i)
        if len(ns) > len(best) or (len(ns) == len(best) and len(best) > 0 and i > best[0]):
            best = ns
    return best

# runs a simulation of the upper section with i spaces availabe. returns the most dice gotten
def upperSection(i):
    available = list(range(1, i+1))
    fstRoll = rollDice([])
    sndRoll = rollDice(keepMostN(fstRoll, available))
    thrdRoll = rollDice(keepMostN(sndRoll, available))
    return len(keepMostN(thrdRoll, available))

# goes for n dice with i available
def upperSectionGoFor(n, i):
    return upperSection(i) >= n

# results for upper section
print("Go for 3, 6 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 3, 6))
print("Go for 3, 5 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 3, 5))
print("Go for 3, 4 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 3, 4))
print("Go for 3, 3 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 3, 3))
print("Go for 3, 2 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 3, 2))
print("Go for 3, 1 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 3, 1))

print("Go for 4, 6 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 4, 6))
print("Go for 4, 5 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 4, 5))
print("Go for 4, 4 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 4, 4))
print("Go for 4, 3 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 4, 3))
print("Go for 4, 2 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 4, 2))
print("Go for 4, 1 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 4, 1))

print("Go for 5, 6 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 5, 6))
print("Go for 5, 5 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 5, 5))
print("Go for 5, 4 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 5, 4))
print("Go for 5, 3 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 5, 3))
print("Go for 5, 2 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 5, 2))
print("Go for 5, 1 spaces left:")
print(trackRolls(upperSectionGoFor, 10000, 5, 1))
