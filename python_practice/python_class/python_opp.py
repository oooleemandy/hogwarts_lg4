#面向对象
class House:
    #静态属性 类变量（在类之中，在方法之外）
    door = "red"
    floor = "white"

    #构造函数，在类实例化时直接执行了
    def __init__(self):
        #在方法中调用类变量，需要加self.
        print(self.door)
        #实例变量，类当中，方法中，"self.变量名"定义
        self.kitchen = "cook"



    #定义动态方法
    def sleep(self):
        #普通变量 在类中 方法中，并且没有self
        bed = "ximengsi"
        self.table = "桌子可以放东西"

        print(f"在房子里可以躺在{bed}上睡觉")
    def cook(self):
        print(self.kitchen)
        print(self.table)
        print("在房子里做饭")


#把类实例化
#北欧风
north_house = House()
north_house.cook()
#中式风
china_house = House()

#用类名调用类属性
# print(House.door)
# #修改类属性
# House.door = "white"
# print(House.door)
#
#
#
# #用实例对象调用类属性
# print(north_house.door)
# #
# north_house = "black"
# print(north_house.door)