#!/usr/bin/python3
if __name__ == "__main__":
    """ Add all arguments."""
    from sys import argv

    res = 0

    for i in argv[1:]:
        res += int(i)
    print("{:d}".format(res))
