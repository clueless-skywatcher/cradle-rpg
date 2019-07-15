import curses
from curses import textpad
from maps import *
from utils import *
from units import *
    
def initmenu(scr):
    scr.clear()
    curses.curs_set(0)
    curses.noecho()
    printgamemenu(scr)
    while True:
        ch = scr.getch()
        if ch == ord('Q') or ch == ord('q'):
            break
        if ch == ord('1') or ch == ord('1'):
            curses.wrapper(onnewgame)
            break

def onnewgame(scr):
    scr.clear()
    scr.addstr(8, 0, '''
    ======================================================================================

    You wake up within a white room. The white colour is not something like a white paint, 
    it seems more like a holy light or something, but you cannot figure anything out. 
    You don't probably remember who you are or what you were up to, and you feel as if 
    your head is lighter than a feather. You look around to scan the surroundings, 
    without any clue of how you ended up here in the first place. At a distance you
    can see prison cell bars, and you figure out that you are locked in a prison. 

    (Press 'c' to continue)

    ======================================================================================
    ''')
    while True:
        ch = scr.getch()
        if ch == ord('Q') or ch == ord('q'):
            break
        if ch == ord('C') or ch == ord('c'):
            curses.wrapper(initgame)
            break
    
def initgame(scr):
    scr.clear()
    curses.curs_set(0)
    curses.noecho()    
    map_ = Map('prologue_tut', 1, scr = scr)
    map_.render(5, 5)
    player = Player(91, 60, 54, 54, 13, 13, scr = scr)
    player.move(player.ypos, player.xpos)    
    while True:
        ch = scr.getch()  
        if ch == ord('q') or ch == ord('Q'):
            break      
        if ch == ord('m') or ch == ord('M'):
            curses.wrapper(initmenu)
            break
        handleInput(scr, ch, player)
        


curses.wrapper(initmenu)

