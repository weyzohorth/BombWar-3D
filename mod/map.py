from __init__ import G
from mur import Mur
from joueur import Joueur

class Map:
    def __init__(__, map="map/default.bw3d"):
        mapfile = open(map,  "rb")
        opt = mapfile.readline().split(' ')
        __.map, __.floor = [], []
        if opt[0] == '1':
            __.fill_list(mapfile,  __.floor)
        __.fill_list(mapfile, __.map)
    
    def fill_list(__, mapfile, maplist):
        string = mapfile.readline().replace('\n', '\r').replace('\r', '')
        while string:
            string = string.split(' ')
            if len(string) == 1:
                string = list(string[0])
            maplist.append(string)
            string = mapfile.readline().replace('\n', '\r').replace('\r', '')
    
    def create(__):
        w = int(G.xmax/(G.R*2)) + 1
        h = int(G.ymax/(G.R*2)) + 1
        __.place_wall(__.floor, -G.bloc_size)
        __.place_wall(__.map, 0)
    
    def place_wall(__, liste, z):
        for y in range(len(liste)):
            for x in range(len(liste[0])):
                if '1' <= liste[y][x] <= '9':
                    Mur(x * G.bloc_size + G.bloc_size / 2,  y * G.bloc_size + G.bloc_size / 2, z + G.bloc_size / 2, int(liste[y][x]) - 1)
                elif 'a' <= liste[y][x] <= 'd':
                    Joueur(x * G.bloc_size + G.bloc_size / 2, y * G.bloc_size + G.bloc_size / 2)
            Mur(-G.bloc_size + G.bloc_size / 2,  y * G.bloc_size + G.bloc_size / 2, z + G.bloc_size / 2, 2)
            Mur((x + 1) * G.bloc_size + G.bloc_size / 2,  y * G.bloc_size + G.bloc_size / 2, z + G.bloc_size / 2, 2)
        for x in range(len(liste[0])):
            Mur(x * G.bloc_size + G.bloc_size / 2,  -G.bloc_size + G.bloc_size / 2, z + G.bloc_size / 2, 2)
            Mur(x * G.bloc_size + G.bloc_size / 2,  (y + 1) * G.bloc_size + G.bloc_size / 2, z + G.bloc_size / 2, 2)

if __name__ == "__main__":
    print Map("../map/default.bw3d").map
