'''
    Created by dl on 2022/7/18
    PROJECT_NAME：lagou_test
'''


class Animal:

    def __init__(self, name, colour='白色', age=2, sex='磁性'):
        self.name = name
        self.colour = colour
        self.age = age
        self.sex = sex

    def shout(self):
        print(f"{self.name}会叫")

    def run(self):
        print(f"{self.name}会跑")


if __name__ == "__main__":
    animal = Animal("dabai")
    animal.shout()
