import pyautogui
import cv2
import pygetwindow as gw
import time
import numpy as np

Emu = gw.getWindowsWithTitle('mGBA - POKEMON FIRE - 0.10.4') [0]
Emu.activate()
time.sleep(1)

if Emu.left > 0 and Emu.top > 0: 
    pyautogui.click(Emu.left + 10, Emu.top + 10)

time.sleep(1)

template = cv2.imread('start.png', 0)

while(True):
    screenshot = pyautogui.screenshot(region=(Emu.left, Emu.top, Emu.width, Emu.height))
    screenshot = np.array(screenshot)
    
    screenshot_cinza = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    result = cv2.matchTemplate(screenshot_cinza, template, cv2.TM_CCOEFF)



    limite = 0.6
    loc = np.where(result >= limite)

    if len(loc[0]) > 0:
        h, w = template.shape
        pyautogui.press('enter')
        break

    else:
        pyautogui.press('x')

    time.sleep(1)

cv2.imshow('Screenshot Capturada', screenshot_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()