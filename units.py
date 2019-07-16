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
    def __init__(self, hp, mp, attack, defense, ypos, xpos, scr, symbol = '^'):
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
        self.ypos = ypos
        self.xpos = xpos
        self.level = 1
        self.symbol = symbol
        self.scr = scr
        self.currmap = None
    
    def move(self, ypos, xpos, symbol):
        self.symbol = symbol
        if self.can_move(ypos, xpos) == False:
            self.scr.addstr(self.ypos, self.xpos, self.symbol)               
            return
        self.scr.addstr(self.ypos, self.xpos, '.')
        self.xpos = xpos
        self.ypos = ypos
        self.scr.move(30, 0)
        self.scr.clrtoeol()
        self.scr.addstr(30, 0, "({}, {})".format(self.xpos, self.ypos))
        self.scr.addstr(self.ypos, self.xpos, self.symbol)        
        self.scr.move(ypos, xpos)

    def place(self, ypos, xpos, symbol):
        self.scr.addstr(ypos, xpos, symbol)
        self.ypos = ypos
        self.xpos = xpos
    
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
        top, t = self.scr.inch(y - 1, x), (y - 1, x)
        bottom, b = self.scr.inch(y + 1, x), (y + 1, x)
        left, l = self.scr.inch(y, x - 1), (y, x - 1)
        right, r = self.scr.inch(y, x + 1), (y, x + 1)
        if top == bottom == left == right == ord('.'):
            showmessage(self.scr, "There's nothing to interact with")
        elif top == ord('D') and self.symbol == '^':
            yesnochoice(self.scr, "You see a door. Open it?", yes = self.currmap.opendoor, no = donothing, yesargs = t, noargs = (self.scr, ))
        elif bottom == ord('D') and self.symbol == 'v':
            yesnochoice(self.scr, "You see a door. Open it?", yes = self.currmap.opendoor, no = donothing, yesargs = b, noargs = (self.scr, ))
        elif left == ord('D') and self.symbol == '<':
            yesnochoice(self.scr, "You see a door. Open it?", yes = self.currmap.opendoor, no = donothing, yesargs = l, noargs = (self.scr, ))
        elif right == ord('D') and self.symbol == '>':
            yesnochoice(self.scr, "You see a door. Open it?", yes = self.currmap.opendoor, no = donothing, yesargs = r, noargs = (self.scr, ))
        elif top == bottom == ord('-') or left == right == ord('|'):
            showmessage(self.scr, "Nothing to interact on the walls")
        elif top == ord('i') or bottom == ord('i') or left == ord('i') or right == ord('i'):
            yesnochoice(self.scr, "You see an item nearby. Pick it up?", yes = donothing, no = donothing)

    def attack(self, being):
        pass
 
    def recruit(self, being):
        pass
            

    