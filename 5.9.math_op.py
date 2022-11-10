"""9) Write a function that receives a list of pairs of integers (tuples with 2 elements) as parameter (named pairs).
The function should return a list of dictionaries for each pair (in the same order as in the input list) that contain
the following keys (as strings): sum (the value should be sum of the 2 numbers),
prod (the value should be product of the two numbers),
pow (the value should be the first number raised to the power of the second number)
Example:
f9(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)] )  will return [{'sum': 7, 'prod': 10, 'pow': 25},
{'sum': 20, 'prod': 19, 'pow': 19}, {'sum': 36, 'prod': 180, 'pow': 729000000}, {'sum': 4, 'prod': 4, 'pow': 4}] """

from math import *


def f9(pairs):
    my_list = []
    for element in pairs:
        my_sum = element[0] + element[1]
        my_prod = element[0] * element[1]
        my_pow = int(pow(element[0], element[1]))
        my_list.append({"sum": my_sum, "prod": my_prod, "pow": my_pow})
    return my_list


def main():

    pairs = [(5, 2), (19, 1), (30, 6), (2, 2)]
    my_list = f9(pairs)
    print(my_list)


if __name__ == "__main__":
    main()
