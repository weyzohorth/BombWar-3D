from __init__ import *
from fire import Fire

class Bombe:
	def __init__(__,x,y,joueur):
		G.BOMBS.append(__)
		if joueur.telecom > len(joueur.bomb_tel):
			joueur.bomb_tel.append(__)
			G.son_bomb_tel.play()
			__.sprite = pygame.image.load('datas/img/bombes/telecom/bomb_tel0.gif').convert()
		elif joueur.bomb_tel:
			G.son_bomb.play()
			__.sprite = pygame.image.load('datas/img/bombes/telecom/bomb_tel.gif').convert()
		else:
			G.son_bomb.play()
			__.sprite = pygame.image.load('datas/img/bombes/normal/bomb0.gif').convert()
		joueur.pose += 1
		__.x, __.y = x, y
		__.r = G.R
		__.joueur = joueur
		__.telecom = __.joueur.telecom
		__.compte = 0
		__.explose = 0

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	def move(__):
		if not __.explose:
			if __.compte < 121:
				if not __.telecom:
					__.compte += 1
					if __.compte < 90:
						__.sprite = pygame.image.load('datas/img/bombes/normal/bomb'+str(__.compte)+'.gif').convert()
					else:
						if __.compte not in [96, 97, 103, 104, 109, 110, 114, 115, 118, 119]:
							__.sprite = pygame.image.load('datas/img/bombes/normal/bomb87.gif').convert()
						else:
							__.sprite = pygame.image.load('datas/img/bombes/normal/bomb89.gif').convert()
				else:
					__.compte = (__.compte + 1) % 3
					if __ in __.joueur.bomb_tel:
						__.sprite = pygame.image.load('datas/img/bombes/telecom/bomb_tel'+str(__.compte)+'.gif').convert()
						if __.joueur.BOOM:
							__.boom()
							__.joueur.BOOM = False
				G.game.blit(__.sprite, (__.x, __.y))
			else:
				__.boom()

#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	def boom(__):
		if not pygame.mixer.get_busy(): G.son_explo.play()
		__.explose = 1
		try: G.BOMBS.remove(__)
		except: pass
		__.joueur.pose -= 1

		if __ in __.joueur.bomb_tel: __.joueur.bomb_tel.remove(__)

		for i in range(5):
			Fire(__.x,__.y,4-i,__.joueur)
