import pygame, stage, values
from utils import *

def FeiGame():
	class o():
		def __init__(self):
			stage.titleScene.setup()
			stage.mainScene.setup()
			stage.endScene.setup()

		def update(self):
			if isSceneOn('title'):
				stage.titleScene.draw()
				stage.titleScene.update()
			if isSceneOn('main'):
				stage.mainScene.draw()
				stage.mainScene.update()
			if isSceneOn('end'):
				stage.endScene.draw()
				stage.endScene.update()
			pygame.display.update()
	return o()

def __main():
	pygame.init()
	pygame.display.set_caption('weixin-airplane')
	g = FeiGame()
	clock = pygame.time.Clock()

	running = True
	while running:

		clock.tick(values.fps)
		values.timer_count += 1
		g.update()

		if isKeyDown(pygame.K_ESCAPE):
			goToScene('end')

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					stage.mainScene.reset()
					goToScene('main')
				if event.key == pygame.K_ESCAPE:
					goToScene('end')
					stage.endScene.saveData()

	pygame.quit()

if __name__ == '__main__':
	__main()