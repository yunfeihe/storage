import pygame
from utils import *

def Images():
    enemy0 = loadImageFromPath('image/enemy0.png')
    enemy1 = loadImageFromPath('image/enemy1.png')
    enemy2 = loadImageFromPath('image/enemy2.png')
    enemy2_1 = loadImageFromPath('image/enemy2_1.png')        
    
    hero1 = loadImageFromPath('image/hero1.png')
    hero2 = loadImageFromPath('image/hero2.png')
    
    enemy0down1 = loadImageFromPath('image/enemy0_down1.png')
    enemy0down2 = loadImageFromPath('image/enemy0_down2.png')
    enemy0down3 = loadImageFromPath('image/enemy0_down3.png')
    enemy0down4 = loadImageFromPath('image/enemy0_down4.png')

    enemy1down1 = loadImageFromPath('image/enemy1_down1.png')
    enemy1down2 = loadImageFromPath('image/enemy1_down2.png')
    enemy1down3 = loadImageFromPath('image/enemy1_down3.png')
    enemy1down4 = loadImageFromPath('image/enemy1_down4.png')

    enemy2down1 = loadImageFromPath('image/enemy2_down1.png')
    enemy2down2 = loadImageFromPath('image/enemy2_down2.png')
    enemy2down3 = loadImageFromPath('image/enemy2_down3.png')
    enemy2down4 = loadImageFromPath('image/enemy2_down4.png')
    enemy2down5 = loadImageFromPath('image/enemy2_down5.png')
    enemy2down6 = loadImageFromPath('image/enemy2_down6.png')

    playerdown1 = loadImageFromPath('image/hero_blowup1.png')
    playerdown2 = loadImageFromPath('image/hero_blowup2.png')
    playerdown3 = loadImageFromPath('image/hero_blowup3.png')
    playerdown4 = loadImageFromPath('image/hero_blowup4.png')

    enemy1hit = loadImageFromPath('image/enemy1_hit.png')
    enemy2hit = loadImageFromPath('image/enemy2_hit.png')

    bullet1 = loadImageFromPath('image/bullet1.png')
    bullet2 = loadImageFromPath('image/bullet2.png')
    bullet3 = loadImageFromPath('image/bullet3.png')
    class o():      
        def __init__(self):
            self.bg = loadImageFromPath('image/background.png')
            self.bg_end = loadImageFromPath('image/gameover.png')
            self.bullet = [bullet1,bullet2,bullet3]
            self.title = loadImageFromPath('image/title.png')
            self.enemies = [enemy0,enemy1,enemy2]
            self.enemy0down=[enemy0down1,enemy0down2,enemy0down3,enemy0down4]
            self.enemy1down=[enemy1down1,enemy1down2,enemy1down3,enemy1down4]
            self.enemy2down=[enemy2down1,enemy2down2,enemy2down3,enemy2down4,enemy2down5,enemy2down6]
            self.enemyDown =[self.enemy0down,self.enemy1down,self.enemy2down]
            self.player = [hero1,hero2]
            self.playerDown = [playerdown1,playerdown2,playerdown3,playerdown4]
            self.enemy1hit = [enemy1hit,enemy1]
            self.enemy2hit = [enemy2hit,enemy2]
            self.enemy0hit = [enemy0]
            self.enemyHit = [self.enemy0hit,self.enemy1hit,self.enemy2hit]
            self.enemy2_move = [enemy2_1,enemy2]
    return o()

def Sounds():
    class o():
        def __init__(self):
            self.bullet = 'sound/bullet.wav'
            self.end = 'sound/game_over.wav'
            self.game = 'sound/game_music.wav'
            self.enemy0down = 'sound/enemy0_down.wav'
            self.enemy1down = 'sound/enemy1_down.wav'
            self.enemy2down = 'sound/enemy2_down.wav'
            self.enemyDown = [self.enemy0down,self.enemy1down,self.enemy2down]
    return o()

images = Images()
sounds = Sounds()