# Write out numbers
# https://www.codewars.com/kata/write-out-numbers

# My code
def f1(n):
    d = { 0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety' }
    return d[n]
def f2(n):
    if n % 10 == 0 or n < 20: return f1(n)
    else: return f1(n // 10 * 10) + '-' + f1(n % 10)
def f3(n):
    if n // 100 == 0: return f2(n % 100)
    if n % 100 == 0: return f1(n // 100) + ' hundred'
    else: return f1(n // 100) + ' hundred ' + f2(n % 100)
def f4(n):
    if n % 1000 == 0: return f1(n // 1000) + ' thousand'
    if n // 1000 < 1000: return f3(n // 1000) + ' thousand ' + f3(n % 1000)
    if n // 1000 < 1000000: return f4(n // 1000) + ' thousand ' + f3(n % 1000)
def number2words(n):
    if (n < 20): return f1(n)
    if (n < 100): return f2(n)
    if (n < 1000): return f3(n)
    if (n < 1000000): return f4(n)
        
# best code
# words = "zero one two three four five six seven eight nine" + \
# " ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty" + \
# " thirty forty fifty sixty seventy eighty ninety"
# words = words.split(" ")

# def number2words(n):
#     if n < 20:
#         return words[n]
#     elif n < 100:
#         return words[18 + n // 10] + ('' if n % 10 == 0 else '-' + words[n % 10])
#     elif n < 1000:
#         return number2words(n // 100) + " hundred" + (' ' + number2words(n % 100) if n % 100 > 0 else '')
#     elif n < 1000000:
#         return number2words(n // 1000) + " thousand" + (' ' + number2words(n % 1000) if n % 1000 > 0 else '')
