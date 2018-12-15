# Correct the mistakes of the character recognition software
# https://www.codewars.com/kata/correct-the-mistakes-of-the-character-recognition-software

# My code
correct = lambda string: string.replace('0','O').replace('1','I').replace('5','S')

# best code
# correct = lambda string: string.translate(str.maketrans("501", "SOI"))
