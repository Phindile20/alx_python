#!/usr/bin/python3
#Write a program that imports the function def add(a, b)
if __name__ == "__main__":
        from add_0 import add
        a = 1
        b = 2
        result = add(a, b)
        print("{:d} + {:d} = {}".format(a, b, result))
