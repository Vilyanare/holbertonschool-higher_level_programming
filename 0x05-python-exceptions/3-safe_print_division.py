#!/usr/bin/python3
def safe_print_division(a, b):
    quotient = None
    try:
        quotient = a / b
    except:
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
        return quotient
