from __init__ import *
from random import randrange
from mod_math import DISTANCE

class Bonus:
	def __init__(__,x,y):
		G.son_bonus.play()
		G.BONUS.append(__)
		__.i = 0
		__.d = 0
		__.x, __.y, __.type = x, y, randrange(5)

		if __.type == 1:#flamme cote
			__.image = pygame.image.load('datas/img/autres/f+.gif').convert()
		elif __.type == 2:#flamme centre
			__.image = pygame.image.load('datas/img/flammes/f0.gif').convert()
		elif __.type == 3:#nucleary
			__.image = pygame.image.load('datas/img/autres/bomb_nucleary.gif').convert()
		elif __.type == 4:#telecommande
			__.image = pygame.image.load('datas/img/autres/telecom.gif').convert()
		else:#bomb
			__.image = pygame.image.load('datas/img/autres/bomb.gif').convert()
		__.sprite = __.image
		G.game.blit(__.sprite, (x, y))

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	def move(__):
		for j in G.JOUEURS:
			if DISTANCE(__.x,__.y,j.x,j.y) < G.R:
				if __.type == 1:
					j.max_size += 1
				elif __.type == 2:
					j.max_size_milieu += 1
				elif __.type == 3:
					j.nucleary += 1
					j.max_size += 1
					j.max_size_milieu += 1
				elif __.type == 4:
					j.telecom += 1
				else:
					j.max_bomb +=1
				G.son_bonus.play()
				G.BONUS.remove(__)

		__.i = (__.i + 1) % 10
		if not __.i:
			if __.sprite == __.image:
				__.sprite = pygame.transform.scale(__.image, (23, 23))
				__.d = 12
			else:
				__.sprite = __.image
				__.d = 0
		G.game.blit(__.sprite, (__.x + __.d, __.y + __.d))


