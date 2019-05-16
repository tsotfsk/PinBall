import pygame

class Button(object):

    def __init__(self, uImage, dImage):

        # 载入图片获取按钮位置
        self.uImage = pygame.image.load(uImage).convert_alpha()
        self.dImage = pygame.image.load(dImage).convert_alpha()
        self.posX, self.posY = 0, 0
        self.width, self.height = self.uImage.get_size()

    #按钮定位
    def move(self, x, y):

        self.posX = x
        self.posY = y

    #鼠标是否在按钮上
    def isOver(self):

        mouseX,mouseY = pygame.mouse.get_pos()
        inX = self.posX < mouseX < self.posX + self.width
        inY = self.posY < mouseY < self.posY + self.height
        return inX and inY

    #控制鼠标移动按钮的显示
    def show(self, screen): 

        if self.isOver():
            screen.blit(self.dImage, (self.posX,self.posY))
        else:
            screen.blit(self.uImage, (self.posX,self.posY))
