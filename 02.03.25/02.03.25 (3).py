import pyautogui
import time

count = int(input("Сколько раз кликнуть? "))
time_1 = int(input("Какая будет задержка? "))
while count != 0:
    pyautogui.click()
    count = count - 1
    time.sleep(time_1)