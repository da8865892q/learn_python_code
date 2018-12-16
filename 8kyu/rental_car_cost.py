# Transportation on vacation
# https://www.codewars.com/kata/transportation-on-vacation

# My code
def rental_car_cost(d):
    if d < 3:
        return 40*d
    elif 3<=d<7:
        return 40*d-20
    else:
        return 40*d-50
        
# best code
# rental_car_cost = lambda d: return d*40 - (d>2)*20 - (d>6)*30