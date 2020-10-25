class Bicycle:
    def run(self, km):
        print(f"一共骑行{km}公里")

#子类继承父类
class EBicycle(Bicycle):
    #属性需要传参定义，可以直接放到构造函数中
    def __init__(self,valume):
        self.valume = valume

    #充电 方法
    def fill_charge(self,vol):
        #充电后的电量=本身的电量+充电电量
        self.valume = self.valume + vol
        print(f"充了{vol}度电，现在电量为{self.valume}度")

    def run(self,km):

        #1、获取目前电量能电动骑行的历程数
        power_km = self.valume *10

        if power_km >= km:
            print(f"使用电量骑了{km}")
        else:
            #电量不够了 用脚骑
            print(f"使用电量骑了{power_km}")
            super().run(km - power_km)


ebike = EBicycle(10)
ebike.fill_charge(150)
ebike.run(2)


# bike = Bicycle()
# print(bike.run(10))