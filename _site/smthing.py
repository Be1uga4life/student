import random
from os import system, name
import time
import sys
import keyboard
import os

def clear():
  if name == 'nt':
    _ = system('cls')
  else:
    _ = system('clear')
    

def minigame():
    minigamestring = "----------------------------------------------------------------------"
    greenstring = "=========="
    minigamestring = list(minigamestring)
    index = random.randint(10, 60)
    temp = ''

    print(index)

    while True:
        if os.name == 'nt':
            import msvcrt
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b' ':
                    break
        else:
            import termios
            import sys
            import tty

            def is_space_pressed():
                return termios.tcgetattr(sys.stdin)[6][0]

            old_settings = termios.tcgetattr(sys.stdin)
            try:
                tty.setcbreak(sys.stdin.fileno())
                while True:
                    if is_space_pressed():
                        break
            finally:
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

        for i in range(len(minigamestring)):
            if i >= index and i - index < 10:
                minigamestring[i] = greenstring[i - index]
            temp += minigamestring[i]

        temp = list(temp)
        temp3 = temp

        for i in range(len(temp)):
            time.sleep(0.025)
            clear()
            temp = temp3
            temp2 = ''
            wheeee = temp[i]
            temp[i] = '|'
            for j in temp:
                temp2 += j
            print(temp2)
            temp[i] = wheeee
            
minigame()
