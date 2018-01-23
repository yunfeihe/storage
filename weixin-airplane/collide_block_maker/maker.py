import pygame, values

pygame.init()
context = pygame.display.set_mode([500,500])

def Maker():

	class o():

		def __init__(self):
			self.ob = loadImageFromPath('img/1.png')
			self.blocks = []

		def update(self):
			pygame.display.update()

		def draw(self):
			context.fill([125,125,125])			
			context.blit(self.ob,[0,0])
			for b in self.blocks:
				drawBlock(b)
			drawRect(size=[values.size_width,values.size_height],pos=getMousePos())

		def loadAndDrawImage(self,path):
			loadImageFromPath(path)

	return o()

def __main():

	global maker
	maker = Maker()
	running = True

	while running:
		maker.draw()
		maker.update()

		if(isKeyDown(pygame.K_q) and not isKeyDown(pygame.K_LSHIFT)):
			values.size_width += 1
		if(isKeyDown(pygame.K_e) and not isKeyDown(pygame.K_LSHIFT)):
			values.size_height += 1
		if(isKeyDown(pygame.K_r)):
			values.size_height = 10
			values.size_width = 10

		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					b = Block(color=values.color_white,pos=getMousePos(),size=[values.size_width,values.size_height])
					maker.blocks.append(b)
				if event.key == pygame.K_q:
					values.size_width += 1
				if event.key == pygame.K_e:
					values.size_height += 1
				if event.key == pygame.K_s:
					saveDate()

	pygame.quit()

def loadImageFromPath(path):
	i = pygame.image.load(path)
	return i 

def isKeyDown(key):
	keys = pygame.key.get_pressed()
	return keys[key]

def isMouseDown(order='left'):
	status = pygame.mouse.get_pressed()
	if(order == 'left'):
		return status[0]
	elif(order == 'right'):
		return status[2]
	else:
		return status[1]

def drawRect(color=[255,255,255],pos=[0,0],size = [25,25],width = 0):
	x = pos[0]
	y = pos[1]
	pygame.draw.rect(context, color, [x,y,size[0],size[1]],width)
	
def getMousePos():
	pos = pygame.mouse.get_pos()
	return pos

def Block(color=[255,255,255],pos=[0,0],size = [25,25],width = 0):
	class o():
		def __init__(self):
			self.color = color
			self.x = pos[0]
			self.y = pos[1]
			self.w = size[0]
			self.h = size[1]
			self.size = size
			self.width = width

	return o()

def drawBlock(ob):
	pygame.draw.rect(context, ob.color, [ob.x,ob.y,ob.size[0],ob.size[1]], ob.width)	
	pass

def saveDate():
	f = open('block_date.txt','w')
	'''
	x,y
	height,width

	'''
	f.write('[')
	for i in maker.blocks:
		f.write('[%d,%d,%d,%d],'%(i.x, i.y, i.w, i.h))
	f.write(']')
	f.close()

if __name__ == '__main__':
	__main()

