# Filter out the geese
# https://www.codewars.com/kata/filter-out-the-geese

# My code
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    for i in range (len(geese)):
        if geese[i] in birds:
            birds.remove(geese[i])
    return  birds

# best code
# geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# def goose_filter(birds):
#     return [b for b in birds if b not in geese]