import pyautogui
from time import sleep
from PIL import Image
from random import *

brother = Image.open('arcrebiano.png')
capt = Image.open('capt.png')
vot =  Image.open('vot_again.png')

comment = 1

mouse_func = [pyautogui.easeOutBack, pyautogui.easeInOutQuad, pyautogui.easeOutQuad, pyautogui.easeInBounce, pyautogui.easeInElastic]

def voto():
    sleep(1)
    w, z = pyautogui.locateCenterOnScreen(capt)
    pyautogui.moveTo(w+randint(-20,150), z+randint(-30,10), uniform(0.5, 2.0), choice(mouse_func))
    pyautogui.click()
    sleep(2)
    a, b = pyautogui.locateCenterOnScreen(vot)
    pyautogui.moveTo(a+randint(-250,250), b+randint(-15,15), uniform(0.5, 2.0), choice(mouse_func))
    pyautogui.click()
    sleep(1)


while True:
    x, y = pyautogui.locateCenterOnScreen(brother)
    pyautogui.moveTo(x+randint(-80,300), y+randint(-40,40), uniform(0.5, 2.0), choice(mouse_func))
    pyautogui.click()
    sleep(1)
    if pyautogui.locateCenterOnScreen(vot) == None:
        pyautogui.scroll(-300)
        voto()
    else:
        voto()
    comment += 1
    print("{} votos computados".format(comment))
