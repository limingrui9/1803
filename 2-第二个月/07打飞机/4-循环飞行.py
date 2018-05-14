import pygame
from PlanSprite import *
pygame.init()
#pygame.display.set_mode()

screen = pygame.display.set_mode((480,700))
#创建背景图片
bj=pygame.image.load("./images/background.png")
screen.blit(bj,(0,0))

#创建飞机图片
fj = pygame.image.load("./images/hero.gif")
screen.blit(fj,(180,500))
#设置时钟
clock = pygame.time.Clock()
#创建飞机的rect
hero_rect = pygame.Rect(180,500,200,200)
#screen.blit(hero,(180,500))
#创建敌机精灵
enemy = GameSprite("./images/enem1.png")
enemy = GameSprite("./images/enemy1.png")
enem1.rect.x = 100
#创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)

#pygame.display.update()


while True:
	clock.tick(60)
	hero_rect.y -=1
	#覆盖背景
	screen.blit(bj,(0,0))
	screen.blit(fj,hero_rect)
	if hero_rect.y + hero_rect.height <= 0:
		hero_rect.y = 700		

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	enemy_group.update()
	enemy_group.draw(screen)
	pygame.display.update()

pygame.quit()