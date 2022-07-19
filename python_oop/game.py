'''
    Created by dl on 2022/7/18
    PROJECT_NAME：lagou_test
'''
from log_decoratot import log_decorator
class Game():

    def __init__(self):
        self.my_hp = 1000
        self.my_power = 200
        self.enemy_hp = 1000
        self.enemy_power = 199
        self.__secret = 10

    def __private_method(self):
        print("this is private_method")

    @log_decorator
    def fight(self):
        while True:
            # 我的剩余血量
            self.my_hp = self.my_hp - self.enemy_power
            # 敌人的剩余血量
            self.enemy_hp -= self.my_power
            print(f"我的血量:{self.my_hp} VS 敌人的血量:{self.enemy_hp}")
            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.enemy_hp <=0:
                print ("我赢了")
                break

    def rest(self,time_num):
        print(f"太累了，休息{time_num}分钟")


    @classmethod
    def win(cls):
        print("this is classmethod")

if __name__ == "__main__":
    game = Game()
    game.fight()
    # game.win()
    # Game.win()
    # print(game.__dir__())
    # game._Game__private_method()

