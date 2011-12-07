from absmenu import  *
from mod.fen import Fen

class Jouer(Abstract_menu):
	def __init__(__, boss):
		__.boss = boss
		Abstract_menu.__init__(__, "Joueurs", ["2", "3", "4"])

	def boucle_event(__):
		for event in pygame.event.get():
			if event.type == QUIT:
				__.quit = True
			elif  event.type == KEYDOWN:
				if not __.event_select(event):
					if event.key == 13:#Entree
						__.boss.quit = __.quit = True
						G.screen.blit(__.back, (0, 0))
						Fen(__.select + 2)
					elif event.key == 27:#Echap
						__.quit = True
