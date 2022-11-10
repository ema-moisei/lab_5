"""2) Create a function and an anonymous function that receive a variable number of arguments.
Both will return the sum of the values of the keyword arguments.
Example:
For the call my_function(1, 2, c=3, d=4) the returned value will be 7."""

from functools import reduce


def my_function(*args, **kwargs):
    result = reduce(lambda my_sum, up_val: my_sum+up_val, kwargs.values())
    return result


def main():

    result = my_function(1, 2, c=3, d=4)
    print(result)


if __name__ == "__main__":
    main()
