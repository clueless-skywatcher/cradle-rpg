import curses
from utils import *

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
    def __init__(self, hp, mp, attack, defense, ypos, xpos, scr, symbol = 'P'):
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defense = defense
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
        self.scr.addstr(0, 0, "({}, {})".format(self.xpos, self.ypos))
        self.scr.addstr(self.ypos, self.xpos, self.symbol)        
        self.scr.move(ypos, xpos)
    
    def can_move(self, ypos, xpos):
        char = self.scr.inch(ypos, xpos)
        impassable = list(map(ord, ['|', '-', 'D', 'I']))
        if char in impassable:
            return False
        else:
            return True

    def getyx(self):
        return self.ypos, self.xpos

    def near(self, obj):
        y, x = self.getyx()
        if inferObjectFromChar(self.scr, self.scr.inch(y - 1, x)) == obj:
            self.scr.addstr(0, 0, "You are near a {}".format(obj))
            return True

    def interact(self, obj):
        if self.near(obj):
            self.scr.refresh()
            self.scr.addstr(1, 0, "Interacting with {}".format(obj))
        else:
            self.scr.refresh()
            self.scr.addstr(1, 0, "Nothing to interact with {}".format(obj.__class__.__name__))

    def attack(self, being):
        pass

    def recruit(self, being):
        pass

    