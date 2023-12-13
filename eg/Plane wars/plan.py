import pygame # 引用第三方模块
from pygame.locals import *
import time
import random
'''
1. 实现飞机的显示，并且可以控制飞机的移动
'''
class HeroPlan:
    def __init__(self, screen):
        '''初始化函数
        :param screen :主窗体函数
        '''
        #设置飞机的默认位置
        self.x = 400
        self.y = 470
        # 设置要显示内容的窗口
        self.screen = screen
        #载入飞机图片
        self.imageName = 'D:\python\python\python\eg\Plane wars\plan\英雄飞机.png'
        self.image = pygame.image.load(self.imageName)
        #存放子弹列表
        self.bulletList = []
        pass
    def moveleft(self):
        '''相左移动'''
        if self.x > 0:
            self.x -= 10
        pass
    def moveright(self):
        '''向右移动'''
        if self.x < 870:
            self.x += 10
        pass
    def display(self):
        '''飞机在窗口中的显示
        :return
        '''
        self.screen.blit(self.image, (self.x, self.y))
        #子弹展示逻辑
        nendDelItemList = []
        for item in self.bulletList:
            if item.judge():
                nendDelItemList.append(item)
        #重新遍历
        for i in nendDelItemList:
            self.bulletList.remove(i)
        for bullet in self.bulletList:
            #显示子弹位置
            bullet.display()
            #子弹移动，下一次显示子弹修改后的位置
            bullet.move()
    def launchBullet(self):
        #创建一个子弹对象
        newBullet = Bullet(self.x,self.y,self.screen)
        self.bulletList.append(newBullet)
# 载入玩家飞机图片
'''
  创建子弹类
'''
class Bullet:
    def __init__(self, x, y, screen):
        '''
        子弹位置
        '''
        self.x = x +13
        self.y = y -20
        self.screen = screen
        self.image = pygame.image.load('D:\python\python\python\eg\Plane wars\plan\英雄武器.png')
    def display(self):
        self.screen.blit(self.image,(self.x, self.y))
    def move(self):
        self.y -= 2
    #判断子弹是否越界
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False  
#创建敌机类
class EnemyPlan:
    def __init__(self, screen):
        #默认设置一个方向 左右移动
        self.direction = 'right'
        #敌机默认位置
        self.x = 0
        self.y = 0
        #设置敌机显示内容的窗口
        self.screen = screen
        self.enemybulletlist = []
        #生成敌机图片对象
        self.imageName = 'D:\python\python\python\eg\Plane wars\plan\敌机-最终.png'
        self.image = pygame.image.load(self.imageName)
    def display(self):
        '''显示敌机'''
        #敌机子弹展示逻辑
        nendDelItemList = []
        for item in self.enemybulletlist:
            if item.judge():
                nendDelItemList.append(item)
        #重新遍历
        for i in nendDelItemList:
            self.enemybulletlist.remove(i)
        for bullet in self.enemybulletlist:
            #显示子弹位置
            bullet.display()
            #子弹移动，下一次显示子弹修改后的位置
            bullet.move()
        self.screen.blit(self.image,(self.x, self.y))
    def launchEnemyBullet(self):
        '''显示敌机随机发射子弹'''
        num = random.randint(1,20)
        if num == 3:
            newenemybullet = EnemyBullet(self.x, self.y, self.screen)
            self.enemybulletlist.append((newenemybullet))
    def move(self):
        '''敌机随机移动'''
        if self.direction == 'right':
            self.x += 1
        elif self.direction == 'left':
            self.x -= 1
        if self.x > 870:
            self.direction ='left'
        elif self.x<0:
            self.direction = 'right'
#创建敌机子弹类
class EnemyBullet:
    def __init__(self, x, y, screen):
        '''
        子弹位置
        '''
        self.x = x
        self.y = y +10
        self.screen = screen
        self.image = pygame.image.load('D:\python\python\python\eg\Plane wars\plan\敌方子弹.png')
    def display(self):
        self.screen.blit(self.image,(self.x, self.y))
    def move(self):
        self.y += 2
    #判断敌方子弹是否越界
    def judge(self):
        if self.y > 500:
            return True
        else:
            return False 
def key_control(HeroObj):
    '''定义普通函数， 用来控制键盘的检测
    :param HeroPlan :可控制检测的对象
    :return
    '''
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            print('退出')
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('左移')
                HeroObj.moveleft() #调用函数实现左移
            elif event.key == K_d or event.key == K_RIGHT:
                print('右移')
                HeroObj.moveright() #调用函数右移
            elif event.key == K_SPACE:
                print('空格')
                HeroObj.launchBullet()
        # 更新显示内容
hero = pygame.image.load('D:\python\python\python\eg\Plane wars\plan\英雄飞机.png')
def main():
    # 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((900, 500), depth = 32)
    #设定背景图片
    background = pygame.image.load('D:\python\python\python\eg\Plane wars\plan\play_back_ground.jpg')
    #设置游戏标题
    pygame.display.set_caption('飞机大作战')
    #添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('D:\python\python\python\eg\Plane wars\plan\柳轻颂 - 溯（钢琴版）.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1) #循环次数 -1 无限循环
    #创建飞机对象
    hero = HeroPlan(screen)
    #创建一个敌机对象
    enemyplan = EnemyPlan(screen)
    while True:
        screen.blit(background, (0, 0)) #显示窗口
        #显示玩家图片
        hero.display()
        #显示敌机内容
        enemyplan.display()
        #敌机移动
        enemyplan.move()
        #敌机随机发射子弹
        enemyplan.launchEnemyBullet()
        #获取键盘事件
        key_control(hero)
        # 更新飞机显示内容
        pygame.display.update() 
        #time.sleep(1)
        pygame.time.Clock().tick(30)
    pass
if __name__ == "__main__":
    main()
