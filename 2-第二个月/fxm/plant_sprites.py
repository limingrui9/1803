import pygame
import random

SCREEN_RECT = pygame.Rect(0,0,790,800)
CREATE_ENEMY_EVENT = pygame.USEREVENT
BUTTER_FUJI_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed = 1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
    
    def update(self,*arge):
        self.rect.y += self.speed
       

class Background(GameSprite):
    def __init__(self,is_alt = False,is_alt1 = False):

        self.image_name = "./images/背景.png"
        super().__init__(self.image_name) 
        self.rect.x = -6
        self.speed = [0,0]
        if is_alt:
            self.rect.y = -self.rect.height
        if is_alt1:
            self.rect.y = -2*self.rect.height
    def update(self):
        self.rect.y += 1
        self.rect.x += 0

        #super().update()

        if self.rect.y >= self.rect.height:
            self.rect.y = -self.rect.height




class Hero(GameSprite):

    def __init__(self,hero_size, *arge):
        self.coefficient = hero_size

        super().__init__(arge[0])
        self.lock = False
        self.speed = [0,0]

        self.L_arms_x = 15 * self.coefficient
        self.L_arms_y = 40 * self.coefficient
        self.R_arms_x = -15 * self.coefficient
        self.R_arms_y = 40 * self.coefficient

        self.rect.center = SCREEN_RECT.center



        #self.rect.width *= self.coefficient
        #self.rect.height *= self.coefficient

        # self.rect.width = 100

    def update(self,*arge):

        self.rect.y += self.speed[1]
        self.rect.x += self.speed[0]

        #出界
        if self.rect.x <= 0:
            self.rect.x = 0

        if self.rect.x + self.rect.width >= SCREEN_RECT.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width

        if self.rect.y <= 0:
            self.rect.y = 0

        if self.rect.y + self.rect.height >= SCREEN_RECT.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height


class Enemy(GameSprite):

    def __init__(self,count = 0):
        self.image_name = "./images/enemy1.png"

        super().__init__(self.image_name)
        self.lock = False
        self.x = count
        self.y = random.randint(1,3)
        self.rect.bottom = 0
        self.speed = [0,0]

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)


        
    def update(self,*arge):

        self.rect.y += 2
        self.rect.x += self.speed[0]

        #出界
        if self.rect.x <= SCREEN_RECT.x:
            self.rect.x = 0

        if self.rect.x + self.rect.width >= SCREEN_RECT.right:
           self.rect.x = SCREEN_RECT.right

        if self.rect.y <= SCREEN_RECT.y:
            self.rect.y = 0

        if self.rect.y >= SCREEN_RECT.bottom:
            self.kill()

    def __del__(self):
        pass


class Blluet(GameSprite):
    def __init__(self,x=0,y=0):
        self.image_name = "./images/bullet1.png"
        super().__init__(self.image_name)

        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.y -= 15

        if self.rect.y <= 0:
            self.kill()

class Blluet1(Blluet):
    pass
    # def __init__(self,x=0,y=0):
    #     super().__init__(x,y)

class Fuji(Hero):
    def pos(self,x,y):
        self.rect.centerx = x
        self.rect.centery = y