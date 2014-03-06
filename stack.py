#/usr/bin/python

sp = 0
bp = 0

stack = [0] * 10

def push(data):
    global sp
    try:
        stack[sp] = data
        sp += 1
        return True
    except IndexError:
        return False

def pop():
    global sp
    try:
        sp -= 1
        return stack[sp]
    except IndexError:
        return False

while True:
    porp = input("Push or pop? ")
    if porp == "push":
        item = input("Enter data to push: ")
        if not push(item):
            print("Stack overflow!")
    elif porp == "pop":
        if not pop():
            print("Stack empty!")
        else:
            print(pop())
    else:
        print("Invalid command")
