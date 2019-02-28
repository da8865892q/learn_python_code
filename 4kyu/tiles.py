# Mahjong - #1 Pure Hand
# https://www.codewars.com/kata/mahjong-number-1-pure-hand

# My code
def function(L):
    if len(L) == 0:
        return True
    elif L[0] == L[1] == L[2]:
        L.remove(L[2])
        L.remove(L[1])
        L.remove(L[0])
    elif L[0]+1 in L and L[0]+2 in L:
        L.remove(L[0]+2)
        L.remove(L[0]+1)
        L.remove(L[0])
    else:
        return False
def check(hand,eye):
    for x in range (13):
        L = hand.copy()
        L.append(eye)
        L.sort()
        if L.count(eye) > 4:
            break
        if L[x] == L[x+1]:
            L.remove(L[x+1])
            L.remove(L[x])
            i = 5
            while i > 0:
                resp = function(L)
                if resp == True:
                    return eye
                i -= 1
def solution(test):
    ans = str()
    for item in range(1,10):
        test = [int(item) for item in test]
        ans = ans + str(check(test,item))
    return ans.replace('None','')

# best code
# from collections import Counter
# class SubCounter(Counter):
#     def __le__(self, other):
#         return all(value <= other[key] for key, value in self.items())
# MELDS = [SubCounter({str(n): 3}) for n in range(1, 10)]
# MELDS.extend([SubCounter([str(n), str(n+1), str(n+2)]) for n in range(1, 8)])
# def solution(tiles):
#     def remove(cnt):
#         if sum(cnt.values()) == 4: # Meld
#             for k, v in cnt.items():
#                 if v >= 2:
#                     p = SubCounter(cnt)
#                     p[k] -= 2
#                     for m in MELDS:
#                         if p <= m:
#                             winning.update((m - p).keys())
#         if sum(cnt.values()) == 1: # Pair
#             winning.update(cnt.keys())
#         else:
#             for m in MELDS:
#                 if m <= cnt:
#                     remove(cnt - m)
#     winning, cnt = set(), SubCounter(tiles)
#     forbidden = {k for k, v in cnt.items() if v >= 4}
#     return remove(cnt) or ''.join(sorted(winning - forbidden))