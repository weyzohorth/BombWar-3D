import pygame
from pygame.locals import *
from mod_gl import *

pygame.init()

class Global:
    liste_destr = None
    liste_indestr = None
    
    def __init__(__):
        __.version = "3D 1.0"
        __.JOUEURS = []
        __.MURS = []
        __.BOMBS = []
        __.BONUS = []
        __.FIRES = []
        __.R = 23
        __.WIDTH = __.HEIGHT = 640
        __.map_x, __.map_y = (500, 500)
        __.bloc_size = 2
        __.f = 1000
        __.n = 1
        __.temps_boucle = 40
        w = int(__.WIDTH/(__.R*2)) + 1
        h = int(__.HEIGHT/(__.R*2)) + 1
        __.xmax = __.WIDTH - (not w % 2) * __.R * 2
        __.ymax = __.HEIGHT - (not h % 2) * __.R * 2
        __.son_mort = pygame.mixer.Sound("datas/son/mort.ogg")
        __.son_explo = pygame.mixer.Sound("datas/son/boom.ogg")
        __.son_bonus = pygame.mixer.Sound("datas/son/bonus.ogg")
        __.son_bomb = pygame.mixer.Sound("datas/son/bomb.ogg")
        __.son_bomb_tel = pygame.mixer.Sound("datas/son/bomb_tel.ogg")
        pygame.mixer.music.load("datas/son/02 - Sleepwalker.ogg")
        __.screen = pygame.display.set_mode((__.WIDTH, __.HEIGHT))
        pygame.display.set_icon(pygame.image.load('datas/img/joueurs/joueur0.gif').convert())
        pygame.display.set_caption("BombWar 1.0 by W3YZOH0RTH", "BombWar")
    
    def init3d(__):
        __.bord = load_texture("datas/img/tex/shogo4.gif")
        __.destr = load_texture("datas/img/tex/shogo1.gif")
        __.indestr = load_texture("datas/img/tex/shogo2.gif")
        __.bio = load_texture("datas/img/tex/pak4_rck1_drt4.gif")
        __.floor = load_texture("datas/img/tex/shogo3.gif")
        __.exp = load_texture("datas/img/tex/pak4_mtl1_wl6.gif")
        
        __.liste_destr = glGenLists(1)
        glNewList(__.liste_destr, GL_COMPILE)
        draw_pave(1, 1, 1, tex=__.destr, couleur=())
        glEndList()
        __.liste_indestr = glGenLists(1)
        glNewList(__.liste_indestr, GL_COMPILE)
        draw_pave(1, 1, 1, tex=__.indestr, couleur=())
        glEndList()
        __.liste_bord = glGenLists(1)
        glNewList(__.liste_bord, GL_COMPILE)
        draw_pave(1, 1, 1, tex=__.bord, couleur=())
        glEndList()

G = Global()
