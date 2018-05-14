import pygame
pygame.init()

hero_rect = pygame.Rect(100,500,120,120)
print('坐标原点%d %d'%(hero_rect.x, hero_rect.y))
print("英雄大小%d %d"%(hero_rect.width, hero_rect.height))
print("英雄大小%d %d"%hero_rect.size)