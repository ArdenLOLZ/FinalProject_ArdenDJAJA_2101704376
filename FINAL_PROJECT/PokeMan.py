import sys
import time
import pygame
from game_fuction import *
from seting import Settings
from sprite1 import *
from Choice import *
from text import *
from BaseMove import *

def Pokefite():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    poke1 = Squirtle(screen)
    poke2 = Bulbasaur(screen)
    choice = Button(screen)
    select = Select(screen)
    option1 = Text1(screen)
    useless_text = Provoke(screen)
    health = HP_BAR(poke2.HP,screen)
    pygame.mouse.set_visible(False)
    pygame.display.set_caption('Test fight')
    bg = pygame.image.load(ai_settings.bg)
    while True:

        screen.blit(bg,[0,0])
        choice.blitme()
        select.blitUpdate()
        option1.blitUse()
        useless_text.blitUse()
        health.updateHP(poke2.HP)
        health.blitUse()
        poke1.blitme(True)
        poke2.blitme(False)
        check_events(select,choice,poke1,poke2,health)
        pygame.display.flip()
Pokefite()
