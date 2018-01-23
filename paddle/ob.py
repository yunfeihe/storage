import pygame, tools, values

#初始化图片
def Images():
    paddle = tools.imageFromPath('img/paddle.png')
    ball = tools.imageFromPath('img/ball.png')
    block = tools.imageFromPath('img/block.png')  
    bg = tools.imageFromPath('img/bg.png')
    class o():      
        def __init__(self):
            self.paddle = paddle
            self.ball = ball
            self.block = block 
            self.bg = bg
    return o()

#游戏对象
def Paddle():    
    class o():
        def __init__(self):
            self.image = images.paddle
            self.x = 100
            self.y = 250
            self.w = self.image.get_width()
            self.h = self.image.get_height()
            self.speed = 5
            
        def move(self):
            if(values.k_a and self.x >= 0):
                self.x -= self.speed
            if(values.k_d and self.x + self.w <= 400):
                self.x += self.speed           
    return o()

def Block(position):
        p = position
        
        class o():
            def __init__(self):
                self.image = images.block
                tools.log(p)
                self.x = p[0]
                self.y = p[1]
                self.w = self.image.get_width()
                self.h = self.image.get_height()
                self.dragging = False
                
                if(len(p) >2 ):
                    self.lifes = p[2] 
                else:
                    self.lifes = 1
                    
            def kill(self):
                self.lifes -= 1
                if (self.lifes == 0):
                    values.score += 100
                    
            def get_info(self):
                return [self.x, self.y, self.lifes]
        return o()
       
def Ball():
        
        class o():
            def __init__(self):
                self.image = images.ball
                self.x = paddle.x + paddle.w/2
                self.y = paddle.y - 20
                self.w = self.image.get_width()
                self.h = self.image.get_height()
                self.speedX = 5
                self.speedY = 5
                self.fired = False
                self.alive = True
                
            def move(self):
                if (self.x < 0 or self.x + self.image.get_width() > 400):
                    self.speedX *= -1
                if (self.y < 0):
                    self.speedY *= -1
                self.x += self.speedX
                self.y += self.speedY
                if (self.y + self.image.get_height() > 300):
                    self.kill()
                
            def smartBounce(self):
                #log(self.x, self.y)
                if(values.k_a):
                    if(self.speedX > 0):
                        self.speedX *= -1
                if(values.k_d):
                    if(self.speedX < 0):
                        self.speedX *= -1
                self.speedY *= -1
            def bounce(self):
                tools.log('times')
                self.speedX *= -1
                self.speedY *= -1
                
            def kill(self):
                self.alive = False
        return o()

def Text(pos,text):
    Text_type = pygame.font.Font('msyh.ttf',16)
    t = text
    class o():
        def __init__(self,pos = pos):
            self.image = Text_type.render(t, True, [255,255,255])
            self.x = pos[0]
            self.y = pos[1]
        def updateText(self,text = t):
            tools.log(text)
            self.image = Text_type.render(text, True, [255,255,255])
    return o()        
            
images = Images()
paddle = Paddle()
ball = Ball()