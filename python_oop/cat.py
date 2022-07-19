'''
    Created by dl on 2022/7/18
    PROJECT_NAME：lagou_test
'''
from  house import Animal
class Cat(Animal):

    def __init__(self, name, duanfa):
        super().__init__(name)
        self.maofa = duanfa

    def catchmice(self):
        print(f"他可以捉老鼠")

    def shout(self):
        print(f'{self.name}可以喵喵叫  是{self.maofa}')


if __name__ == "__main__":
    cat = Cat('dabai', 'ss')
    cat.shout()
    print(cat.sex)