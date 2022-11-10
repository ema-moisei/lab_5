"""4) Write a function that receives a variable number of arguments and keyword arguments. The function returns a list
containing only the arguments which are dictionaries,
containing minimum 2 keys and at least one string key with minimum3 characters.
Example:
my_function({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764,
dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True})
will return: [{'abc': 4, 'def': 5}, {1: 1, 'test': True}]"""


def my_function(*args, **kwargs):
    my_list = []
    my_dic = []
    for element in args:
        if isinstance(element, set) or isinstance(element, dict):
            my_dic.append(element)
    for element in kwargs:
        my_dic.append(kwargs[element])
    for element in my_dic:
        if len(element) >= 2:
            for key in element.keys():
                if isinstance(key, str):
                    if len(key) >= 3:
                        my_list.append(element)
                        break

    return my_list


def main():

    my_list = my_function({1: 2, 3: 4, 5: 6}, {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764,
                          dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, test={1: 1, 'test': True})
    print(my_list)


if __name__ == "__main__":
    main()
