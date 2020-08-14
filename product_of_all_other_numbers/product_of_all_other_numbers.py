'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # 1 to multiply by itself
    result = 1

    # while loop thru array, mult by result
    for x in arr:
        # After mult, new result to mult to, until there are no more elem
        result *= x
        # total result will be divided by numbers in list.
    return [result / x for x in arr]

    # first arr = [1, 2, 3, 4, 5] will return a result 120.
    # 120 divided by each number in list, output of [120, 60, 40, 30, 24]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    '''arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]'''

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
