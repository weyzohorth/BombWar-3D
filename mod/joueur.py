from __init__ import *
from bombe import Bombe
from mod_math import *
from camera import Camera_FreeFly

class Joueur:
    def __init__(__,x,y,max_bomb=2,max_size=2,max_size_milieu=1,telecom=0,nucleary=0):
        __.image = pygame.image.load('datas/img/joueurs/joueur'+str(len(G.JOUEURS))+'.gif').convert()
        __.droite, __.haut, __.gauche, __.bas, __.activ_bomb , __.lache_bomb = [
                                                                                        (100, 122, 113, 115, 101, 97),
                                                                                        (275, 273, 276, 274, 305, 303),
                                                                                        (109, 111, 107, 108, 112, 105),
                                                                                        (259, 261, 257, 258, 262, 260)
                                                                                        ][len(G.JOUEURS)]
    
        G.JOUEURS.append(__)
        if len(G.JOUEURS) == 1:
            __.cam = Camera_FreeFly((x, y, 0), speed=1)
            __.cam.draw()
        else:
            __.cam = None
        __.x, __.y = x, y
        __.r = 16
        __.max_bomb, __.max_size, __.max_size_milieu, __.telecom, __.nucleary =\
                       max_bomb, max_size, max_size_milieu, telecom, nucleary
        __.pose = 0
        __.new_bomb = None
        __.bomb_tel = []
        __.mort = False
        __.direction, __.bomb, __.BOOM = 0, False, False
        __.sprite = __.image
        __.dir = 0
    
        G.game.blit(__.sprite, (x, y))

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def direction_set(__,x):
        if not __.mort:
            if __.direction != x > 0:
                __.dir = x - 1
                __.sprite = pygame.transform.rotate(__.image, __.dir * 90)
            __.direction = x
    
    def draw(__):
        if __.cam:
            __.cam.draw()
    
    def event(__, event):
        if __.cam:
            __.cam.event(event)
        #__.draw()

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def move(__):
        if not __.mort:
            if __.direction == 1:
                if __.collision_mur(__.x+G.R/2, __.y):
                    __.x += G.R/2
            elif __.direction == 2:
                if __.collision_mur(__.x, __.y-G.R/2):
                    __.y -= G.R/2
            elif __.direction == 3:
                if __.collision_mur(__.x-G.R/2, __.y):
                    __.x -= G.R/2
            elif __.direction == 4:
                if __.collision_mur(__.x, __.y+G.R/2):
                    __.y += G.R/2
    
            if __.bomb and __.pose < __.max_bomb:
                if __.new_bomb == None:
                    __.bomb = False
                    __.new_bomb = Bombe(__.x,__.y,__)
        G.game.blit(__.sprite, (__.x, __.y))

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def collision_mur(__,x,y):
        for m in G.MURS:
            if x + __.r * 1.5 > m.x and x + 8  < m.x + G.R * 2 and y + __.r * 1.5 > m.y and y + 8  < m.y + G.R * 2:
                return 0
        for b in G.BOMBS:
            if b == __.new_bomb:
                if DISTANCE(x, y, b.x, b.y) > G.R:
                  __.new_bomb = None
            else:
                if DISTANCE(x, y, b.x, b.y) < G.R:
                    return 0
        return 1

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	def boom(__):
		if not __.mort: G.son_mort.play()
		__.sprite = pygame.transform.rotate(pygame.image.load('datas/img/joueurs/joueur_m.gif').convert(), __.dir * 90)
		G.game.blit(__.sprite, (__.x, __.y))
		__.mort = True

