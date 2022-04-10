from time import sleep
import pyautogui
import pytesseract
import os

pyautogui.FAILSAFE = True

def chooseMission():
    #Definicja tablic
    x = 0
    while x < 7:
        MapPoint = []
        makePath = []
        vnum = []
        MapPoint.append(x)
        makePath.append(x)
        vnum.append(x)
        x+=1
    #Sprawdzanie misji
    i = 0
    while i < 1:
        #Tworzenie ścieżki
        istr = str(i)
        path = 'C:/Users/Kredek/Desktop/ReMetin/ReMetin/HeroZeroBot/img/MapPoint'
        png = '.png'
        v = 'v'
        vnum = 0

        while vnum < 3:
            vnumstr = str(vnum)
            makePath[i] = path + istr + v + vnumstr + png

            #Obsługa błędów
            Error1pt1 = 'Na mapie numer '
            Error1pt2 = ' nie znaleziono odniesienia.'
            Error1 = Error1pt1 + istr + Error1pt2
            Error2pt1 = 'Pozycja numer '
            Error2pt2 = ' jest niedostępna'
            Error2 = Error2pt1 + vnumstr + Error2pt2

            #Szukanie punktu odniesienia
            MapPoint[i] = pyautogui.locateOnScreen(makePath[i])
            if MapPoint[i] == None:
                print(Error2)
                vnum+=1
            else:
                #Otwórz panel misji
                mapPointBtn = pyautogui.center(MapPoint[i])
                pyautogui.moveTo(mapPointBtn)
                pyautogui.move(0, -105)
                pyautogui.click(button='left')

                #Przeklikaj misje
                sleep(0.5)
                arrowRight = pyautogui.locateOnScreen('C:/Users/Kredek/Desktop/ReMetin/ReMetin/HeroZeroBot/img/arrowRight.png')
                arrowRightBtn = pyautogui.center(arrowRight)
                pyautogui.moveTo(arrowRightBtn)
                pyautogui.click(button='left')
                sleep(0.5)
                pyautogui.click(button='left')

                #Zamknij panel misji
                sleep(0.5)
                pyautogui.move(125, 0)
                pyautogui.click(button='left')

                #Przejdź do następnej mapy
                sleep(0.5)
                arrowRight = pyautogui.locateOnScreen('C:/Users/Kredek/Desktop/ReMetin/ReMetin/HeroZeroBot/img/arrowRight.png')
                arrowRightBtn = pyautogui.center(arrowRight)
                pyautogui.moveTo(arrowRightBtn)
                pyautogui.click(button='left')
                
                vnum+=3
        i+=1
chooseMission()