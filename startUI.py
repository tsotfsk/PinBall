import pygame as pg
import setup
from Button import *

def startUI():

    # 开始界面
    startImage = pygame.image.load('./res/picture/others/startImage.jpeg').convert()
    screen.blit(startImage, (0, 0))

    # 单人开始按钮
    singleButton = Button("./image/singleButton.png", "./image/singleButton.png")
    singleButton.move(SCREENWIDTH // 2 - singleButton.width // 2, SCREENHEIGHT // 2 - 4 * singleButton.height)
    singleButton.show(setup.SCREEN)  

    # 双人开始按钮
    doubleButton = Button("./image/doubleButton.png", "./image/doubleButton.png")
    doubleButton.move(SCREENWIDTH // 2 - doubleButton.width // 2, SCREENHEIGHT // 2 - 2 * doubleButton.height)
    doubleButton.show(setup.SCREEN)     

    # 联机开始按钮
    onlineButton = Button("./image/onlineButton.png", "./image/onlineButton.png")
    onlineButton.move(SCREENWIDTH // 2 - onlineButton.width // 2, SCREENHEIGHT // 2)
    onlineButton.show(setup.SCREEN) 

    # 设置按钮
    settingButton = Button("./image/settingButton.png", "./image/settingButton.png")
    settingButton.move(SCREENWIDTH // 2 - settingButton.width // 2, SCREENHEIGHT // 2 + 2 * settingButton.height)
    settingButton.show(setup.SCREEN)

    # 结束按钮
    closeButton = Button("./image/closeButton.png", "./image/closeButton.png")
    closeButton.move(SCREENWIDTH // 2 - closeButton.width // 2, SCREENHEIGHT // 2 + 4 * closeButton.height)
    closeButton.show(setup.SCREEN)

    pg.display.update()


def start():  
    while not setup.CLOSEWINDOW:
        for event in pygame.event.get():
            if event.type == QUIT:
                closeWindow = True
            if event.type == MOUSEBUTTONDOWN:
                if singleButton.isOver():  # 单人游戏
                    return 0
                if doubleButton.isOver():  # 双人游戏
                    return 1
                if onlineButton.isOver():  # 联机游戏
                    return 2
                if settingButton.isOver():  # 设置按钮
                    return 3
                if closeButton.isOver():  # 关闭按钮
                    return 4