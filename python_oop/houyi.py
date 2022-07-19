'''
    Created by dl on 2022/7/18
    PROJECT_NAME：lagou_test
'''
from game import Game


class Houyi(Game):
    def __init__(self):
        self.defense = 100
        # 继承父类的构造方法
        super(Houyi, self).__init__()

    def fight(self):
        # 改造一下my_hp的计算方式
        while True:
            # 我的剩余血量
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            # 敌人的剩余血量
            self.enemy_hp -= self.my_power

            super(Houyi, self).rest(5)
            print(f"我的血量:{self.my_hp} VS 敌人的血量:{self.enemy_hp}")
            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break

        # super()._Game__private_method()



if __name__ == "__main__":
    houyi = Houyi()
    houyi.fight()
    # houyi.rest(5)
