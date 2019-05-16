from settings import *
import pygame

# 挡板类
class Baffle(object):
    
    def __init__(self, form='./res/baffle/ballfeDefault.png',
                 height=BAFFLEHEIGHT, width=BAFFLEWIDTH, speed=BAFFLESPEED):
        
        # 设置挡板的样式
        self.form = pygame.image.load(form).convert_alpha()

        # 挡板的初始位置
        self.posX = 0
        self.posY = 0

        # 挡板的高度和宽度
        self.height = height
        self.width = width

        # 挡板的速度
        self.speed = speed

    def show(self, screen):
        
        screen.blit(self.form, (self.posX, self.posY))

    def move(self, offsetX):
        
        self.posX += offsetX  
        self.posX = max(0, self.posX)
        self.posX = min(SCREENWIDTH - self.width, self.posX)

    # 需要重定义
    def reset(self):
        pass

class UpBaffle(Baffle):

    def reset(self):

        # 挡板的初始位置
        self.posX = SCREENWIDTH // 2 - self.width // 2
        self.posY = 0

class DownBaffle(Baffle):

    def reset(self):

        # 下挡板的初始位置
        self.posX = SCREENWIDTH // 2 - self.width // 2
        self.posY = SCREENHEIGHT - self.height