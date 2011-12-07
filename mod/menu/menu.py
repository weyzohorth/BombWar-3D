# -*- coding: cp1252 -*-
from __init__ import *
from jouer import Jouer

class Menu:
	back = pygame.Surface((G.WIDTH, G.HEIGHT))
	weyzohorth = pygame.image.load("datas/img/menu/W3YZOH0RTH.gif").convert()
	bombwar1 = M.font_bw.render("BombWar", True, pygame.Color(0, 255, 0, 255))
	bombwar2 = M.font_bw.render("BombWar", True, pygame.Color(255, 0, 0, 0))
	liste_menu = []
	for i in ["jouer", "commandes", "options", "site web", "quitter"]:
		liste_menu.append((M.font1.render(i, True, pygame.Color(0, 0, 155, 255)),
						M.font2.render(i, True, pygame.Color(255, 0, 0, 0))))
	bw1_1 = M.font_bw.render(G.version, True, pygame.Color(0, 255, 0, 255))
	bw1_2 = M.font_bw.render(G.version, True, pygame.Color(255, 0, 0, 0))
	txt = M.font_txt.render("Vous présente", True, pygame.Color(255, 0, 0, 0))

	def __init__(__):
		__.start = __.quit = False
		__.i = -640
		__.phase = 0
		__.old_select = __.select = 0
		__.boucle()

	def boucle(__):
		while not __.quit and not __.start:
			G.screen.blit(__.back, (0, 0))
			if not __.phase:
				if __.i < 0:
					G.screen.blit(__.weyzohorth, (__.i, 100))
				else:
					__.i = -385
					__.phase += 1
					G.screen.blit(__.weyzohorth, (0, 100))
			elif __.phase == 1:
				if __.i < 645:
					G.screen.blit(__.weyzohorth, (0, 100))
					G.screen.blit(__.txt, (__.i, 300))
				else:
					__.i = -5
					__.phase += 1
					G.screen.blit(__.weyzohorth, (0, 100))
			elif __.phase == 2:
				if __.i <= 255:
					__.weyzohorth.set_alpha(255 - __.i)
					G.screen.blit(__.weyzohorth, (0, 100 + __.i))
					G.screen.blit(__.bombwar1, (0, -200 + __.i))
					G.screen.blit(__.bombwar2, (5, -195 + __.i))
					G.screen.blit(__.bw1_1, (400, -125 + __.i))
					G.screen.blit(__.bw1_2, (405, -120 + __.i))
				else:
					G.screen.blit(__.bombwar1, (0, 55))
					G.screen.blit(__.bombwar2, (5, 60))
					G.screen.blit(__.bw1_1, (400, 130))
					G.screen.blit(__.bw1_2, (405, 135))
					__.phase += 1
					__.i = -640
			elif __.phase == 3:
				if __.i <= 500:
					G.screen.blit(__.bombwar1, (0, 55))
					G.screen.blit(__.bombwar2, (5, 60))
					G.screen.blit(__.bw1_1, (400, 130))
					G.screen.blit(__.bw1_2, (405, 135))
					for y, item in enumerate(__.liste_menu):
						x = __.i - y * 100
						if x > 20: x = 20
						for i in item: G.screen.blit(i, (x, 180 + y*90))
				else:
					__.phase += 1
					__.i = 0
					G.screen.blit(__.bombwar1, (0, 55))
					G.screen.blit(__.bombwar2, (5, 60))
					G.screen.blit(__.bw1_1, (400, 130))
					G.screen.blit(__.bw1_2, (405, 135))
					for y, item in enumerate(__.liste_menu):
						for i in item: G.screen.blit(i, (20, 180 + y*90))

			else:
				G.screen.blit(__.bombwar1, (0, 55))
				G.screen.blit(__.bombwar2, (5, 60))
				G.screen.blit(__.bw1_1, (400, 130))
				G.screen.blit(__.bw1_2, (405, 135))
				for y, item in enumerate(__.liste_menu):
					G.screen.blit(item[0], (20, 180 + y*90))
					if __.select == y: G.screen.blit(item[1], (20 + __.i, 180 + __.i + y*90))
					elif __.old_select == y: G.screen.blit(item[1], (30 - __.i, 190 - __.i + y*90))
					else: G.screen.blit(item[1], (20, 180 + y*90))
				if __.i < 10: __.i += 1

			if __.phase < 4: __.i += 5

			pygame.display.update()

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					__.quit = True
				elif  event.type == KEYDOWN:
					if __.phase != 4:
						__.phase =4
						__.i = 0
					else:
						if event.key == 273 or event.key == 274:
							__.old_select = __.select
							__.i = 0
							if event.key == 274: __.select = (__.select + 1) % 5
							else:__.select = (__.select - 1) % 5
						elif event.key == 13:#Entree
							if __.select == 0: Jouer(__)

			pygame.time.delay(40)
