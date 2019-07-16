from maps import *
import pprint

def printgamemenu(scr):
    scr.addstr(8, 0, '''
    =======================================================================

    Welcome to The Cradle: A Shin Megami Tensei inspired text RPG

    What would you like to do?

    1) New Game
    2) <In development>
    3) <In development>
    
    Press 'q' to quit the game anytime.
    Press 'r' to clear the bottom message panel.
    Press 'TAB' to view your status.

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
    symbol = player.symbol
    if ch == ord('w') or ch == ord('W'):
        symbol = '^'
        ypos = ypos - 1        
    elif ch == ord('a') or ch == ord('A'):
        symbol = '<'
        xpos = xpos - 1        
    elif ch == ord('s') or ch == ord('S'):
        symbol = 'v'
        ypos = ypos + 1        
    elif ch == ord('d') or ch == ord('D'):
        symbol = '>'
        xpos = xpos + 1        
    if ch == ord('f') or ch == ord('F'):
        player.interact()
    if ch == ord('r') or ch == ord('R'):
        clearmessagepanel(scr)

    if ch == ord('\t'):
        showmessage(scr, str(player.__dict__))

    player.move(ypos, xpos, symbol)

def donothing(scr):
    clearmessagepanel(scr)

def yesnochoice(scr, string, yes, no, yesargs = tuple(), noargs = tuple()):
    showmessage(scr, string)
    scr.addstr(32, 0, "Press 'y' for Yes, 'n' for No")
    while True:
        ch = scr.getch()
        if ch == ord('y') or ch == ord('Y'):
            scr.move(32, 0)
            scr.clrtoeol()
            yes(*yesargs)
            break
        elif ch == ord('n') or ch == ord('N'):
            scr.move(32, 0)
            scr.clrtoeol()
            no(*noargs)
            break

def clearmessagepanel(scr):
    scr.move(31, 0)
    scr.clrtobot()

def process_map_meta(meta):
    orig_meta = meta
    width = meta['width'] - 1
    height = meta['height'] - 1
    doors = meta['doors']
    for door in doors:
        if door['xpos'] == 'left':
            door['xpos'] = 0
        elif door['xpos'] == 'right':
            door['xpos'] = width

        if door['ypos'] == 'top':
            door['ypos'] = 0
        elif door['ypos'] == 'bottom':
            door['ypos'] = height
    return meta, orig_meta

if __name__ == "__main__":
    pprint.pprint(process_map_meta({
    "width" : 57,
    "height" : 6,
    "doors" : [
        {
            "xpos" : 18,
            "ypos" : "bottom",
            "status" : "not-locked",
            "to_chapter" : "prologue_tut",
            "to_mapno" : 1,
            "spawn_next_xpos" : 19,
            "spawn_next_ypos" : 0
        },
        {
            "xpos" : "right",
            "ypos" : 3,
            "status" : "locked",
            "to_chapter" : "prologue_tut",
            "to_mapno" : 4,
            "spawn_next_xpos" : 0,
            "spawn_next_ypos" : 1
        }
    ]
})[0])