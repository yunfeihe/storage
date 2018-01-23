

def CollideBlock(pos,size):
	class o():
		def __init__(self):
			self.x = pos[0]
			self.y = pos[1]
			self.w = size[0]
			self.h = size[1]
			self.speed = 0

		def move(self, order,step = self.speed):
			
			if(order == 'left'):
				self.x -= step
			if(order == 'right'):
				self.x += step
			if(order == 'up'):
				self.y -= step
			if(order == 'down'):
				self.y += step

	return o()