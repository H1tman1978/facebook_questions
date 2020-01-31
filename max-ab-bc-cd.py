"""
FILE: max-ab-bd-cd.py
AUTHOR: Anthony Rolfe
DATE: 31 January 2020

DESCRIPTION: Given a target sum, this program will find that max value of ab + bc + cd, where a+b+c+d=target sum and
a, b, c, d are unique integers.

Special thanks to Manavalan Michael for this coding challenge and to Geeks for Geeks for their four elements code which
I have expanded upon. See https://www.geeksforgeeks.org/find-four-numbers-with-sum-equal-to-given-sum/ for their original
function.
"""


# Import required modules
from itertools import permutations
from operator import add, mul
from functools import reduce

# Set target sum (i.e what does a + b + c + d =)
TARGET_SUM = 63

def find_four_elements(numberList, targetSum):
    """
    This function takes a list of numbers and a target sum and finds all the numbers in that list that
    add up to the target sum.
    :param numberList:     A list of ints.
    :param targetSum:      An int
    :return: targetList    A list of target numbers
    """
    # Determine length of numberList
    length = len(numberList)

    # Setup list to return
    targetList = []
    # Fix the first element and find other three
    for i in range(0, length - 3):
        # Fix the second element and find the other two
        for j in range(i + 1, length - 2):
            # Fix the third element and find the fourth
            for k in range(j + 1, length - 1):
                # Find the fourth
                for l in range(k + 1, length):
                    if numberList[i] + numberList[j] + numberList[k] + numberList[l] == targetSum:
                        targetList.append([numberList[i], numberList[j], numberList[k], numberList[l]])

    # Return targetList
    return targetList

def find_max_ab_bc_cd(list_of_sumsLists):
    """
    This function iterates over a list of lists which contain elements [a, b, c, d] that add up to TARGET_SUM and
    returns the maximum value of ab+bc+cd of the elements inside each list.
    :param list_of_sumsLists: This should be the list that is returned by find_four_elements()
    :return: max_value: an int which is the greatest value of ab+bc+cd
    """
    max_value = 0
    for item in list_of_sumsLists:
        result = list(permutations(item, 2))
        value = reduce(add, [mul(*i) for i in result[::4]])
        if value > max_value:
            max_value = value
    return max_value


# Main Program Loop
if __name__ == '__main__':
    # Create a list of all integers from 1 to TARGET_SUM
    number_list = [x for x in range(1, TARGET_SUM + 1)]

    # Find lists of a, b, c, d who's sum equals TARGET_SUM
    sumElements = find_four_elements(number_list, TARGET_SUM)

    # Find and print max ab + bc+ cd
    max_ab_bc_cd = find_max_ab_bc_cd(sumElements)
    print(max_ab_bc_cd)
