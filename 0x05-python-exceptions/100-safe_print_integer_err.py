#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    import traceback
    try:
        print("{:d}".format(value))
        return True
    except Exception as inst:
        sys.stderr.write("Exception: " + str(inst) + "\n")
