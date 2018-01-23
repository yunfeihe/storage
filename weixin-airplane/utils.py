import pygame, stage, values
from random import randint

def loadImageFromPath(path):
	i = pygame.image.load(path)
	return i

def drawObjectOnContext(ob):
	stage.context.blit(ob.image, [ob.x, ob.y])
	pass

def goToScene(name):
	for s in values.scene:
		values.scene[s] = False
	values.scene[name] = True

def isSceneOn(name):
	return values.scene[name]
	pass

def isKeyDown(key):
	keys = pygame.key.get_pressed()
	return keys[key]

def log(a,b='debug:'):
	#print b,a
	pass

def timer(sec = 0.5):

	if values.timer_count % (sec * values.fps) == 0:
		return True
	else:
		return False

def isACollideB(a,b):
    p1 = (a.y < b.y + b.h )
    p2 = (a.y + a.h > b.y ) 
    p3 = (a.x > b.x - a.w and a.x < b.x + b.w)    
    if p1 and p2 and p3:
        return True
    else:
        return False

def random(a,b):
	return randint(a,b)
	pass

def loadMusicFromPath(path):
	m = pygame.mixer.Sound(path)
	return m

def playMusic(name,loop = 0):
	m = loadMusicFromPath(name)
	m.play(loops=loop)