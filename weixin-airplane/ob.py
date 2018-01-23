import pygame, loads, stage, values, random
from utils import *

class NewO():
	def __init__(self):
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.alive = True
		self.collide_blocks=[]

	def update(self):
		pass


	def setCollideBlock(self,data):
		#data means relative position
		for d in data:
			pos = [d[0],d[1]]
			size = [d[2],d[3]]
			b = CollideBlock(self,pos,size)
			self.collide_blocks.append(b)

def NewImage(img,pos):
	class o(NewO):
		def __init__(self):
			self.image = img
			self.x = pos[0]
			self.y = pos[1]
			
			NewO.__init__(self)

	return o()

def Player():
	class o(NewO):
		def __init__(self):
			self.image = loads.images.player[0]
			self.x = 200
			self.y = 700
			self.speed = 5
			#Animation
			self.a_move = Animation(self,loads.images.player)
			self.a_death = Animation(self, loads.images.playerDown)
			#

			NewO.__init__(self)
			self.setCollideBlock(values.c_p)

		def move(self):
			if (isKeyDown(pygame.K_w ) and self.y >= 0):
				self.y -= self.speed
				for c_b in self.collide_blocks:
					c_b.move('up',self.speed)
			if (isKeyDown(pygame.K_s) and (self.y + self.h) <= 875):
				self.y += self.speed
				for c_b in self.collide_blocks:
					c_b.move('down',self.speed)
				self.s_fire = loadMusicFromPath(loads.sounds.bullet)
			if (isKeyDown(pygame.K_a) and self.x >=5):
				self.x -= self.speed
				for c_b in self.collide_blocks:
					c_b.move('left',self.speed)
			if (isKeyDown(pygame.K_d) and self.x+self.w <=480):
				self.x += self.speed
				for c_b in self.collide_blocks:
					c_b.move('right',self.speed)

		def update(self):
			self.move()
			self.a_move.play(0.5)
			#log(self.collide_blocks[0].y,'player.y:')
			#log(self.collide_blocks[0].x,'player.x:')
			if isKeyDown(pygame.K_j) :
				if timer(0.25):
					self.fire()
			if(not self.alive):
				self.a_move.stop()
				self.a_death.play(0.1)
				if(self.a_death.played):
					goToScene('end')
					stage.endScene.saveData()

		def fire(self):
			playMusic(loads.sounds.bullet)
			pos=[self.x + self.w / 2 - 3,self.y]
			b = Bullet(pos)
			stage.mainScene.addElement(b)
			stage.mainScene.bullets.append(b)

		def kill(self):
			self.alive = False
			playMusic(loads.sounds.end)
			

		def hit(self):
			self.kill()


	return o()

def Enemy(e_type=random(0,2)):
	class o(NewO):

		def __init__(self):
			self.type = e_type
			self.image = loads.images.enemies[self.type]
			self.x = random(0,450) 
			self.y = -random(100,1500)
			self.speed = random(1,3)
			self.lifes = (self.type+1)**2
			self.hitted = False
			#Animation
			self.a_e2_move = Animation(self,loads.images.enemy2_move)
			self.a_death = Animation(self, loads.images.enemyDown[self.type])
			self.a_hit = Animation(self, loads.images.enemyHit[self.type])
			#Sound
			NewO.__init__(self)
			self.setCollideBlock(values.c_es[self.type])
		
		def move(self):
			self.y += self.speed
			pass

		def update(self):
			self.move()
			#fire
			if(self.type==2):
				if(timer(1.5)):
					self.fire()
			else:
				if(timer(2)):
					self.fire()
			if(self.type == 2):
				self.a_e2_move.play(0.5)
			#play death animation
			if(not self.alive):
				self.a_e2_move.stop()
				self.a_death.play(0.1)
				self.kill()
			#play hit animation
			if(self.hitted and self.alive):
				if(self.a_hit.played):
					self.hitted = False
					self.a_e2_move.keepGoing()
					self.a_hit.played = False
				self.a_e2_move.stop()
				self.a_hit.play(5/60.0,loop=1)
			#update collide blocks
			for b in self.collide_blocks:
				b.move('down',step=self.speed)
			#suicide
			if self.y > values.window_height:
				if(self in stage.mainScene.enemies):
					stage.mainScene.enemies.remove(self)
				if(self in stage.mainScene.elements):
						stage.mainScene.delElement(self)
			log(len(stage.mainScene.enemies), 'number of enemy now:')
		
		def kill(self):
			#collide self dead
			self.alive = False
			if(self in stage.mainScene.enemies):
				stage.mainScene.enemies.remove(self)
				values.scores += (self.type+1)*100
			playMusic(loads.sounds.enemyDown[self.type])
			#draw self dead
			if(self.a_death.played):
				if(self in stage.mainScene.elements):
					stage.mainScene.delElement(self)
			
		def hit(self):
			self.lifes -= 1
			if(self.lifes==0):
				self.kill()
			self.hitted = True

		def fire(self):
			pos=[self.x+self.w/2-5,self.y+self.h]
			b = Bullet(pos,type=2)
			stage.mainScene.addElement(b)
			stage.mainScene.bullets_es.append(b)
	
	return o()

def Bullet(pos,type = 0):
	class o(NewO):

		def __init__(self):
			self.type = type
			self.image = loads.images.bullet[self.type]
			self.x = pos[0]
			self.y = pos[1]
			if(self.type==0):
				self.speed = 10
			else:
				self.speed = 4
			NewO.__init__(self)
			self.setCollideBlock([[0,0,0,0]])

		def move(self):
			if(self.type == 0):
				self.y -= self.speed
			if(self.type == 2):
				self.y += self.speed

		def update(self):
			for b in self.collide_blocks:
				if(self.type == 0):
					b.move('up',step=self.speed)
				if(self.type == 2):
					b.move('down',step=self.speed)
			self.move()

			if(self.y > 850 or self.y +self.h < 0):
				self.kill()

		def kill(self):
			self.alive = False
			if(self in stage.mainScene.bullets):
				stage.mainScene.bullets.remove(self)
			if(self in stage.mainScene.bullets_es):
				stage.mainScene.bullets_es.remove(self)
			if(self in stage.mainScene.elements):
				stage.mainScene.delElement(self)

		def hit(self):
			self.kill()

	return o()

def CollideBlock(ob,pos,size):
	x = pos[0] + ob.x
	y = pos[1] + ob.y
	w = size[0]
	h = size[1]

	class o():
		def __init__(self):
			self.x = x
			self.y = y
			self.w = w
			self.h = h
			self.speed = 0

		def move(self, order,step = 0):
			if(step == 0):
				step = self.speed
			
			if(order == 'left'):
				self.x -= step
			if(order == 'right'):
				self.x += step
			if(order == 'up'):
				self.y -= step
			if(order == 'down'):
				self.y += step

	return o()

def Animation(ob,images):
	class o():
		def __init__(self):
			self.animaionIndex = 0
			self.played = False
			self.stopped = False
		def play(self,sec=0.5,loop = -1):
			if(not self.stopped):
				if(timer(sec)):
					if(self.animaionIndex == len(images)):
						self.animaionIndex = 0
						self.played = True
						if(loop == 1):
							return 0
					ob.image = images[self.animaionIndex]
					self.animaionIndex += 1
		def stop(self):
			self.stopped = True
		
		def keepGoing(self):
			self.stopped = False
	return o()