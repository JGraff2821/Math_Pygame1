import random
import os, sys
import pygame
from pygame.locals import *


class Picture:
    random.seed()
    def __init__(self, rel_path: str, x_cord: int, y_cord: int, ID =0, length=300,width=300, ):
        self.image = pygame.image.load(self.create_abs_file_path(rel_path))
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.selected = False
        self.length = length
        self.width = width
        self.scale_image(length, width)
        self.EffectNumber = random.randint(0,10)
        self.EffectID = ID

    @staticmethod
    def create_abs_file_path(rel_path):
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, rel_path)
        return abs_file_path

    def scale_image(self, length: int, width: int):
        self.image = pygame.transform.scale(self.image, (length, width))
        self.length = length
        self.width = width

    def coordInArea(self, coord:list):
        x = self.x_cord
        y = self.y_cord
        a = self.length
        b = self.width
        v = coord[0]
        w = coord[1]
        if x<=v<=x+a and y<w<y+b :
            return True
        return False



class ActionPicture(Picture):
    # random.seed()
    EffectKey:int
    # EffectNumber = random.randint(0, 10)



