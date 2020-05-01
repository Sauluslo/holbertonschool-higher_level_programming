#!/usr/bin/python3
if __name__ == "__main__":
    list1 = "arguments."
    list2 = "arguments:"
    list3 = "argument:"
    from sys import argv
    argc = len(argv) - 1
    if argc == 1:
        print("{:d} {}".format(argc, list3))
    else:
        if argc == 0:
            print("{:d} {}".format(argc, list1))
        else:
            print("{:d} {}".format(argc, list2))
    count = 0
    for argument in argv:
        if count > 0:
             print("{:d}: {}".format(count, argument))
        count += 1
