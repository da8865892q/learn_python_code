# Mean Square Error
# https://www.codewars.com/kata/51edd51599a189fe7f000015

# My code
def solution(array_a, array_b):
    l = len(array_a)
    sum = 0
    for i in range (l):
        sum = sum+(array_a[i]-array_b[i])*(array_a[i]-array_b[i])
    return sum/l

# best code
# def solution(a, b):
#     return sum((x - y)**2 for x, y in zip(a, b)) / len(a)