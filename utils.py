from maps import *

def printgamemenu(scr):
    scr.addstr(8, 0, '''
    =======================================================================

    Welcome to The Cradle: A Shin Megami Tensei inspired text RPG

    What would you like to do?

    1) New Game
    2) <In development>
    3) <In development>
    
    Press 'q' to quit the game anytime.

    =======================================================================    
    ''')

def showmessage(scr, msg):
    scr.move(31, 0)
    scr.clrtoeol()
    scr.addstr(31, 0, msg)

def inferObjectFromChar(scr, char):
    obj = None
    if char == 'D':
        obj = Door
    if obj != None:
        scr.addstr(0, 0, obj)
    return obj

def handleInput(scr, ch, player):
    xpos = player.xpos
    ypos = player.ypos
    if ch == ord('w') or ch == ord('W'):
        ypos = ypos - 1
    elif ch == ord('a') or ch == ord('A'):
        xpos = xpos - 1
    elif ch == ord('s') or ch == ord('S'):
        ypos = ypos + 1
    elif ch == ord('d') or ch == ord('D'):
        xpos = xpos + 1
    elif ch == ord('f') or ch == ord('F'):
        player.interact()

    player.move(ypos, xpos)

def donothing():
    pass

def yesnochoice(scr, string, yes, no, yesargs = tuple(), noargs = tuple()):
    showmessage(scr, string)
    scr.addstr(32, 0, "Press 'y' for Yes, 'n' for No")
    while True:
        ch = scr.getch()
        if ch == ord('y') or ch == ord('Y'):
            yes(*yesargs)
            break
        elif ch == ord('n') or ch == ord('N'):
            no(*noargs)
            break
