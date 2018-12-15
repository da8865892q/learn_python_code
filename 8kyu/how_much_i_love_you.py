# I love you, a little , a lot, passionately ... not at all
# https://www.codewars.com/kata/i-love-you-a-little-a-lot-passionately-dot-dot-dot-not-at-all

# My code
def how_much_i_love_you(nb_petals):
    L = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
    return (L[(nb_petals-1)%6])

# best code
# how_much_i_love_you = lambda n: ['I love you','a little','a lot','passionately','madly','not at all'][n%6-1]
