import curses
import json

from utils import showmessage, process_map_meta

RENDER_XPOS = 5
RENDER_YPOS = 5
IMPASSABLE_OBJECTS = list(map(ord, ['|', '-', 'I', 'D']))        

class Map:
    def __init__(self, chapter, mapno, player, scr, ypos = RENDER_YPOS, xpos = RENDER_XPOS):
        self.chapter = chapter
        self.mapno = mapno
        self.scr = scr
        self.doors = {}
        self.ypos = ypos
        self.xpos = xpos
        self.meta = {}
        self.player = player

    def render(self):
        self.scr.clear()
        map_ = load_map(self.chapter, self.mapno)
        meta = load_metadata(self.chapter, self.mapno)
        
        self.meta, orig_meta = process_map_meta(meta)            
        for i in range(len(map_)):
            self.scr.addstr(self.ypos + i, self.xpos, map_[i])
        
        self.renderplayer(self.player.ypos, self.player.ypos)        
        self.renderdoors()
        self.renderitems()
        self.player.currmap = self
        
    def renderplayer(self, ypos, xpos):
        self.player.place(ypos, xpos, self.player.symbol)        
    
    def renderdoors(self):
        for door in self.meta['doors']:
            doordata = {}
            doordata['xposd'] = door['xpos']
            doordata['yposd'] = door['ypos']
            doordata['status'] = door['status']
            doordata['to_chapter'] = door['to_chapter']
            doordata['to_mapno'] = door['to_mapno']
            doordata['spawn_next_xpos'] = door['spawn_next_xpos']
            doordata['spawn_next_ypos'] = door['spawn_next_ypos']
            self.scr.addstr(doordata['yposd'] + self.ypos, doordata['xposd'] + self.xpos, 'D')
            self.doors['({}, {})'.format(doordata['yposd'], doordata['xposd'])] = doordata

    def renderitems(self):
        pass
        
    def opendoor(self, ypos, xpos):
        door = self.doors['({}, {})'.format(ypos - RENDER_YPOS, xpos - RENDER_XPOS)]
        status = door['status']
        if status == 'locked':
            showmessage(self.scr, "This door is locked.")
            return
        else:
            self.mapno = door['to_mapno']
            axpos = door['spawn_next_xpos']
            aypos = door['spawn_next_ypos']
            self.player.move(aypos, axpos, self.player.symbol)
            self.render()
        
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
