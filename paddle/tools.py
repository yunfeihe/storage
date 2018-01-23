import pygame, json, values

def imageFromPath(path):
    img = pygame.image.load(path)
    return img
    
def log (a ='debug',b=''):
    print a,b
    pass #调试时去掉上面注释
   
def isObjectChosenByMouse(o):
    if(pygame.mouse.get_pressed()[0]):
        mouse_pos = pygame.mouse.get_pos()
        xIn = o.x+o.w >= mouse_pos[0] >= o.x 
        yIn = o.y+o.h >= mouse_pos[1] >= o.y
        return (xIn and yIn)
   
def moveObjectByMouse(o):
    o.x = pygame.mouse.get_pos()[0]
    o.y = pygame.mouse.get_pos()[1]
    
def dumpsLevels():
    temp_date = json.dumps(values.levels)
    data_file = open('levels.data','w')
    data_file.write(temp_date)
    data_file.close()