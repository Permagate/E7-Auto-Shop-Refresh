# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 19:19:03 2020

@author: Ema
"""


from pyautogui import *
import pyautogui
import time
import keyboard

#pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)
#Scroll at semi random place
#Aprox place X: 1263 Y:  590
########
#%%Fail-Safes
##After each pyautogui instruction waits for 0.25 seconds
pyautogui.PAUSE = 0.3
##If you drag your mouse to the upper left will abort program
pyautogui.FAILSAFE = True
#%%Set-up
##Get screen res
pantalla=pyautogui.size()
##Move to center of the screen instantly
pyautogui.moveTo(pantalla[0]/2, pantalla[1]/2, duration=0)

#number of visual inspections done on screen
scanned=0
#number of coven bought
cont_coven=0
#number of mystic bought
cont_mystic=0
#number of refresh done
cont_refresh=0

#mark coven as bought so the script no longer attempts to buy it twice every shop refresh
coven_bought=False
#mark mystic as bought so the script no longer attempts to buy it twice every shop refresh
mystic_bought=False

#scan only limited number of times before refreshing shop
scan_per_refresh=3

#in between scan, the script attempt to drag upward by this amount (in pixel)
drag_length=300

#max refresh attempt
max_refresh=333

#countdown to script run
#to give startup grace time so user can refocus the emulator
for i in range(3,0,-1):
    print(f"Running script in {i}...")
    time.sleep(1)

#%%
while keyboard.is_pressed('q') == False:
    time.sleep(0.2)
#Search for the refresh button
    RB_pos=pyautogui.locateOnScreen('refresh_button.PNG',confidence=0.90)
#The confidence is added due to little variations in the background
#Search for the price and quantity image of covenant summon
    Coven_pos=pyautogui.locateOnScreen('covenant.PNG',confidence=0.85,grayscale=True)
#Search for the price and quantity image of mystic summon
    Mystic_pos=pyautogui.locateOnScreen('mystic.PNG',confidence=0.85,grayscale=True)

#Checks for covenant
    if coven_bought == False and (Coven_pos) != None:
        print("Buy Covenant Summons.")
        pyautogui.click(x=Coven_pos[0]+800, y=Coven_pos[1]+100, clicks=2, interval=0.05, button='left')
        time.sleep(0.5) #wait for confirm button
        Buy_button_Covenant_pos=pyautogui.locateOnScreen('Buy_button_Covenant.PNG',confidence=0.90)
        Buy_button_Covenant_point=pyautogui.center(Buy_button_Covenant_pos)
        pyautogui.click(x=Buy_button_Covenant_point[0], y=Buy_button_Covenant_point[1], clicks=2, interval=0.05, button='left')
        cont_coven+=1
        coven_bought=True
    else:
        time.sleep(0.05)

#checks for mystic
    if mystic_bought == False and (Mystic_pos) != None:
        print("Buy Mystic Summons.")
        pyautogui.click(x=Mystic_pos[0]+800, y=Mystic_pos[1]+100, clicks=2, interval=0.05, button='left')
        time.sleep(0.5) #wait for confirm button
        Buy_button_Mystic_pos=pyautogui.locateOnScreen('Buy_button_Mystic.PNG',confidence=0.90)
        Buy_button_Mystic_point=pyautogui.center(Buy_button_Mystic_pos)
        pyautogui.click(x=Buy_button_Mystic_point[0], y=Buy_button_Mystic_point[1], clicks=2, interval=0.05, button='left')
        cont_mystic+=1
        mystic_bought=True
    else:
        time.sleep(0.05)

# Increment scan attempt, the script scans only a limited number of times before refreshing the shop
    scanned+=1

# Refresh if scan attempt hits the limit
# Otherwise, drag the screen upward
    if scanned>=scan_per_refresh:
        if cont_refresh>=max_refresh:
            # Exit script when max refresh attempt has been reached
            break
        time.sleep(0.5)
        RB_point=pyautogui.center(RB_pos)
        pyautogui.click(x=RB_point[0], y=RB_point[1], clicks=2, interval=0.05, button='left')
        time.sleep(0.5)#wait for confirm to appear
        Confirm_pos=pyautogui.locateOnScreen('confirm button.PNG',confidence=0.90)
        Confirm_point=pyautogui.center(Confirm_pos)
        pyautogui.click(x=Confirm_point[0], y=Confirm_point[1], clicks=2, interval=0.05, button='left')
        scanned=0
        time.sleep(0.5)
        cont_refresh+=1
        coven_bought=False
        mystic_bought=False
        print("Covenant Summons bought=",cont_coven)
        print("Mystic Summons bought=",cont_mystic)
        print("Refresh Done=",cont_refresh)
    else:
        pyautogui.moveTo(pantalla[0]/2, pantalla[1]/2, duration=0)
        #Drag upward 300 pixels in 0.2 seconds
        pyautogui.dragTo(pantalla[0]/2, pantalla[1]/2-drag_length, duration=0.2)
        time.sleep(0.1)

#%%Outside of the while loop
print("You exited successfuly")