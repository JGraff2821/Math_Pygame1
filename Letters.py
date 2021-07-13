import pygame
import random
from pygame.locals import *

class Letters:
    def __init__(self,font, size: int, message: str, color, background_color, x_value, y_value ):
        print("Using Letters Initalizer")
        self.size = size
        self.message = message
        self.color = color
        self.x=x_value
        self.y =y_value
        self.background_color =background_color
        print("fontsetter with: ",font,size)
        self.fontsetter = pygame.font.SysFont(font,size)
        self.MessageSurface = self.fontsetter.render(message,False,color, background_color)
        self.selected = False

    def refresh(self):
        self.MessageSurface = self.fontsetter.render(self.message,False, self.color, self.background_color)
    def coordInArea(self, coord:list):
        x = self.x
        y = self.y
        a = 30
        b = 30
        v = coord[0]
        w = coord[1]
        if x<=v<=x+a and y<w<y+b :
            self.selected =True
            return True
        return False


class NumberLetter(Letters):
    random.seed()
    rand_floor: int = 0
    rand_cap: int = 50
    def __int__(self):
        self.number = random.randint(0, 10)
        self.background_color = (255, 100, 0)
        self.message = " "+str(self.number)+" "
        print("number refreshed")
        self.refresh()
    def is_target_number(self):
        self.number = random.randint(0,100)
        self.message = " " + str(self.number) + " "
        self.refresh()
    def add_number(self, new_number):
        self.number += new_number
        self.message = " "+str(self.number)+" "
        self.refresh()

    def sub_number(self, new_number):
        self.number -= new_number
        self.message = " " + str(self.number) + " "
        self.refresh()

    def mult_number(self, new_number):
        self.number *= new_number
        self.message = " " + str(self.number) + " "
        self.refresh()

    def divide_number(self, new_number):
        self.number /= new_number
        self.message = " " + str(self.number) + " "
        self.refresh()

    def mod_number(self, new_number):
        self.number %= new_number
        self.message = " " + str(self.number) + " "
        self.refresh()




