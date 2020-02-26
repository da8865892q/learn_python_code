# Strip Comments
# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

# My code
def solution(string,markers):
    list = string.split('\n')
    status = ""
    for i in range(len(list)):
        for j in markers:
            place = list[i].find(j)
            if place > 0:
                list[i] = list[i][:place-1]
            elif place == 0:
                list[i] = list[i][:place]
                status = "0"
    string = '\n'.join(list)
    return (string if status else string.rstrip())

# best code
# def solution(string,markers):
#     parts = string.split('\n')
#     for s in markers:
#         parts = [v.split(s)[0].rstrip() for v in parts]
#     return '\n'.join(parts)
