import sys
import pygame
from sprite1 import *
from text import *
from Squirtle import *
from Bulbasaur import *
import time
from Choice import *
position3 = (2,533)
position2 = (201,466)
position1 = (2,466)
position4 = (201,533)

def check_events(select,button,poke1,poke2,health):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif health.hape < 1:
            layar = pygame.display.set_mode((1170,650))
            closing = pygame.image.load('image/Untitled.png')
            layar.blit(closing,(0,0))
            pygame.display.flip()
            time.sleep(3)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if select.serect == button.rect1:
                    select.serect = button.rect2
                elif select.serect == button.rect2:
                   select.serect = button.rect3
                elif select.serect == button.rect3:
                    select.serect = button.rect4
                elif select.serect == button.rect4:
                    select.serect = button.rect1

            elif event.key == pygame.K_LEFT:
                if select.serect == button.rect2:
                    select.serect = button.rect1
                elif select.serect == button.rect3:
                    select.serect = button.rect2
                elif select.serect == button.rect4:
                    select.serect = button.rect3
                elif select.serect == button.rect1:
                    select.serect = button.rect4

            elif event.key == pygame.K_RETURN:
                if select.serect == button.rect2:
                    poke2.takeDamage(poke1.skills[1].power)
                elif select.serect == button.rect3:
                    poke2.takeDamage(poke1.skills[2].power)
                elif select.serect == button.rect4:
                    poke2.takeDamage(poke1.skills[3].power)
                elif select.serect == button.rect1:
                    poke2.takeDamage(poke1.skills[0].power)
                health.hape = poke2.HP

