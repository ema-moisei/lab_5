"""1) a) Write a module named utils.py that contains one function called process_item.
The function will have one parameter, x, and will return the least prime number greater than x. 
When run, the module will request an input from the user, convert it to a number and it will display the output of the 
process_item function."""
from math import *


def process_item(x):
    if x.isalpha():
        x = ord(x)
    x = int(x)
    prime = 0
    rad = int(sqrt(x))
    nr = x
    while not prime:
        nr += 1
        is_prime = True
        if nr % 2 == 0:
            continue
        for i in range(3, rad + 2, 2):
            if nr % i == 0:
                is_prime = False
        if is_prime:
            prime = nr
            break
    return prime


def main():

    x = input("Give an input: ")
    x = process_item(x)
    print(x)


if __name__ == "__main__":
    main()
