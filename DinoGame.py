import pyautogui
from PIL import Image,ImageGrab
def takescreenshot():
    image=ImageGrab.grab()
    image.show()



if __name__="__main__":
    takescreenshot()