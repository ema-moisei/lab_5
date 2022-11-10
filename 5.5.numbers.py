"""5) Write a function with one parameter which represents a list. The function will return a new list containing all
the numbers found in the given list.

Example: my_function([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]) will return [1, 5, 6, 3.0]"""


def my_function(my_list):
    nr_list = []
    for element in my_list:
        if isinstance(element, int) or isinstance(element, float):
            nr_list.append(element)

    return nr_list


def main():

    my_list = [1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]
    nr_list = my_function(my_list)
    print(nr_list)


if __name__ == "__main__":
    main()
