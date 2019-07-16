def yesnochoice(yes, no, yesargs = tuple(), noargs = tuple()):
    while True:
        ch = str(input())
        if ch == 'y':
            yes(*yesargs)
            break
        if ch == 'n':
            no(*noargs)
            break
    
def add(a, b):
    print(a + b)

def sub(a, b):
    print(a - b)

yesnochoice(add, sub, (2, 3), (2, 5))