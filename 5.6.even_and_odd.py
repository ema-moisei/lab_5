"""6) Write a function that receives a list with integers as parameter that contains an equal number of even and odd
numbers that are in no specific order. The function should return a list of pairs (tuples of 2 elements) of
numbers (Xi, Yi) such that Xi is the i-th even number in the list and Yi is the i-th odd number
Example:
my_function([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]) will return [(2, 1), (8, 3), (4, 5), (10, 7), (2, 9)]"""


def my_function(my_list):
    tuple_list = []
    odd = 0
    even = 0
    for element in my_list:
        if element % 2 == 0:
            if len(tuple_list) <= even:
                tuple_list.append([element, ])
            elif len(tuple_list) > even:
                tuple_list[even][0] = element
                tuple_list[even] = tuple(tuple_list[even])
            even += 1
        else:
            if len(tuple_list) <= odd:
                tuple_list.append(["", element])
            elif len(tuple_list) > odd:
                tuple_list[odd][1] = element
                tuple_list[odd] = tuple(tuple_list[odd])
            odd += 1

    return tuple_list


def main():

    my_list = [1, 3, 5, 2, 8, 7, 4, 10, 9, 2]
    tuple_list = my_function(my_list)
    print(tuple_list)


if __name__ == "__main__":
    main()
