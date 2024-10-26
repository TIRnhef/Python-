import pyautogui
import time
from pynput import keyboard
from playsound import playsound
import random


i = 1
ci = int(input("请输入次数:"))  # 刷屏次数
content = str(input("请输入内容:"))  # 刷屏内容
speed = float(input("打印间隔:"))  # 刷屏间隔时间
YON: str = input("是否开启随机间隔:")
IOS: float = speed

# 倒计时
for a in range(10, 0, -1):
    print(f"\r请在{a}S内将鼠标放在要输入的位置", end='')
    time.sleep(1)

pyautogui.click()
# time.sleep(0.5)
k = keyboard.Controller()

# 判断是否开启随机间隔
if YON == "yes":

    while i <= ci:
        deviation = random.random()  # 随机数
        if IOS > 0:
            IOS -= deviation
        else:
            IOS += deviation
        print(f"\r剩余次数:{ci - i};频率:{IOS}S/条", end='')
        k.type(content)  # 模拟键盘打字
        pyautogui.keyUp('enter')  # 按下enter键
        pyautogui.keyDown('enter')  # 松开enter键
        time.sleep(IOS)  # 输入间隔
        IOS = speed

        i += 1

else:
    while i <= ci:
        print(f"\r剩余次数:{ci - i};频率:{speed}S/条", end='')
        k.type(content)  # 模拟键盘打字
        pyautogui.keyUp('enter')  # 按下enter键
        pyautogui.keyDown('enter')  # 松开enter键
        time.sleep(speed)  # 输入间隔

        i += 1

print("\r完成")
playsound('Level Up.mp3')  # 播放提示音
