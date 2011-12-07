from __init__ import *
from mod_math import DISTANCE

class Fire:
	def __init__(__,x,y,sens,joueur):
		G.FIRES.append(__)
		if sens: __.max = joueur.max_size
		else: __.max = joueur.max_size_milieu
		__.sens = sens
		__.x, __.y = x, y
		__.plus = __.touche = 0
		__.nucleary = joueur.nucleary

		__.image = pygame.image.load('datas/img/flammes/f'+ "n" * int(bool(joueur.nucleary)) + str(sens)+ '.gif').convert()
		__.sprite = __.image
		G.game.blit(__.sprite, (__.x, __.y))

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	def move(__):
		if __.plus < __.max * G.R + 1 and __.touche <= __.nucleary:
			__.plus += int(G.R) #/ (1 + bool(not __.sens))
			X = G.R + __.plus
			if not __.sens:
				X += G.R
				__.sprite = pygame.transform.scale(__.image, (X, X))
			elif 2 != __.sens != 4:#gauche droite
				__.sprite = pygame.transform.scale(__.image, (X, G.R))
			else:
				__.sprite = pygame.transform.scale(__.image, (G.R, X))

			x = y = 0
			if not __.sens: x = y= __.plus * 0.5
			elif __.sens == 2:  y = __.plus
			elif __.sens == 3: x = __.plus

			__.collision(G.JOUEURS)
			__.collision(G.BOMBS)
			__.collision(G.MURS,1)
			G.game.blit(__.sprite, (__.x - x, __.y - y))
		else:
			G.FIRES.remove(__)

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	def collision(__,objets,mur=0):
		for j in objets:
			if __.sens == 1:#doite
				if __.x + G.R/2 < j.x + j.r * 2 and __.x + G.R/2 + __.plus > j.x and __.y + G.R/2 < j.y + j.r * 2 and __.y + G.R * 1.5 > j.y:
					j.boom()
					__.touche += 1

			elif __.sens == 2:#haut
				if __.x + G.R/2 < j.x + j.r * 2 and __.x + G.R * 1.5 > j.x and __.y - G.R/2 - __.plus < j.y + j.r * 2 and __.y  -  G.R/2> j.y:
					j.boom()
					__.touche += 1

			elif __.sens == 3:#gauche
				if __.x - G.R/2 - __.plus < j.x + j.r * 2 and __.x -  G.R/2 > j.x and __.y + G.R/2 < j.y + j.r * 2 and __.y + G.R * 1.5 > j.y:
					j.boom()
					__.touche += 1

			elif __.sens == 4:#bas
				if __.x + G.R/2 < j.x + j.r * 2 and __.x + G.R * 1.5 > j.x and __.y + G.R/2 < j.y + j.r * 2 and __.y + G.R/2 + __.plus > j.y:
					j.boom()
					__.touche += 1

			else:#centre
				if DISTANCE(__.x, __.y, j.x, j.y) < (mur * G.R + __.plus)/2:
					j.boom()
