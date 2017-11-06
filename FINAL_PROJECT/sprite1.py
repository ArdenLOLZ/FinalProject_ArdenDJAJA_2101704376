import pygame
from BaseMove import *
from Bulbasaur import *
from Squirtle import *
class Squirtle():
    def __init__(self,screen):
        self.Type = 'Water'
        self.HP = 80
        self.Speed = 10
        self.screen = screen
        self.imageBack = pygame.image.load('image/squirtleBack.png')
        self.imageFront = pygame.image.load('image/squirtleFront.png')
        self.rectBot = self.imageBack.get_rect(topleft=(0,195))
        self.rectUp = self.imageFront.get_rect(topleft=(225,0))
        self.screen_rect = screen.get_rect()
        self.skills = [Tackle, Growl, WaterGun, TailWhip]
    def blitme(self,booli):
        if booli==True:
            self.screen.blit(self.imageBack,self.rectBot)
        elif booli == False:
            self.screen.blit(self.imageFront,self.rectUp)



    def showHP(self):
        return self.HP
class Bulbasaur():
    def __init__(self,screen):
        self.Type = 'grass'
        self.HP = 60
        self.Speed = 12
        self.screen = screen
        self.imageBack = pygame.image.load('image/bulbasaurBack.png')
        self.imageFront = pygame.image.load('image/bulbasaurFront.png')
        self.rectBot = self.imageBack.get_rect(topleft=(0,195))
        self.rectUp = self.imageFront.get_rect(topleft=(225,0))
        self.screen_rect = screen.get_rect()
        self.skills = [Scratch, Growl, VineWhip, TailWhip]
    def blitme(self,booli):
        if booli==True:
            self.screen.blit(self.imageBack,self.rectBot)
        elif booli == False:
            self.screen.blit(self.imageFront,self.rectUp)
    def takeDamage(self,skill):
        self.HP -= skill

