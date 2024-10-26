import random
from playsound import playsound

OPS: float = random.randint(0, 100)

# 作用是减少猜中概率
num = [1, 2, 3, 4, 5]  # 正负差值
Difference: float = random.choice(num)  # 随机选取一个元素
if OPS <= 0:
    OPS += Difference
else:
    OPS -= Difference


i: int = 0
print("---TI_程序集---\n猜数字 (0 ~ 100)")
while True:
    C: float = float(input("数字："))
    if C < OPS:
        print("猜小了")
    if C > OPS:
        print("猜大了")
    if C == OPS:
        print("游戏结束,恭喜答案正确")
        break
    i += 1

playsound('Level Up.mp3')
print(f"程序结束,猜了{i}次")
