# https://www.codewars.com/kata/removing-elements/train/python
# Removing Elements

# My code
def remove_every_other(my_list):
    for x in range(1,len(my_list)):
        my_list.pop(1,len(my_list))
    return my_list
