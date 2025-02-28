import pyautogui
import cv2
import numpy as np

screenshot = pyautogui.screenshot()

screenshot = np.array(screenshot)

screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)

template = cv2.imread('gba.png', 0)

screenshot_cinza = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(screenshot_cinza, template, cv2.TM_CCOEFF_NORMED)

limite = 0.8
loc = np.where(result >= limite)

if len(loc[0]) > 0:
    print("Janela Encontrada!")
    h, w = template.shape
    for pt in zip(*loc[::-1]):
        cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
else:
    print("Janela não encontrada!")

cv2.imshow('result', screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()