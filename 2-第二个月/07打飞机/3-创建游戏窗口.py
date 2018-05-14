import pygame.display
pygame.display.set_mode()

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

pygame.display.update()

i = 0
while True:
	clock.tick(60)
	hero_rect.y -=1
	screen.blit(bj,(0,0))
	screen.blit(fj,hero_rect)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	pygame.display.update()

pygame.quit()