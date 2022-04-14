from tkinter import *
from tkinter import ttk
from time import sleep
from turtle import width
import pytesseract
import pyautogui
import os
import sys

#onLoad
path = os.path.dirname(sys.argv[0])
pytesseract.pytesseract.tesseract_cmd = r'D:/tesseract/tesseract.exe'

def expBtn():
    x = 0
    y = 0

    def cancel():
        pathToFind = path + "/img/cancel.png"
        img = pyautogui.locateOnScreen(pathToFind)
        if img == None:
            print('')
        else:
            imgBtn = pyautogui.center(img)
            pyautogui.moveTo(imgBtn)
            pyautogui.click(button='left')
    cancel()

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
        if img == None:
            pathToFind = path + "/img/v" + str(x) + ".png"
            img = pyautogui.locateOnScreen(pathToFind)
        imgBtn = pyautogui.center(img)
        pyautogui.moveTo(imgBtn)
        if x == 3 or x == 6 or x == 7 or x == 8:
            pyautogui.move(245, 0)
        else:
            pyautogui.move(220, 0)
        pyautogui.click(button='left')

        #Przeklikaj i sprawdź misje
        sleep(1)
        def questCalc():
            try:
                pathToFind = path + "/img/Konieczne.png"
                img = pyautogui.locateOnScreen(pathToFind)
                pyautogui.screenshot(path + "/screenshots/time.png", region=(img.left-22,655, 23, 20))
                time = pytesseract.image_to_string(path + "/screenshots/time.png")
                timeInt = int(time)
                
                try:
                    pathToFind = path + "/img/reward.png"
                    img = pyautogui.locateOnScreen(pathToFind)
                    pyautogui.screenshot(path + "/screenshots/reward.png", region=(img.left+38,695, 60, 20))
                    reward = pytesseract.image_to_string(path + "/screenshots/reward.png")
                    rewardInt = int(reward)
                    print(rewardInt)
                except ValueError:
                    try:
                        reward = pytesseract.image_to_string(path + "/screenshots/reward.png")
                        reward = reward[0:2] + reward [3:6]
                        rewardInt = int(reward)
                        print(rewardInt)
                    except ValueError:
                        try:
                            reward = pytesseract.image_to_string(path + "/screenshots/reward.png")
                            reward = reward[0:1] + reward [2:5]
                            rewardInt = int(reward)
                            print(rewardInt)
                        except ValueError:
                            try:
                                reward = pytesseract.image_to_string(path + "/screenshots/reward.png")
                                reward = reward[0:3]
                                rewardInt = int(reward)
                                print(rewardInt)
                            except ValueError:
                                print('ERROR 1')
            except ValueError:
                pathToFind = path + "/img/Konieczne.png"
                img = pyautogui.locateOnScreen(pathToFind)
                pyautogui.screenshot(path + "/screenshots/time.png", region=(img.left-22,655, 26, 20))
                time = pytesseract.image_to_string(path + "/screenshots/time.png")
                timeInt = int(time[0:2])

                try:
                    pathToFind = path + "/img/reward.png"
                    img = pyautogui.locateOnScreen(pathToFind)
                    pyautogui.screenshot(path + "/screenshots/reward.png", region=(img.left+38,695, 60, 20))
                    reward = pytesseract.image_to_string(path + "/screenshots/reward.png")
                    rewardInt = int(reward)
                    print(rewardInt)
                except ValueError:
                    try:
                        reward = pytesseract.image_to_string(path + "/screenshots/reward.png")
                        reward = reward[0:2] + reward [3:6]
                        rewardInt = int(reward)
                        print(rewardInt)
                    except ValueError:
                        try:
                            reward = pytesseract.image_to_string(path + "/screenshots/reward.png")
                            reward = reward[0:1] + reward [2:5]
                            rewardInt = int(reward)
                            print(rewardInt)
                        except ValueError:
                            try:
                                reward = pytesseract.image_to_string(path + "/screenshots/reward.png")
                                reward = reward[0:3]
                                rewardInt = int(reward)
                                print(rewardInt)
                            except ValueError:
                                print('ERROR 1')
        questCalc()

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
        pyautogui.moveTo(img.left, img.top)
        pyautogui.click(button='left')

        sleep(0.5)
        questCalc()
        pyautogui.click(button='left')

        sleep(0.5)
        questCalc()

        cancel()

        x+=1

def expStopBtn():
    print('')

#gui

#TODO
##########################
#  SETTINGS  #  Exp Bot  #
#TesseractCMD#           #
#  [      ]  #  [START]  #
#  [APPLY!]  #  [STOP!]  #
##########################
#         [QUIT]         #
##########################

hzb = Tk()
hzb.title('HzBot')

mainFrm = ttk.Frame(hzb)
mainFrm.grid()
mainFrm['padding'] = 10
mainFrm['relief'] = 'sunken'

settings = ttk.Frame(mainFrm)
settings.grid(column=0, row=1)
settings['padding'] = 10
settings['border'] = 2
settings['relief'] = 'sunken'
ttk.Label(mainFrm, text="Settings").grid(column=0, row=0)
ttk.Label(settings, text="TesseractCMD").grid(column=0, row=0)
Text(settings, height = 1, width = 10).grid(column=0, row=1) #TODO: Ustawienia ścieżki do tesseracta, kalibracja tesseracta
ttk.Button(settings, text="APPLY", command=expBtn).grid(column=0, row=2)

ttk.Label(mainFrm, text="Exp Bot").grid(column=1, row=0)
expBotFrm = ttk.Frame(mainFrm)
expBotFrm.grid(column=1, row=1, padx=10)
expBotFrm['padding'] = 10
expBotFrm['border'] = 2
expBotFrm['relief'] = 'sunken'
#expBotFrm = ttk.Frame(hzb, width=1000, height=1000) TODO: Do naprawy

ttk.Button(expBotFrm, text="Start", command=expBtn).grid(column=1, row=1)
ttk.Button(expBotFrm, text="Stop", command=expStopBtn).grid(column=1, row=2)
ttk.Radiobutton(expBotFrm, text="Exp", value=1).grid(column=1, row=3)
ttk.Radiobutton(expBotFrm, text="Exp", value=2).grid(column=1, row=4) #TODO: zmienić na Money

#quit = ttk.Button(mainFrm, text="Quit", command=hzb.destroy, width=10).grid(column=0, row=99) TODO: Do poprawy
hzb.mainloop()