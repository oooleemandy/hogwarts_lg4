#定义敌人的血量 敌人的攻击力
import random


def fight(enemy_hp, enemy_power):
    #定义自己的血量 自己的攻击力
    my_hp = 1000
    my_power = 200

    #打印敌人的血量 敌人的攻击力
    print(f"敌人的血量为{enemy_hp}, 敌人的攻击力为{enemy_power}")

    #加入循环 进行多轮游戏
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        #判断谁的血量小于等于0
        if my_hp <= 0:
            #打印我和敌人的剩余血量
            print(f"我的剩余血量为{my_hp}")
            print(f"敌人的剩余血量为{enemy_hp}")
            print("我输了")

            #满足条件跳出循环
            break
        elif enemy_hp <= 0:
            print(f"我的剩余血量为{my_hp}")
            print(f"敌人的剩余血量为{enemy_hp}")
            print("我赢了")
            break


if __name__ == "__main__":
    #列表推导式生成hp
    hp = [x for x in range(990,1010)]

    #让敌人的hp从hp列表中随机取一个值
    enemy_hp = random.choice(hp)

    enemy_power = random.randint(190,210)

    #调用函数，传入敌人的hp和power
    fight(enemy_hp, enemy_power)
