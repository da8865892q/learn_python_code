# Champernowne's Championship
# https://www.codewars.com/kata/champernownes-championship

# My code
def f1(n):
    p = 10
    d = 1
    while d != 0:
        a = 1
        for x in range(d):
            a *= 10
        b = a*10-1
        s = (b-a+1)*(d+1)
        p += s
        if p >= n:
            d == 0
            return d+1, b//10, p-s
        d += 1
def f2(a, E, N):
    if E == 0:
        return N %10
    else:
        for x in range(a-E+1):
            p = N
            N //= 10
            A = p - N * 10
        return A
def champernowneDigit(n):
    if type(n) == int and type(n) != bool and n>0:
        if n <= 10 :
            return n-1
        else:
            a, b, c = f1(n)
            N=0
            if (n-c)%a == 0:
                N = b+(n-c)//a
            else:
                N = b+(n-c)//a+1
            E = (n-c)%a
            return f2(a, E, N)
    else:
        return float("NaN")

# best code
# DIGIT_CNTS = [1] + [(10**i - 10**(i-1)) * i for i in range(1, 20)]
# def champernowneDigit(n):
#     if not isinstance(n, int) or n is True or n <= 0:
#         return float('nan')
#     n -= 1
#     for digits, cnt in enumerate(DIGIT_CNTS):
#         if n < cnt:
#             break
#         n -= cnt
#     start = int(10 ** (digits-1))
#     q, r = divmod(n, digits) if digits > 1 else (n, 0)
#     return int(str(start + q)[r])
