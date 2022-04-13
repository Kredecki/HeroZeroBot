from time import sleep
import pyautogui
import os
import sys
path = os.path.dirname(sys.argv[0])
print(path)

def expBtn():
    x = 0
    y = 0
    while x < 10:
        sleep(1)
        #Znajdź samolot
        pathToFind = path + "/img/plain.png"
        img = pyautogui.locateOnScreen(pathToFind)
        imgBtn = pyautogui.center(img)
        pyautogui.moveTo(imgBtn)
        pyautogui.click(button='left')

        #Znajdź misje
        sleep(1)
        pathToFind = path + "/img/" + str(x) + ".png"
        img = pyautogui.locateOnScreen(pathToFind)
        imgBtn = pyautogui.center(img)
        pyautogui.moveTo(imgBtn)
        if x == 3 or x == 6 or x == 7 or x == 8:
            pyautogui.move(245, 0)
        else:
            pyautogui.move(220, 0)
        pyautogui.click(button='left')

        #Przeklikaj misje
        sleep(1)
        pathToFind = path + "/img/arrowRight.png"
        img = pyautogui.locateOnScreen(pathToFind)
        if img == None:
            pathToFind = path + "/img/cancelErr.png"
            img = pyautogui.locateOnScreen(pathToFind)
            imgBtn = pyautogui.center(img)
            pyautogui.moveTo(imgBtn)
            pyautogui.click(button='left')
            pyautogui.move(-100, 0)
            x+=1
            continue
        imgBtn = pyautogui.center(img)
        pyautogui.moveTo(imgBtn)
        pyautogui.click(button='left')

        sleep(0.5)
        pyautogui.click(button='left')

        #cancel
        pathToFind = path + "/img/cancel.png"
        img = pyautogui.locateOnScreen(pathToFind)
        imgBtn = pyautogui.center(img)
        pyautogui.moveTo(imgBtn)
        pyautogui.click(button='left')

        x+=1

expBtn()