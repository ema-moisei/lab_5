"""3) Using functions, anonymous functions, list comprehensions and filter, implement three methods to generate a list
with all the vowels in a given string.

For the string "Programming in Python is fun" the list returned will be ['o', 'a', 'i', 'i', 'o', 'i', 'u']."""


def my_function(my_string):
    my_list = []
    for element in my_string:
        if element in ['o', 'a', 'i', 'i', 'o', 'i', 'u']:
            my_list.append(element)

    return my_list


def ano_func(my_string):
    vowels = ['o', 'a', 'i', 'i', 'o', 'i', 'u']
    my_list = list(filter(lambda x: x in vowels, my_string))

    return my_list


def list_compr(my_string):
    my_list = [x for x in my_string if x in ['o', 'a', 'i', 'i', 'o', 'i', 'u']]

    return my_list


def main():

    my_string = "Programming in Python is fun"

    function_list = my_function(my_string)
    print("Vowels obtained by a function: ", function_list)

    ano_function = ano_func(my_string)
    print("Vowels obtained by an anonymous function: ", ano_function)

    compr_list = list_compr(my_string)
    print("Vowels obtained by list comprehensions and filter: ", compr_list)


if __name__ == "__main__":
    main()
