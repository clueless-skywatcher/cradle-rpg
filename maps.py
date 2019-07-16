import curses

import curses
import json

from utils import showmessage

IMPASSABLE_OBJECTS = list(map(ord, ['|', '-', 'I', 'D']))        

class Map:
    def __init__(self, chapter, mapno, scr):
        self.chapter = chapter
        self.mapno = mapno
        self.scr = scr
        self.doors = {}

    def render(self, ypos, xpos):
        map_ = load_map(self.chapter, self.mapno)
        meta = load_metadata(self.chapter, self.mapno)
        for i in range(len(map_)):
            self.scr.addstr(ypos + i, xpos, map_[i])
        for door in meta['doors']:
            doordata = {}
            doordata['xposd'] = door['xpos']
            doordata['yposd'] = door['ypos']
            doordata['status'] = door['status']
            doordata['to_chapter'] = door['to_chapter']
            doordata['to_mapno'] = door['to_mapno']
            self.scr.addstr(doordata['yposd'] + ypos, doordata['xposd'] + xpos, 'D')
            self.doors['({}, {})'.format(doordata['yposd'], doordata['xposd'])] = doordata
        showmessage(self.scr, str(self.doors))

    def opendoor(self, ypos, xpos):
        showmessage(self.scr, str(self.doors))
        
class Floor:
    def __init__(self, scr, ypos, xpos):
        self.ypos = ypos
        self.xpos = xpos
        self.scr = scr
            
class Door:
    def __init__(self, ypos, xpos, status, to_chapter, to_mapno, scr, currmap):
        self.ypos = ypos
        self.xpos = xpos
        self.status = status
        self.to_chapter = to_chapter
        self.to_mapno = to_mapno  
        self.scr = scr
        self.currmap = currmap  

def load_metadata(chapter, mapno):
    file = open('chapters/{}/maps/map{}.data.json'.format(chapter, mapno))
    metafile = json.load(file)
    return metafile

def load_map(chapter, mapno):
    mapfile = open('chapters/{}/maps/map{}.txt'.format(chapter, mapno))
    lines = mapfile.readlines()
    return lines

def initscreen(scr):
    curses.curs_set(2)
    curses.noecho()
    map_ = Map('prologue_tut', 1, scr)
    map_.render(5, 5)
    scr.getch()

if __name__ == "__main__":
    #curses.wrapper(initscreen)
    meta = load_metadata('prologue_tut', 1)
    print(meta['doors'])
