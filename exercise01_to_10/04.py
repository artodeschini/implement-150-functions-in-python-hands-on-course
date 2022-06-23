"""
Define a function called swap_elements()
that takes a list as argument and replaces the first and last elements of that list.
Example:
         [IN]:swap_elements([4,5,6,7])
         [OUT]:[7,5,6,4]
         [IN]:swap_elements([4,5,6,7,1])
         [OUT]:[1,5,6,7,4]
"""


def swap_elements(array):
    temp = []
    for i in array:
        temp.append(i)
    temp[0] = array[len(array) - 1]
    temp[len(array) - 1] = array[0]

    return temp


print(swap_elements([4, 5, 6, 7]))
print(swap_elements([4, 5, 6, 7, 1]))
print(swap_elements([4, 5]))

"""Solution I:

def swap_elements(new_list):
    temp = new_list[0]
    new_list[0] = new_list[-1]
    new_list[-1] = temp
    return new_list


Solution II:

def swap_elements(new_list):
    (new_list[0], new_list[-1]) = (new_list[-1], new_list[0])
    return new_list
"""
