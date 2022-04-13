from time import sleep
import pytesseract
import pyautogui
import os
import sys

#OnLoad
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

expBtn()