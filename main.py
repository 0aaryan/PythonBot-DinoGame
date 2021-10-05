import pyautogui
from PIL import ImageGrab
import time
def jump(x,y):
    img = ImageGrab.grab(bbox=(x, y, x+1, y+1))
    rgbimg = img.convert('RGB')
    r,g,b = rgbimg.getpixel((0,0))
    if r==83:
        pyautogui.press('space')

try:
    time.sleep(5)
    while True:
        jump(240,460) #pass cordinates at which you want bot to jump
except KeyboardInterrupt:
    print("\nDone...")

