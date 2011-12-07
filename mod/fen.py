from __init__ import *
from joueur import Joueur
from mur import Mur
from map import Map
from camera import Camera_FreeFly

class Fen:
    def __init__(__, joueurs=2):
        G.fen = __
        pygame.display.init()
        fullscreen = False
        resolution_screen = G.WIDTH, G.HEIGHT
        w, h = resolution_screen
        if fullscreen:
            if not resolution_screen:
                Info = pygame.display.Info()
                G.WIDTH, G.HEIGHT = Info.current_w, Info.current_h
            else: G.WIDTH, G.HEIGHT	= resolution_screen
        else: G.WIDTH, G.HEIGHT = w, h
        init(G.WIDTH, G.HEIGHT, G.n, G.f, 70, pygame.RESIZABLE | pygame.FULLSCREEN*fullscreen)
        G.init3d()
        
        G.game = pygame.Surface((G.xmax, G.ymax))
        __.back = pygame.Surface((G.xmax, G.ymax))
        #pygame.draw.rect(G.screen, pygame.Color(0, 255, 0, 50), (0, 0, G.WIDTH, G.HEIGHT), 0)
        __.x = (G.WIDTH - G.xmax) / 2
        __.y = (G.HEIGHT - G.ymax) / 2
        #G.screen.blit(G.game, (__.x, __.y))
        #G.game.blit(__.back, (0, 0))
        Map().create()
        #__.place_mur(joueurs)
        __.quit = False
        __.boucle()

    def boucle(__):
        __.temps = pygame.time.get_ticks()
        while not __.quit:
            if not pygame.mixer.music.get_busy(): pygame.mixer.music.play()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(70, float(G.WIDTH) / G.HEIGHT, G.n, G.f)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            __.blit()
            __.event()
            if not __.quit:
                pygame.display.flip()
                temp = pygame.time.get_ticks()
                temps_passe = temp  - __.temps
                __.temps = temp
                pygame.time.wait(G.temps_boucle - temps_passe)
        pygame.quit()

    def blit(__):
        #G.screen.blit(G.game, (__.x, __.y))
        #G.game.blit(__.back, (0, 0))
        #for i in G.BOMBS: i.move()
        #for i in G.JOUEURS: i.draw()
        G.JOUEURS[0].draw()
        for i in G.MURS: i.draw()
        #for i in G.BONUS: i.move()
        #for i in G.JOUEURS: i.move()
        #for i in G.FIRES: i.move()

    def event(__):
        for event in pygame.event.get():
            if event.type == QUIT:
                __.quit = True
            elif  event.type == KEYDOWN:
                __.event_keydown(event)
            elif  event.type == KEYUP:
                __.event_keyup(event)
            if event.type in Camera_FreeFly.events:
                for i in G.JOUEURS: i.event(event)
                    
    def event_keydown(__, event):
        if event.key == pygame.K_ESCAPE:
            __.quit = True
        for i in G.JOUEURS:
            if event.key == i.droite: i.direction_set(1)
            elif event.key == i.haut: i.direction_set(2)
            elif event.key == i.gauche: i.direction_set(3)
            elif event.key == i.bas: i.direction_set(4)
            elif event.key == i.activ_bomb: i.BOOM = True
            elif event.key == i.lache_bomb: i.bomb = True
    
    def event_keyup(__, event):	
        for i in G.JOUEURS:
            if event.key == i.droite: i.direction_set(0)
            elif event.key == i.haut: i.direction_set(0)
            elif event.key == i.gauche: i.direction_set(0)
            elif event.key == i.bas: i.direction_set(0)
            elif event.key == i.activ_bomb: i.BOOM = False
    
    
    def place_mur(__,nombre=2):
        w = int(G.xmax/(G.R*2)) + 1
        h = int(G.ymax/(G.R*2)) + 1
        for x in range(w):
            Mur(x * G.R * 2,  0)
            Mur(x * G.R * 2,  G.R * h * 2 - G.R * 2)
        for y in range(h-2):
            Mur(0,  G.R * 2 + y * G.R * 2)
            Mur(G.R * w * 2 - G.R * 2,  G.R * 2 + y * G.R * 2)
    
        for x in range(w-2):
            for y in range(h-2):
                if x != 0 and x!=1 or y!=0 and y!=1 or x==1 and y==1:
                    if x != w-3 and x!=w-4 or y!=0 and y!=1 or x==w-4 and y==1:
                        if x != w-3 and x!=w-4 or y!=h-3 and y!=h-4 or x==w-4 and y==h-4:
                            if x != 0 and x!=1 or y!=h-3 and y!=h-4 or x==1 and y==h-4:
                                if y % 2 and x % 2:
                                    Mur(G.R * 2 + x * G.R * 2,  G.R * 2 + y * G.R * 2)
                                else:
                                    Mur(G.R * 2 + x * G.R * 2,  G.R * 2 + y * G.R * 2,  1)
                            else:
                                if x == 0 and y ==h-3:
                                    if nombre >= 4:
                                        Joueur(G.R * 2 + x * G.R * 2,  G.R * 2 + y * G.R * 2)
                        else:
                            if x == w-3 and y ==h-3:
                                if nombre >= 2:
                                    Joueur(G.R * 2 + x * G.R * 2,  G.R * 2 + y * G.R * 2)
    
                    else:
                        if x == w-3 and y ==0:
                            if nombre >= 3:
                                Joueur(G.R * 2 + x * G.R * 2,  G.R * 2 + y * G.R * 2)
                else:
                    if x == 0 and y ==0:
                        Joueur(G.R * 2 + x * G.R * 2,  G.R * 2 + y * G.R * 2)
