#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    iterargv = iter(argv)
    next(iterargv)
    if len(argv) == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(argv) - 1))
        x = 1
        for args in iterargv:
            print("{}: {}".format(x, args))
            x += 1
