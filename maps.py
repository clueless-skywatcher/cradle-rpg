import curses

import curses
import json

class Map:
    def __init__(self, chapter, mapno, scr):
        self.chapter = chapter
        self.mapno = mapno
        self.scr = scr
        self.doors = []

    def render(self, ypos, xpos):
        map_ = load_map(self.chapter, self.mapno)
        meta = load_metadata(self.chapter, self.mapno)
        for i in range(len(map_)):
            self.scr.addstr(ypos + i, xpos, map_[i])
        for door in meta['doors']:
            xposd = door['xpos']
            yposd = door['ypos']
            status = door['status']
            to_chapter = door['to_chapter']
            to_mapno = door['to_mapno']
            self.doors.append(Door(yposd, xposd, status, to_chapter, to_mapno))
            self.scr.addstr(yposd + ypos, xposd + xpos, 'D')
            
class Door:
    def __init__(self, ypos, xpos, status, to_chapter, to_mapno):
        self.ypos = ypos
        self.xpos = xpos
        self.status = status
        self.to_chapter = to_chapter
        self.to_mapno = to_mapno      

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
