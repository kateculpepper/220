

"""
searching
sorting
Recrsion



"""

def linear_search(search_list, target):
    pass

def binary_search(search_list, target):
    left_index = 0
    right_index = len(search_list)-1
    while left_index <= right_index:
        middle_index = (right_index + left_index) // 2
        middle_value = search_list[middle_index]
        if middle_value == target:
            return middle_index
        elif middle_value < target:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
    return -1

