import sys
import pygame
import random

class Skill():
    def __init__(self,power,accuracy,element,name):
        self.element = element
        self.power = power
        self.accuracy = accuracy
        self.name = name
Tackle = Skill(20,95,'normal','Tackle')
Growl = Skill(0,0,'normal','Growl')
WaterGun = Skill(30, 80, 'Water', 'Water Gun')
TailWhip = Skill(0,0,'normal','Tail Whip')
VineWhip = Skill(30, 80, 'Grass', 'Vine Whip')
Scratch = Skill(15,95,'normal', 'Scratch')
