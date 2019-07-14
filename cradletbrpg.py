import curses
from curses import textpad
from maps import *
  
class Player:
    def __init__(self, hp, mp, ypos, xpos, scr, symbol = 'P'):
        self.hp = hp
        self.mp = mp
        self.ypos = ypos
        self.xpos = xpos
        self.level = 1
        self.symbol = symbol
        self.scr = scr
    
    def move(self, ypos, xpos):        
        if self.can_move(ypos, xpos) == False:
            return            
        self.scr.addstr(self.ypos, self.xpos, '.')
        self.xpos = xpos
        self.ypos = ypos
        self.scr.addstr(self.ypos, self.xpos, self.symbol)
        self.scr.move(ypos, xpos)
    
    def can_move(self, ypos, xpos):
        char = self.scr.inch(ypos, xpos)
        impassable = list(map(ord, ['|', '-', '!']))
        if char in impassable:
            return False
        else:
            return True
    
def initgame(scr):
    curses.curs_set(0)
    curses.noecho()    
    map_ = Map('prologue_tut', 1, scr = scr)
    map_.render(5, 5)
    player = Player(91, 60, 13, 13, scr = scr)
    player.move(player.ypos, player.xpos)    
    while True:
        ch = scr.getch()  
        if ch == ord('q') or ch == ord('Q'):
            break      
        if ch == ord('r') or ch == ord('R'):
            scr.erase()
        handleInput(scr, ch, player)
        
def handleInput(scr, ch, player: Player):
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
    
    player.move(ypos, xpos)

curses.wrapper(initgame)

