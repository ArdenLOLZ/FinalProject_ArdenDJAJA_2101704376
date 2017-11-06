import pygame
import sys
import os
position3 = (2,533)
position2 = (201,466)
position1 = (2,466)
position4 = (201,533)
class Button():
    def __init__(self,screen):
        self.button = pygame.image.load('image/button.png')
        self.screen = screen
        self.rect1 = self.button.get_rect(topleft = position1)
        self.rect2 = self.button.get_rect(topleft = position2)
        self.rect3 = self.button.get_rect(topleft = position3)
        self.rect4 = self.button.get_rect(topleft = position4)


    def blitme(self):
        self.screen.blit(self.button, self.rect1)
        self.screen.blit(self.button, self.rect2)
        self.screen.blit(self.button, self.rect3)
        self.screen.blit(self.button, self.rect4)
class Select():
    def __init__(self,screen):
        self.select = pygame.image.load('image/select.png')
        self.screen = screen
        self.serect = self.select.get_rect(topleft = position1)
    def blitUpdate(self):
        self.screen.blit(self.select, self.serect)
