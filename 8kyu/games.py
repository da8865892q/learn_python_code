# Total amount of points
# https://www.codewars.com/kata/total-amount-of-points

# My code
def points(games):
    n = 0
    for x in range (len(games)):
        if str(games[x][0]) > str(games[x][2]):
            n += 3
        if str(games[x][0]) == str(games[x][2]):
            n += 1
    return n

# best code
# points = lambda g: sum((x==y)+(x>y)*3 for x,_,y in g)

