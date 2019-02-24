# Playing with digits
# https://www.codewars.com/kata/playing-with-digits

# My code
def dig_pow(n, p):
    sum = 0
    for x in str(n):
      sum += int(x)**p
      p += 1
    return (sum//n) if (n*(sum//n) == sum) else (-1)
        
# best code
# def dig_pow(n, p):
#     s = sum(int(d)**(p+i) for i,d in enumerate(str(n)))
#     return s/n if s%n == 0 else -1