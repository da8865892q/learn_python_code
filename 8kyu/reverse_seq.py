# Reversed sequence
# https://www.codewars.com/kata/reversed-sequence

# My code
def reverse_seq(n):
    list = []
    for x in range(n,0,-1):
        list.append(x)
    return(list)

# best code
# reverse_seq = lambda n: list(range(n,0,-1))
