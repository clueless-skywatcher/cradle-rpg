import curses
from utils import *
import time
from maps import *

class BeingBattleObject:
    def __init__(self, baselv, hp, mp, attack, defense):
        self.baselv = baselv
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense

    def attack(self, player):
        pass

class Player:
    def __init__(self, hp, mp, attack, defense, ypos, xpos, scr, currmap, symbol = 'P'):
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.ypos = ypos
        self.xpos = xpos
        self.level = 1
        self.symbol = symbol
        self.scr = scr
        self.currmap = currmap
    
    def move(self, ypos, xpos):        
        if self.can_move(ypos, xpos) == False:
            return            
        self.scr.addstr(self.ypos, self.xpos, '.')
        self.xpos = xpos
        self.ypos = ypos
        self.scr.addstr(30, 0, "({}, {})".format(self.xpos, self.ypos))
        self.scr.addstr(self.ypos, self.xpos, self.symbol)        
        self.scr.move(ypos, xpos)
    
    def can_move(self, ypos, xpos):
        char = self.scr.inch(ypos, xpos)
        if char in IMPASSABLE_OBJECTS:
            return False
        else:
            return True

    def getyx(self):
        return self.ypos, self.xpos

    def interact(self):
        y, x = self.ypos, self.xpos
        top = self.scr.inch(y - 1, x)
        bottom = self.scr.inch(y + 1, x)
        left = self.scr.inch(y, x - 1)
        right = self.scr.inch(y, x + 1)
        if top == bottom == left == right == ord('.'):
            showmessage(self.scr, "There's nothing to interact with")
        elif top == ord('D'):
            yesnochoice(self.scr, "You see a door", yes = self.currmap.opendoor, no = donothing, yesargs = (y - 1, x))
        else:
            showmessage(self.scr, "There's something interesting near you")

    def attack(self, being):
        pass
 
    def recruit(self, being):
        pass

    