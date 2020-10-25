# 1、定义人类 属性有姓名年龄体重 方法有吃饭睡觉加班
class Person():
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        print(f"{self.name}在吃饭")

    def work(self):
        print(f"{self.name}在加班")

    def sleep(self):
        print(f"{self.name}在睡觉")


p = Person('Mark',30,150)
p.eat()
p.work()
p.sleep()


# 2、定义一个箱子类，属性有颜色和大小 方法有装食品装物品
class Box:
    def __init__(self,color, size):
        self.color =color
        self.size = size

    def food(self):
        print(f"{self.size}{self.color}的箱子用来装吃的")

    def obj(self):
        print(f"{self.size}{self.color}的箱子用来装物品")

bfood = Box('红色','大的')
bobj = Box('蓝色','小的')
bfood.food()
bobj.obj()

#3、定义机票类 属性有出发地 目的地和历经时间
class Ticket:
    def __init__(self,departure,destination,time):
        self.departure = departure
        self.destination = destination
        self.time = time

    def p(self):
        print(f"由{self.departure}飞往{self.destination}的飞机历时{self.time}到达")

t = Ticket('杭州', '深圳','2小时')
t.p()

#4、定义一个学生类 属性有班级学号分数 方法有期末考试
class Student:
    def __init__(self,grade,no,score):
        self.grade = grade
        self.no = no
        self.score = score

    def exam(self):
        print(f"{self.grade}班的学号为{self.no}的同学本次考试成绩为{self.score}")

s = Student('11','19190808','150')
s.exam()


#5、定义一个书类 书的属性有书名 作者 序列号,有新增图书和借出图书方法
class Book:
    def __init__(self,name,author,index):
        self.name = name
        self.author = author
        self.index = index

    def addbook(self):
        print(f"新增一本{self.name}图书，作者为{self.author},序号为{self.index}")

    def lendbook(self):
        print(f"{self.name}图书，作者为{self.author}，序列号为{self.index}被借出去啦")

class Library(Book):
    print("这里是图书馆")


libadd = Library('哈利波特与魔法石','J.K.Rowling','85533')
liblend = Library("哈利波特与死亡圣器",'J.K.Rowling','85566')
libadd.addbook()
liblend.lendbook()