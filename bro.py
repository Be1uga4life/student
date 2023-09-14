import random
import time
import keyboard
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def minigame():
    minigamestring = "----------------------------------------------------------------------"
    greenstring = "=========="
    minigamestring = list(minigamestring)
    index = random.randint(10, 60)

    print(index)

    while True:
        if keyboard.is_pressed('space'):
            break

        for i in range(len(minigamestring)):
            if i >= index and i - index < len(greenstring):
                minigamestring[i] = greenstring[i - index]
        
        temp = ''.join(minigamestring)
        clear()
        print(temp)
        time.sleep(0.025)

minigame()

