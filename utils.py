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
    scr.addstr(50, 0)

def inferObjectFromChar(scr, char):
    obj = None
    if char == 'D':
        obj = Door
    if obj != None:
        scr.addstr(0, 0, obj)

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
    elif ch == ord(' '):
        player.interact(Door)
    
    player.move(ypos, xpos)