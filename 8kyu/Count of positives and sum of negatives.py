# https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives/train/python
# Count of positives / sum of negatives

# My code
def count_positives_sum_negatives(arr):
    a = b = 0
    if arr == []:
        return [] 
    else:
        for x in range(len(arr)):
            if arr[x] > 0:
                a += 1
            else:
                b += arr[x]
        return [a,b]

# best code
# def count_positives_sum_negatives(arr):
#     return [sum(n > 0 for n in arr), sum(n for n in arr if n < 0)] if arr else []