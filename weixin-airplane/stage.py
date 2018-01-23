import pygame, ob, loads
from utils import *


context = pygame.display.set_mode([480,850])

class Scene():
	def __init__(self):
		self.elements = []

	def draw(self):
		for e in self.elements:
			drawObjectOnContext(e)

	def update(self):
		for e in self.elements:
			e.update()

	def addElement(self, e):
		self.elements.append(e)

	def delElement(self, e):
		self.elements.remove(e)

	def set_bg(self, img, pos = [0, 0]):
		bg = ob.NewImage(img, pos)
		self.addElement(bg)

	def write(self,text,pos,size=40):
		text_type = pygame.font.Font('font/MarkerFelt.ttf',size)
		t = text_type.render(text,True,[255,255,255])
		context.blit(t,pos)

def TitleScene():
	class o(Scene):
		def setup(self):
			playMusic(loads.sounds.game,loop=-1)
			self.set_bg(loads.images.bg)

		def update(self):
			self.write('Press R to start the game',[50,425])

	return o()

def MainScene():
	class o(Scene):
		def __init__(self):
			self.player = ob.Player()
			self.numberOfEnemy = 12

		def setup(self):
			self.elements = []
			self.enemies = []
			self.bullets = []
			self.bullets_es = []
			self.set_bg(loads.images.bg)
			self.addEnemies()
			self.addElement(self.player)


		def reset(self):
			values.scores = 0
			endScene.openData()
			self.player.alive = True
			self.player.image = loads.images.player[0]
			self.player.a_move.keepGoing()
			self.player.a_death.played = False
			self.player.x = 200
			self.player.y = 700
			self.player.collide_blocks=[]
			self.player.setCollideBlock(values.c_p)
			self.setup()

		def update(self):
			for e in self.elements:
				e.update()
			self.write('Scores:%d'%values.scores, [0,0])
			
			#the collide between enemy and bullet_player
			for ey in self.enemies:
				for ey_c in ey.collide_blocks:
					for b_player in self.bullets:
						for b_c in b_player.collide_blocks:
							if(isACollideB(ey_c,b_c)):
								ey.hit()
								b_player.hit()
					for p_c in self.player.collide_blocks:
						if(isACollideB(ey_c,p_c)):
							self.player.hit()
			#the collide between bulllet_enemy and player				
			for b_enemy in self.bullets_es:
				for b_c in b_enemy.collide_blocks:
					for p_c in self.player.collide_blocks:
						if(isACollideB(b_c,p_c)):
							self.player.hit()
							b_enemy.hit()
							self.player.hit()

			if(len(self.enemies)<5):
				self.addEnemies()


		def addEnemies(self):
			for i in range(0,self.numberOfEnemy):
				if(random(1,10)<8):
					e_type = random(0,1)
				else:
					e_type = 2
				e = ob.Enemy(e_type)
				self.addElement(e)
				self.enemies.append(e)

	return o()

def EndScene():
	class o(Scene):
		def setup(self):
			self.set_bg(loads.images.bg_end)
			self.openData()
			
		def update(self):
			self.write('%d' %values.scores,[200,580],size = 60)
			self.write('%d' %self.history_score,[200,280],size=60)
			self.write('Press R to start the game',[50,425])

		def openData(self):
			f_i = open ('score.data','r')
			self.history_score = int(f_i.read())
			f_i.close()

		def saveData(self):
			f_o = open ('score.data','w')  
			if(values.scores>self.history_score):
				f_o.write('%d' %values.scores)
			else:
				f_o.write('%d' %self.history_score)
			f_o.close()

	return o()

titleScene = TitleScene()
mainScene = MainScene()
endScene = EndScene()