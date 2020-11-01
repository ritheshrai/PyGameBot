import pyautogui
from PIL import Image, ImageGrab
import time

def takess():
    image = ImageGrab.grab()
    image.show()


if __name__ == "__main__":
    takess()
