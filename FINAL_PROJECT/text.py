import sys
import pygame
from BaseMove import *
from game_fuction import *
from Choice import *
from sprite1 import *
pygame.font.init()
class Text1():
    def __init__(self,screen):
        self.screen = screen
        self.myFont = pygame.font.SysFont('Comic Sans MS', 20)
        self.use1 = self.myFont.render('Tackle',False,(0,0,0))
        self.use2 = self.myFont.render('Growl',False,(0,0,0))
        self.use3 = self.myFont.render('Water Gun',False,(0,0,0))
        self.use4 = self.myFont.render('Tail Whip',False,(0,0,0))
        self.rect1 = self.use1.get_rect(topleft = (8,467))
        self.rect2 = self.use2.get_rect(topleft = (207,467))
        self.rect3 = self.use3.get_rect(topleft = (8,534))
        self.rect4 = self.use4.get_rect(topleft = (207,534))
    def blitUse(self):
        self.screen.blit(self.use1, self.rect1)
        self.screen.blit(self.use2, self.rect2)
        self.screen.blit(self.use3, self.rect3)
        self.screen.blit(self.use4, self.rect4)

class Text2():
    def __init__(self,screen):
        self.screen = screen
        self.myFont = pygame.font.SysFont('Comic Sans MS', 20)
        self.use1 = self.myFont.render('Scratch',False,(0,0,0))
        self.use2 = self.myFont.render('Growl',False,(0,0,0))
        self.use3 = self.myFont.render('Vine Whip',False,(0,0,0))
        self.use4 = self.myFont.render('Tail Whip',False,(0,0,0))
        self.rect1 = self.use1.get_rect(topleft = (8,534))
        self.rect2 = self.use2.get_rect(topleft = (207,467))
        self.rect3 = self.use3.get_rect(topleft = (8,467))
        #self.rect4 = self.use4.get_rect(topleft = (203,534))
    def blitUse(self):
        self.screen.blit(self.use1, self.rect1)
        self.screen.blit(self.use2, self.rect2)
        self.screen.blit(self.use3, self.rect3)
        #self.screen.blit(self.use4, self.rect4)

class Provoke():
    def __init__(self,screen):
        self.screen = screen
        self.myFont = pygame.font.SysFont('Comic Sans MS', 30)
        self.text = self.myFont.render('This is a punching bag game',False,(0,0,0))
        self.pos = self.text.get_rect(topleft = (8,367))
    def blitUse(self):
        self.screen.blit(self.text, self.pos)

class HP_BAR():
    def __init__(self,hp,screen):
        self.screen = screen
        self.myFont = pygame.font.SysFont('Comic Sans MS', 30)
        self.hape = hp
    def blitUse(self):
        self.health = self.myFont.render('HP L ' + str(self.hape) ,False,(0,0,0))
        self.hpos = self.health.get_rect(topleft = (50,0))
        self.screen.blit(self.health,self.hpos)
    def updateHP(self,HP):
        self.hape = HP
