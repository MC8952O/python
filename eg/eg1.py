'''
双人对战小游戏
'''
import time
class Player():
    def __init__(self, name, blood):
        '''
        构造初始化函数
        param name：玩家姓名
        param blood：玩家血量
        '''
        self.name = name
        self.blood = blood
    def tong(self,enemy):
        '''
        普通攻击，掉血5点
        '''
        enemy.blood -= 10
        info= '{}攻击了{}，{}掉了5点血'.format(self.name, enemy.name, enemy.name)
        print(info)  
    def kan(self,enemy):
        '''
        大招，掉血10点
        '''
        info = '{}使用了大招，攻击了{}，{}掉了10点血'.format(self.name, enemy.name, enemy.name)
        print(info)
        enemy.blood -= 20
    def chiyao(self):
        '''
        吃药，补血10点
        '''
        self.blood += 5
        print('{}吃了要，补血10点'.format(self.name))
    def __str__(cls, *args, **kwargs):
        '''
        打印玩家信息
        '''
        return '{}当前血量为：{}'.format(cls.name, cls.blood)
#创建玩家
player_mia = Player('mia', 100)
player_vesey = Player('vesey', 100)
print(player_vesey) #打印vesey血量
print(player_mia) #打印mia血量
while True:
    if player_mia.blood <= 0 or player_vesey.blood <= 0:
        '''
        满足条件退出循环
        '''
        break
    player_mia.tong(player_vesey) #mia普通攻击vesey
    print(player_vesey)
    print('----------------------------')
    player_vesey.kan(player_mia) #vesey大招攻击miap  rint(player_mia) #打印mia血量
    print('------------------------------')
    player_mia.chiyao() #mia吃药
    print(player_mia) #打印mia血量