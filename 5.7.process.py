"""7) Write a function called process that receives a variable number of keyword arguments
The function generates the first 1000 numbers of the Fibonacci sequence and then processes them in the following way:
If the function receives a parameter called filters, this will be a list of predicates (function receiving an argument
and returning True/False) and will retain from the generated numbers only those for which the predicates are True.
If the function receives a parameter called limit, it will return only that amount of numbers from the sequence.
If the function receives a parameter called offset, it will skip that number of entries from the beginning of the
result list.
The function will return the processed numbers.
Example:
def sum_digits(x):
    return sum(map(int, str(x)))
process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20], limit=2,offset=2)
    returns [34, 144]
Explanation:
# Fibonacci sequence will be: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...
# Valid numbers are: 2, 8, 34, 144, 610, 2584, 10946, 832040
# After offset: 34, 144, 610, 2584, 10946, 832040
# After limit: 34, 144
"""


def fibonacci(number):
    """Calculates each term of the Fibonacci series and assigns the values one by one to a string"""
    F0 = 0
    if number == 1:
        fibonacci_string = 0
    elif number == 2:
        fibonacci_string = [0, 1]
    else:
        Fn = 1
        fibonacci_string = [0, 1]
        while number > 2:
            Fn, F0 = Fn + F0, Fn
            number -= 1
            fibonacci_string.append(Fn)
    return fibonacci_string


def sum_digits(x):
    return sum(map(int, str(x)))


def process(filters=None, limit=2, offset=2):
    fi = fibonacci(1000)

    if filters is None:
        filters = [lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20]
        for func in filters:
            fi = list(filter(func, fi))

    fi = fi[offset:]
    fi = fi[:limit]

    return fi


def main():

    fi = process(None, 2, 2)
    print(fi)


if __name__ == "__main__":
    main()
