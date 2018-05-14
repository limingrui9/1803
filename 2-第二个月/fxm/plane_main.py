import pygame
from plant_sprites import *
from pygame.locals import *
from sys import exit
from pygame.font import *

class PlantGame:
    def __init__(self):

        self.life1 = 3
        self.score1 = 0
        self.life2 = 3
        self.score2 = 0

        self.speed_hero = 3
        self.speed_bg1 = 4
        pygame.init()
        pygame.display.set_caption("飞机大战")
        self.jiantou = './images/jianTou.png'
        self.mouse_cursor = pygame.image.load(self.jiantou)

        pygame.time.set_timer(CREATE_ENEMY_EVENT, 200)
        pygame.time.set_timer(BUTTER_FUJI_EVENT, 200)

        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()

        self.__create_sprites()
        self.key_pressed = None

        self.my_if = False
        self.my_if1 = False
        self.fuji1_L_if = False
        self.fuji1_R_if = False
        self.fuji2_L_if = False
        self.fuji2_R_if = False
        self.enemy_if = False

        self.bigin_if = False
        self.win_if = True




        # #音乐
        # pygame.mixer.init()
        # pygame.mixer.music.load("./a2.mp3")
        # pygame.mixer.music.play()





    def __create_sprites(self):
        self.bg1 = Background()
        self.bg2 = Background(True)
        self.bg3 = Background(True,True)
        # self.bg2 = Background(True)

        self.hero = Hero(1,'./images/me1.png')
        self.hero1 = Hero(1,'./images/me1.png')
        self.hero.rect.x = 600
        self.hero.rect.y = 500

        self.hero1.rect.x = 100
        self.hero1.rect.y = 500
        self.enemy = Enemy()

        self.fuji1_L = Fuji(1,'./images/life.png')
        self.fuji1_R = Fuji(1,'./images/life.png')

        self.fuji2_L = Fuji(1,'./images/life.png')
        self.fuji2_R = Fuji(1,'./images/life.png')

        self.back_group = pygame.sprite.Group(self.bg1,self.bg2,self.bg3)
        self.enemy_group = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group(self.hero,self.hero1)

        self.hero_bullte_group = pygame.sprite.Group()
        self.hero_bullte1_group = pygame.sprite.Group()

        self.fuji_group = pygame.sprite.Group(self.fuji1_L , self.fuji1_R, self.fuji2_L , self.fuji2_R)

        self.buttons = button("./images/again.png", "./images/again_down.png", (SCREEN_RECT.width/2,SCREEN_RECT.height/2))
        self.buttons_bigin = button("./images/buttons_bigin_up.png", "./images/buttons_bigin_down.png", (SCREEN_RECT.width/2,SCREEN_RECT.height/2))

        self.bg_bigin = pygame.image.load("./images/bg_bigin.png")
    def start_game(self):

        while True:
            # x -= self.mouse_cursor.get_width() / 2
            # y -= self.mouse_cursor.get_height() / 2
            self.clock.tick(60)
            x,y = pygame.mouse.get_pos()
            self.screen.blit(self.mouse_cursor,(x,y))
            self.__event_handler()

            if self.score1 + self.score2 > 100:
                self.screen.blit(self.bg_bigin,(0,0))
                self.show_win()
                self.win_if = False
                self.buttons.render(self.screen)
                pygame.display.update()

            if not self.bigin_if:
                self.screen.blit(self.bg_bigin,(0,0))
                self.buttons_bigin.render(self.screen)
                pygame.display.update()

            # if not self.win_if:
            #     self.show_win()
            #     pygame.display.update()


            if self.bigin_if and self.win_if:
                self.__update_sprites()
                self.__check_colide()
                self.show_life()
                pygame.display.update()



    def __event_handler(self):
        #事件监听

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            if self.buttons_bigin.mouse_if:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.bigin_if = True





            if self.bigin_if:
                if event.type == CREATE_ENEMY_EVENT:
                    self.enemy = Enemy()
                    self.enemy_group.add(self.enemy)

                #key
                self.key_perssed = pygame.key.get_pressed()


                if self.key_perssed[pygame.K_RIGHT]:
                    self.hero.speed[0] = self.speed_hero
                    # self.bg1.speed[0] = -self.speed_bg1
                    # self.enemy.speed[0] = self.speed_bg1

                elif self.key_perssed[pygame.K_LEFT]:
                    self.hero.speed[0] = -self.speed_hero
                    # self.bg1.speed[0] = self.speed_bg1
                    # self.enemy.speed[0] = -self.speed_bg1

                elif self.key_perssed[pygame.K_UP]:
                    self.hero.speed[1] = -self.speed_hero
                    # self.bg1.speed[1] = self.speed_bg1
                    # self.enemy.speed[1] = self.speed_bg1

                elif self.key_perssed[pygame.K_DOWN]:
                    self.hero.speed[1] = self.speed_hero
                    # self.bg1.speed[1] = -self.speed_bg1
                    # self.enemy.speed[1] = -self.speed_bg1
                else:
                    self.hero.speed = [0,0]
                    # self.bg1.speed = [0,0]
                    # self.enemy.speed = [0,0]

                if self.key_perssed[pygame.K_KP1] and not self.my_if:
                    for i in (1,2,3):
                        self.hero_bullte_group.add(Blluet(self.hero.rect.x + self.hero.L_arms_x,(self.hero.rect.y + self.hero.L_arms_y)-20*i))
                        self.hero_bullte_group.add(Blluet(self.hero.rect.right + self.hero.R_arms_x,(self.hero.rect.y + self.hero.R_arms_y)-20*i))




                if self.key_perssed[pygame.K_d]:
                    self.hero1.speed[0] = self.speed_hero
                    # self.bg1.speed[0] = -self.speed_bg1
                    # self.enemy.speed[0] = self.speed_bg1

                elif self.key_perssed[pygame.K_a]:
                    self.hero1.speed[0] = -self.speed_hero
                    # self.bg1.speed[0] = self.speed_bg1
                    # self.enemy.speed[0] = -self.speed_bg1

                elif self.key_perssed[pygame.K_w]:
                    self.hero1.speed[1] = -self.speed_hero
                    # self.bg1.speed[1] = self.speed_bg1
                    # self.enemy.speed[1] = self.speed_bg1

                elif self.key_perssed[pygame.K_s]:
                    self.hero1.speed[1] = self.speed_hero
                    # self.bg1.speed[1] = -self.speed_bg1
                    # self.enemy.speed[1] = -self.speed_bg1
                else:
                    self.hero1.speed = [0,0]
                    # self.bg1.speed = [0,0]
                    # self.enemy.speed = [0,0]

                if self.key_perssed[pygame.K_j] and not self.my_if1:
                    for i in (1,2,3):
                        self.hero_bullte1_group.add(Blluet1(self.hero1.rect.x + self.hero1.L_arms_x,(self.hero1.rect.y + self.hero1.L_arms_y)-20*i))
                        self.hero_bullte1_group.add(Blluet1(self.hero1.rect.right + self.hero1.R_arms_x,(self.hero1.rect.y + self.hero1.R_arms_y)-20*i))

                if event.type == BUTTER_FUJI_EVENT and not self.my_if and not self.fuji1_L_if:
                    self.hero_bullte_group.add(Blluet(self.fuji1_L.rect.x + self.fuji1_L.L_arms_x,(self.fuji1_L.rect.y + self.fuji1_L.L_arms_y)-20))
                    self.hero_bullte_group.add(Blluet(self.fuji1_L.rect.right + self.fuji1_L.R_arms_x,(self.fuji1_L.rect.y + self.fuji1_L.R_arms_y)-20))

                if event.type == BUTTER_FUJI_EVENT and not self.my_if and not self.fuji1_R_if:
                    self.hero_bullte_group.add(Blluet(self.fuji1_R.rect.x + self.fuji1_R.L_arms_x,(self.fuji1_R.rect.y + self.fuji1_R.L_arms_y)-20))
                    self.hero_bullte_group.add(Blluet(self.fuji1_R.rect.right + self.fuji1_R.R_arms_x,(self.fuji1_R.rect.y + self.fuji1_R.R_arms_y)-20))

                if event.type == BUTTER_FUJI_EVENT and not self.my_if1 and not self.fuji2_L_if:
                    self.hero_bullte1_group.add(Blluet1(self.fuji2_L.rect.x + self.fuji2_L.L_arms_x,(self.fuji2_L.rect.y + self.fuji2_L.L_arms_y)-20))
                    self.hero_bullte1_group.add(Blluet1(self.fuji2_L.rect.right + self.fuji2_L.R_arms_x,(self.fuji2_L.rect.y + self.fuji2_L.R_arms_y)-20))

                if event.type == BUTTER_FUJI_EVENT and not self.my_if1 and not self.fuji2_R_if:
                    self.hero_bullte1_group.add(Blluet1(self.fuji2_R.rect.x + self.fuji2_R.L_arms_x,(self.fuji2_R.rect.y + self.fuji2_R.L_arms_y)-20))
                    self.hero_bullte1_group.add(Blluet1(self.fuji2_R.rect.right + self.fuji2_R.R_arms_x,(self.fuji2_R.rect.y + self.fuji2_R.R_arms_y)-20))

                #按钮
                if self.buttons.mouse_if:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.__init__()




    def __check_colide(self):
        #碰撞检测
        enemy_collide = pygame.sprite.groupcollide(self.hero_bullte_group,self.enemy_group,True,True)
        enemy1_collide = pygame.sprite.groupcollide(self.hero_bullte1_group,self.enemy_group,True,True)

        hero_collide = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        hero1_collide = pygame.sprite.spritecollide(self.hero1,self.enemy_group,True)

        fuji1_L_collide = pygame.sprite.spritecollide(self.fuji1_L,self.enemy_group,True)
        fuji1_R_collide = pygame.sprite.spritecollide(self.fuji1_R,self.enemy_group,True)

        fuji2_L_collide = pygame.sprite.spritecollide(self.fuji2_L,self.enemy_group,True)
        fuji2_R_collide = pygame.sprite.spritecollide(self.fuji2_R,self.enemy_group,True)

        if len(enemy_collide):
            self.score2 += 1

        if len(enemy1_collide):
            self.score1 += 1

        if len(hero_collide):
            self.life2 -= 1

            if self.life2 < 1:
                self.hero.kill()
                self.fuji1_L.kill()
                self.fuji1_R.kill()

                self.hero.rect.x = 1000
                self.hero.rect.y = 1000

                self.my_if = True

        if len(hero1_collide):
            self.life1 -= 1
            if self.life1 < 1:
                self.hero1.kill()
                self.fuji2_L.kill()
                self.fuji2_R.kill()

                self.hero1.rect.x = 1000
                self.hero1.rect.y = 1000

                self.my_if1 = True

        if len(fuji1_L_collide):
            self.fuji1_L.kill()
            self.fuji1_L.rect.x = 1000
            self.fuji1_L.rect.y = 1000
            self.fuji1_L_if = True

        if len(fuji1_R_collide):
            self.fuji1_R.kill()
            self.fuji1_R.rect.x = 1000
            self.fuji1_R.rect.y = 1000
            self.fuji1_R_if = True

        if len(fuji2_L_collide):
            self.fuji2_L.kill()
            self.fuji2_L.rect.x = 1000
            self.fuji2_L.rect.y = 1000
            self.fuji2_L_if = True

        if len(fuji2_R_collide):
            self.fuji2_R.kill()
            self.fuji2_R.rect.x = 1000
            self.fuji2_R.rect.y = 1000
            self.fuji2_R_if = True



    def __update_sprites(self):
        #更新精灵族
        for group in [self.back_group, self.hero_group ,self.hero_bullte_group,self.hero_bullte1_group,self.fuji_group]:
            group.update()
            group.draw(self.screen)
        self.enemy_group.update(self.bg1)
        self.enemy_group.draw(self.screen)

        self.fuji1_L.pos(self.hero.rect.x - 10, self.hero.rect.bottom + 20)
        self.fuji1_R.pos(self.hero.rect.right + 10, self.hero.rect.bottom + 20)

        self.fuji2_L.pos(self.hero1.rect.x - 10, self.hero1.rect.bottom + 20)
        self.fuji2_R.pos(self.hero1.rect.right + 10, self.hero1.rect.bottom + 20)

        if self.my_if and self.my_if1:
            self.buttons.render(self.screen)






    def __game_over(self):
        #游戏结束
        print('游戏结束！')
        pygame.quit()
       


    def show_life(self):
        pygame.font.init()

        pos1_01 = (0,0)
        pos1_02 = (0,30)

        pos2_01 = (400,0)
        pos2_02 = (400,30)

        color1 = (225,10,10)
        color2 = (100,225,10)

        text1_01 = '生命值A:' + str(self.life1)
        text1_02 = '杀敌数A:'+ str(self.score1)
        text2_01 = '生命值B:' + str(self.life2)
        text2_02 = '杀敌数B:' + str(self.score2)

        cur_font = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 30)

        text_fmt1_01= cur_font.render(text1_01,1,color1)
        text_fmt1_02 = cur_font.render(text1_02,1,color1)
        text_fmt2_01 = cur_font.render(text2_01,1,color2)
        text_fmt2_02 = cur_font.render(text2_02,1,color2)

        self.screen.blit(text_fmt1_01,pos1_01)
        self.screen.blit(text_fmt1_02,pos1_02)
        self.screen.blit(text_fmt2_01,pos2_01)
        self.screen.blit(text_fmt2_02,pos2_02)


    def show_win(self):
        pygame.font.init()

        pos1_01 = (SCREEN_RECT.width/2 - 250,SCREEN_RECT.height/2 - 200)

        color1 = (100,225,10)

        text1_01 = "恭喜你赢了，你们一共打了：" + str(self.score1 + self.score2) + "个敌人."

        cur_font = pygame.font.Font('C:/Windows/Fonts/simhei.ttf', 30)

        text_fmt1_01= cur_font.render(text1_01,1,color1)

        self.screen.blit(text_fmt1_01,pos1_01)





class button(object):

    def __init__(self, upimage, downimage,position):
        self.imageUp = pygame.image.load(upimage)
        self.imageDown = pygame.image.load(downimage)
        self.position = position 
        self.mouse_if = False

    def isOver(self):
        point_x,point_y = pygame.mouse.get_pos()
        x, y = self. position
        w, h = self.imageUp.get_size()

        in_x = x - w/2 < point_x < x + w/2
        in_y = y - h/2 < point_y < y + h/2
        return in_x and in_y

    def render(self,screen):
        w, h = self.imageUp.get_size()
        x, y = self.position

        if self.isOver():
            screen.blit(self.imageDown, (x-w/2,y-h/2))
            self.mouse_if = True
        else:
            screen.blit(self.imageUp, (x-w/2, y-h/2))
            self.mouse_if = False


start_game = PlantGame()
start_game.start_game()