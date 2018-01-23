import pygame, ob, values, tools, levels


context = pygame.display.set_mode([400,300])
pygame.display.set_caption('Paddle')


paddle = ob.Paddle()
ball = ob.Ball()

class FeiScene():

    def __init__(self):
        self.elements = [] #储存绘画对象
        self.bg = [True,None]
        
    def draw(self):
        self.bg[0] or context.blit(self.bg[1],[0, 0])
        for e in self.elements:
            drawImage(e)            
        pygame.display.update() 
    def update():
        #相关逻辑
        pass
    def set_bg(self, backgroundImage):
        self.bg[1] = backgroundImage
        self.bg[0] = None
    def addElement(self, element):
        self.elements.append(element)
    
    def write(self,pos, text= u"text"):
        t = ob.Text(pos,text)
        self.addElement(t)
        return t
                
class mainScene(FeiScene):        
    def setup(self, n = 1):
        levels.loadLevel(n)
        self.set_bg(ob.images.bg)
        self.addElement(paddle)
        self.addElement(ball)
        self.text_score = self.write([0,240],'Scores:%d' %values.score)
        self.text_level = self.write([0,260],'Level:%d' %values.level_now)
        
        for b in values.blocks:
            self.addElement(b)
        self.temp_blocks = self.elements[4:] #关于砖块的镜像
        tools.log('len:',len(values.blocks))
    def reset(self):
        self.elements = []
        ball.alive = True
        ball.fired = False
        ball.x = paddle.x + paddle.w/2
        ball.y = paddle.y - 20
        values.score = 0
        self.setup(values.level_now)

    def update(self):
        
        self.text_level.updateText()
        self.text_score.updateText('Scores:%d' %values.score)
        
        if (ball.fired):
            paddle.move()
            if(ball.alive):
                ball.move()
            else:
                goToScene('end')
        if(isACrackB(ball, paddle)):
            ball.smartBounce()
        for b in self.temp_blocks:    
            if (isACrackB(ball, b)):
                ball.bounce()
                b.kill()
                print b
                if(b.lifes == 0):
                    
                    self.elements.remove(b)
                    self.temp_blocks.remove(b)
        if (self.temp_blocks == []):
            if(values.level_now < levels.levels_max):
                values.level_now += 1
                self.reset()               
            else:
                #结束画面
                values.gameWin = True
                goToScene('end')
                
class titleScene(FeiScene):
    def setup(self):
        self.write([260,150],u'Press R to start')
        self.write([260,170],u'A,D to move')
        self.write([260,190],u'F to fire off')
        self.write([260,210],'E to edit level')
    
    def update(self):
        context.fill([0, 0, 0])
        

class endScene(FeiScene):
    def setup(self):
        pass
    
    def update(self):
        context.fill([0, 0, 0])
        if(values.gameWin):
            self.write([160,140],u'You win!')
        else:
            self.write([160, 140],u'Game Over')
        self.write([160, 160],u'Press R to restart')
        self.write([160,180], u'Esc to back to title')    

class editScene(FeiScene):
    def setup(self):
        self.set_bg(ob.images.bg)
        self.mouse_posx, self.mouse_posy = pygame.mouse.get_pos()
        self.text_blockpos = self.write([0,0],'Positon:(%d,%d)'%(self.mouse_posx,self.mouse_posy))
        self.text_level = self.write([0, 20],'Level:%d' %values.level_edit)
        self.write([0, 40],'+ to save the level')
        self.write([0,60], u'Esc to back to title')
    
    def update(self):
        self.mouse_posx, self.mouse_posy = pygame.mouse.get_pos()
        self.text_level.updateText('Level:%d' %values.level_edit)
        self.text_blockpos.updateText('Positon:(%d,%d)'%(self.mouse_posx,self.mouse_posy))
        context.blit(ob.Images().block, [self.mouse_posx, self.mouse_posy])
        for b in values.blocks:
            drawImage(b)
        values.gameOn = False
    
    def addBlock(self):
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        b = ob.Block([x,y])
        self.addElement(b)
    
    def emptyBlocks(self):
        blocks = self.elements[4:]
        for b in blocks:
            self.elements.remove(b)
        print self.elements
    def saveLevelToLevels(self):
        level = []
        blocks = self.elements[4:] #得到所有block对象
        tools.log('blocks:',len(blocks))
        for b in blocks:
            level.append(b.get_info())
            self.elements.remove(b)
        values.blocks = []
        values.levels.append(level)
        values.level_edit += 1
        #tools.dumpsLevels()
                    
def drawImage(o):
    x = o.x
    context.blit(o.image,[o.x, o.y])

def isACrackB(a,b):
    p1 = (a.y < b.y + b.h )
    p2 = (a.y + a.h > b.y ) 
    p3 = (a.x > b.x - a.w and a.x < b.x + b.w)    
    if p1 and p2 and p3:
        return True
    else:
        return False
          
def goToScene(name):
    
    for i in values.scene:
        values.scene[i] = True
    values.scene[name] = False
    for i in values.scene:
        values.scene[i] = not values.scene[i]