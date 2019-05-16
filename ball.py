from settings import *
import pygame
import random
import time

# 弹珠
class Ball(object):
    
    def __init__ (self, form='./res/picture/ball/pokeball.png', size=BALLSIZE): 

        # 默认设置球的样式为pokeball
        self.form = pygame.image.load(form).convert_alpha()

        # 设置球的尺寸
        self.size = size

        # 初始化球的随机种子
        self.seed = int(time.time()) % 10000

        #初始球的速度和方向
        self.randomPos()
        self.randomSpeed()

    def show(self, screen):
        # 绘制一个球
        screen.blit(self.form, (self.posX, self.posY, self.size, self.size))

    def move(self, offsetX, offsetY):

        self.posX = self.posX + offsetX
        if self.posX < 0:  # 球打到左边界
            self.posX = 0
            self.speedX = -self.speedX
        elif self.posX > SCREENWIDTH - self.size:  # 球打到右边界
            self.posX = SCREENWIDTH - self.size
            self.speedX = -self.speedX 

        self.posY = self.posY + offsetY

    def reset(self):

        # 球位置的随机
        self.randomPos()
        # 设置弹珠弹速随机
        self.randomSpeed()

    # 碰撞检测
    def collisionDetection(self, baffle):

        if self.posX + self.size  > baffle.posX and self.posX < baffle.posX + baffle.width: # 横坐标在下挡板范围内
            if baffle.name == 'down':
                if self.posY + self.size > baffle.posY:  # 纵坐标在下挡板可接受范围内
                    self.posY = SCREENHEIGHT - self.size - baffle.height
                    self.speedY = -self.speedY
            if baffle.name == 'up':
                if baffle.posY + baffle.height > self.posY:  # 纵坐标在上挡板氪接受范围内
                    self.posY = baffle.posY + baffle.height
                    self.speedY = -self.speedY

    # 随机的球速
    def randomSpeed(self):
        "随机产生球的X与Y方向上的速度, 范围是[150, 300] ∪ [-300, -150]"

        # x方向速度随机
        random.seed(self.seed)
        self.speedX = random.randint(150, 300)
        self.seed -=10

        # y方向速度随机
        random.seed(self.seed)
        self.speedY = random.randint(150, 300)
        self.seed -=10 

        # 方向与随机的速度有关，其本质也是随机的
        if self.speedX % 2 == 0:
            self.speedX = -self.speedX

        if self.speedY % 2 == 0:
            self.speedY = -self.speedY

    def randomPos(self):

        random.seed(self.seed)
        self.posX = random.randint(0, SCREENWIDTH - self.size)
        self.seed -= 10  # 第二个种子是第一个种子随机产生的结果

        random.seed(self.seed)
        self.posY = random.randint(SCREENHEIGHT // 3, SCREENHEIGHT // 1.5)
        self.seed -= 10  # 新的备用随机种子

    # 球体样式选择
    def setForm(self, ballType):

        self.form = pygame.image.load(BALLFORMLIST[ballType]).convert_alpha()
