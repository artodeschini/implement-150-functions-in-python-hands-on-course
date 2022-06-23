"""""
<Define a function called is_nested()
 that checks if the passed list is nested and consists of elements of type list (a list of lists).
 
print(is_nested([[3,4]]))
[OUT]:True
print(is_nested([[3,4],4]))
[OUT]:False
print(is_nested([[3,4],[2,1]]))
[OUT]:True
print(is_nested([[3,4],0,[2,1]]))
[OUT]:False
 
"""""


def is_nested(array):
    if len(array) == 0:
        return False
    return all(isinstance(row, list) for row in array)


print(is_nested([[3, 4]]))              # True
print(is_nested([[3, 4], 4]))           # False
print(is_nested([[3, 4], [2, 1]]))      # True
print(is_nested([[3, 4], 0, [2,1]]))    # False
