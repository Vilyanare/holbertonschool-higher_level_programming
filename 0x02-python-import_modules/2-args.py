#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    iterargv = iter(argv)
    next(iterargv)
    y = len(argv)
    if y == 1:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(y - 1, '' if y == 2 else 's'))
        x = 1
        for args in iterargv:
            print("{}: {}".format(x, args))
            x += 1
