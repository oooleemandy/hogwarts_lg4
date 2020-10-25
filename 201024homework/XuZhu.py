"""
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
"""
class XuZhu(TongLao):
    def read(self):
        print("罪过罪过")


tl = XuZhu(1000,200)
tl.see_people('WYZ')
tl.see_people('李秋水')
tl.see_people('丁春秋')
tl.fight_zms(1000,200)
tl.read()


