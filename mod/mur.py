from __init__ import *
from random import randrange
from bonus import Bonus

class Mur:
    names = ["basic indestructible", "basic destructible", "bord"]
    types = {names[0] : 0, names[1] : 1, names[2] : 0}
    
    def __init__(__, x, y, z=0, type_=0):
        G.MURS.append(__)
        __.x, __.y, __.z = x, y, z
        __.r = G.R
        __.name = __.names[type_]
        __.des = __.types[__.name]
        __.liste_sprite = {__.names[0] : G.liste_indestr, __.names[1] : G.liste_destr, __.names[2] : G.liste_bord}[__.name]
        #G.game.blit(__.sprite, (x, y))

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def boom(__):
        if __.des:
            if not randrange(3):
                Bonus(__.x,__.y)
            try:
                G.MURS.remove(__)
            except:
                pass

    def draw(__):
        glPushMatrix()
        glTranslated(__.x, __.y, __.z)
        glScaled(G.bloc_size, G.bloc_size, G.bloc_size)
        glCallList(__.liste_sprite)
        glPopMatrix()

