import keyboard as keyboard
import pyautogui
from PIL import Image, ImageGrab
import time
import win32api, win32con

def click(key):
    pyautogui.keyDown(key)
    #time.sleep(0.01)
    #pyautogui.keyUp(key)
def hit(key):
    if key == 'up':
        win32api.keybd_event(win32con.VK_UP, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)  # press
        time.sleep(0.01)
        win32api.keybd_event(win32con.VK_UP, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)  # release
    if key == 'down':
        win32api.keybd_event(win32con.VK_DOWN, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)  # press
        time.sleep(0.01)
        win32api.keybd_event(win32con.VK_DOWN, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)  # release


def iscolliddata(data):
     for i in range(222, 311):
        for j in range(  222, 411):
            if data[i, j] == 172:
                hit('down')
                break
     for i in range(222, 289):
        for j in range(441, 461):
            if data[i, j] == 172:
                hit("up")
                break


if __name__ == '__main__':
    time.sleep(1)
    '''cactus=X:  227 Y:  469  to X:  228 Y:  421
    bird =  273 Y:  377'''
    while keyboard.is_pressed('q') == False:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        iscolliddata(data)

