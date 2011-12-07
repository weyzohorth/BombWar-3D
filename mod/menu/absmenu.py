from __init__ import *

class Abstract_menu:
	back = pygame.Surface((G.WIDTH, G.HEIGHT))

	def __init__(__, titre, liste_menu):
		__.titre1 = M.font_bw.render(titre, True, pygame.Color(0, 255, 0, 255))
		__.titre2 = M.font_bw.render(titre, True, pygame.Color(255, 0, 0, 0))
		__.liste_menu = []
		for i in liste_menu:
			__.liste_menu.append((M.font1.render(i, True, pygame.Color(0, 0, 155, 255)),
							M.font2.render(i, True, pygame.Color(255, 0, 0, 0))))
		__.quit = False
		__.i = __.old_select = __.select = 0
		__.lim = len(liste_menu)
		__.boucle()

	def boucle(__):
		while not __.quit:
			__.boucle_draw()
			__.boucle_event()
			pygame.time.delay(40)

	def boucle_draw(__):
		G.screen.blit(__.back, (0, 0))
		G.screen.blit(__.titre1, (0, 55))
		G.screen.blit(__.titre2, (5, 60))
		for y, item in enumerate(__.liste_menu):
			G.screen.blit(item[0], (20, 180 + y*90))
			if __.select == y: G.screen.blit(item[1], (20 + __.i, 180 + __.i + y*90))
			elif __.old_select == y: G.screen.blit(item[1], (30 - __.i, 190 - __.i + y*90))
			else: G.screen.blit(item[1], (20, 180 + y*90))
		if __.i < 10: __.i += 1
		__.draw()
		pygame.display.update()

	def boucle_event(__): pass

	def event_select(__, event):
		if event.key == 273 or event.key == 274:
			__.old_select = __.select
			__.i = 0
			if event.key == 274: __.select = (__.select + 1) % __.lim
			else:__.select = (__.select - 1) % __.lim
			return 1
		return 0

	def draw(__): pass
