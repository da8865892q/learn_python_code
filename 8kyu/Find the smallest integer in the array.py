# Find the smallest integer in the array
# https://www.codewars.com/kata/find-the-smallest-integer-in-the-array/train/python

# My code
def find_smallest_int(arr):
    arr.sort()
    return arr[0]

# best code
# find_smallest_int = lambda arr: min(arr)
