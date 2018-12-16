# Basic Mathematical Operations
# https://www.codewars.com/kata/basic-mathematical-operations

# My code
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    else:
        return value1 / value2

# best code
# basic_op = lambda o, a, b: eval(f'{a}{o}{b}')

# basic_op = lambda o, a, b: eval("{}{}{}".format(a,o,b))

# basic_op = lambda o, a, b: {'+':a+b,'-':a-b,'*':a*b,'/':a/b}.get(o)
