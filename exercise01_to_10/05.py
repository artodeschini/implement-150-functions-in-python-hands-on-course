"""
Define a function called swap_elements()
that takes a list and two indices as arguments, and replaces the elements at the indicated indices.
Example:
         [IN]:swap_elements([4,5,6,7,1],1,2)
         [OUT]:[4,6,5,7,1]
         [IN]:swap_elements(['A','B','C','D','E'],4,2)
         [OUT]:['A','B','E','D','c']2
"""


def swap_elements(array, p1, p2):
    temp = []
    for i in array:
        temp.append(i)

    temp[p1] = array[p2]
    temp[p2] = array[p1]

    return temp


print(swap_elements([4, 5, 6, 7, 1], 1, 2))
print(swap_elements(['A', 'B', 'C', 'D', 'E'], 4, 2))
print(swap_elements([2.1, 5.2, 7.1, 2.6, 2.1], 3, 2))