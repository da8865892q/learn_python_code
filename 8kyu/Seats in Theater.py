# Simple Fun #1: Seats in Theater
# https://www.codewars.com/kata/simple-fun-number-1-seats-in-theater/train/python

# My code
def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_cols - col + 1) * (tot_rows - row)

# best code
# seats_in_theater = lambda C, R, c, r: (C-c+1)*(R-r)