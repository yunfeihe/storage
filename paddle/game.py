import pygame, levels, stage, tools, ob, values


mainScene = stage.mainScene()
titleScene = stage.titleScene()   
endScene = stage.endScene()
editScene = stage.editScene()

def FeiGame():
    
    class o():    
        def __init__(self):
            mainScene.setup()  
            titleScene.setup()   
            endScene.setup()
            editScene.setup()
            
        def update(self):
            if(values.scene['main']):  
                mainScene.draw()
                mainScene.update()                
           
            if(values.scene['title']):
                titleScene.draw()
                titleScene.update()
                
            if(values.scene['end']):
                endScene.draw()
                endScene.update()
            if(values.scene['edit']) :
                editScene.draw()
                editScene.update()
                  
            #debug
            '''if(values.mouse_dragging):
                stage.ball.x = pygame.mouse.get_pos()[0]
                stage.ball.y = pygame.mouse.get_pos()[1]                            
            for b in values.blocks:
                if(b.dragging):
                    b.x = pygame.mouse.get_pos()[0]
                    b.y = pygame.mouse.get_pos()[1] ''' 
    return o()    
                           
def __main():

    #初始化
    clock = pygame.time.Clock()
    pygame.init()
    g = FeiGame()
               
               
    while values.running:
    
        clock.tick(values.fps)   
        if(not values.pause):                                                        
            g.update()        
        
        #游戏事件监听
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                values.running = False
             
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if values.scene['main']:
                        values.k_a = True
                    elif(values.scene['edit']):
                        editScene.addBlock()
                if event.key == pygame.K_d:
                    values.k_d = True
                if event.key == pygame.K_f:
                    stage.ball.fired = True    
                if event.key == pygame.K_p:
                    values.pause = not values.pause
                    tools.log(values.pause,'Pause')
                if event.key == 61: #K_+
                    if(values.scene['main']):
                        levels.level('plus')
                        mainScene.reset()
                    else:
                        editScene.saveLevelToLevels()
                        tools.dumpsLevels()
                if event.key == 45:  #k_-
                    if(values.scene['main']):
                        levels.level('minus')
                        mainScene.reset()
                    elif(values.scene['edit']):
                        editScene.emptyBlocks()
                if event.key == pygame.K_r:
                    stage.goToScene('main')
                    mainScene.reset()
                if event.key == pygame.K_e:
                    stage.goToScene('edit')
                if event.key == 27: #esc键
                    stage.goToScene('title')   
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    values.k_a = False
                if event.key == pygame.K_d:
                    values.k_d = False

    pygame.quit()
                                 
   
if __name__=='__main__':    #确保不会在当作模块调用时执行本函数   
    __main()
