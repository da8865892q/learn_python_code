# Counting sheep...
# https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python

# My code
def count_sheeps(arrayOfSheeps):
  sum = 0
  for x in range(len(arrayOfSheeps)):
    if arrayOfSheeps[x] == True:
      sum += 1
  return sum

# best code
# count_sheeps = lambda arrayOfSheeps: arrayOfSheeps.count(True)
