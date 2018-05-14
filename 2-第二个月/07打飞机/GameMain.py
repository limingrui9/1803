import pygame
from PlanSprite import *
class PlanGame(object):
	#初始化
	def __init__(self):
		print("游戏初始化")
		#创建窗口
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		#创建时钟对象
		self.clock = pygame.time.Clock()

		self.__create_sprite()
	#开始游戏
	def startGame(self):
		print("开始游戏")	
		while True:
			self.clock.tick(60)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()

			pygame.display.update()
			pass


	#创建精灵或精灵组
	def __create_sprite(self):
		pass

	#事件监听
	def __event_handler(self):
		pass

	#碰撞检测

	def __check_collide(self):
		pass

	#更新精灵组
	def __update_sprites(self):
		pass

	def __game_over(self):
		print("游戏结束")	
		pygame.quit()
		exit()	


if __name__ == '__main__':
	plangame = PlanGame()
	plangame.startGame()