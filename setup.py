import pygame as pg
from settings import *

pygame.init()

# 设置分辨率 
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

# 控制两个挡板移动
MOVEDICT = {K_LEFT:0, K_RIGHT:0}

# 控制游戏窗口结束
CLOSEWINDOW = False

# 游戏窗口标题
pg.display.set_caption("PinBall")
