"""
Define a function called is_all_equal()

that checks if the passed list consists of the same elements.
Example:
    [IN]:is_all_equal([4,5,7])
     [OUT]:False
     [IN]:is_all_ equal([4,4,4])
     [OUT]:True

     [IN]:is_all_equal(['Q','Q','Q'])
     [OUT]:True
"""


def is_all_equal(iterator):
    return len(set(iterator)) <= 1


print(is_all_equal([4, 5, 7]))          # False
print(is_all_equal([4, 4, 4]))          # True
print(is_all_equal(['Q', 'Q', 'Q']))    # False
