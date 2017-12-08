#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sumt = 0
    iterargv = iter(argv)
    next(iterargv)
    for args in iterargv:
        sumt += int(args)
    print("{}".format(sumt))
