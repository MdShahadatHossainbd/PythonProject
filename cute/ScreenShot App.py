import time
import pyautogui

def ScreenShot():
    name = int(round(time.time()*1000))
    name = 'D:/cute/ScreenShot/{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

ScreenShot()
