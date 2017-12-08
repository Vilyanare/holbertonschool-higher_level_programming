#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dirlist = dir(hidden_4)
    for x in dirlist:
        if x[:2] != "__":
            print("{}".format(x))
