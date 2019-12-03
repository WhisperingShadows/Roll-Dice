import random
from pprint import pprint
DEBUG = False

def roll(d):
    if d < 1:
        print("Input values must be greater than or equal to 1")
        return None
    return random.randint(1,d)


def main():
    while True:
        val = input().strip()
        if len(val.split("d")) == 2:
            try:
                val = int(val.split("d")[1])
                out = roll(val)
                if out:
                    print(out)
            except:
                print("Expected input in form dx where x is an integer greater than or equal to one")
        else:
            if DEBUG:
                print("============")
                print(val.split("d"))
                print(len(val.split("d")))
                print(val.split("d")[1])
                print(type(val.split("d")[1]))
                print("============")


def test():
    log = {}
    logRange = 100
    rollRange = 20

    for i in range(logRange):
        val = roll(rollRange)
        try:
            log[val] += 1
        except:
            log[val] = 1

    sortedLog = {}
    for i in range(rollRange):
        sortedLog[i+1] = log[i+1]

    pprint(log)


mode = input("T: test, M: mode")
if mode.lower == "t":
    test()
elif mode.lower == "m":
    main()
else:
    print("Main it is")
    main()
    
