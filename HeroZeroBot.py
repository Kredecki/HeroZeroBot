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
        #Zmien mape x + 1
        while y < 3:
            pathToFind = path + "/img/MapPoint" + str(x) + str(y) + ".png" #Budowa ścieżki: ścieżka bezwzględna + folder i nazwa pliku + id mapy + id punktu
            img = pyautogui.locateOnScreen(pathToFind)
            if img == None:
                y+=1
            else:
                imgBtn = pyautogui.center(img)
                pyautogui.moveTo(imgBtn)
                pyautogui.move(0, -105)
                pyautogui.click(button='left')

                sleep(0.5)
                pathToFind = path + "/img/arrowRight" + ".png"
                img = pyautogui.locateOnScreen(pathToFind)
                imgBtn = pyautogui.center(img)
                pyautogui.moveTo(imgBtn)
                pyautogui.click(button='left')

                sleep(0.5)
                pyautogui.click(button='left')

                sleep(0.5)
                pathToFind = path + "/img/cancel" + ".png"
                img = pyautogui.locateOnScreen(pathToFind)
                imgBtn = pyautogui.center(img)
                pyautogui.moveTo(imgBtn)
                pyautogui.click(button='left')

                sleep(0.5)
                pathToFind = path + "/img/arrowRight" + ".png"
                img = pyautogui.locateOnScreen(pathToFind)
                imgBtn = pyautogui.center(img)
                pyautogui.moveTo(imgBtn)
                pyautogui.click(button='left')

                break
        break

expBtn()