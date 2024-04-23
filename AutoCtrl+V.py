

import pyautogui
import time
import keyboard
import logging
from colorama import Fore, init

init(autoreset=True)  
logging.basicConfig(filename='AutoCtrl+V.log', level=logging.INFO, format='%(asctime)s %(message)s')

print( Fore.CYAN + '''
    _       _        ___ _       _   _ __   __
   /_\ _  _| |_ ___ / __| |_ _ _| |_| |\ \ / /
  / _ \ || |  _/ _ \ (__|  _| '_| |_   _\ V / 
 /_/ \_\_,_|\__\___/\___|\__|_| |_| |_|  \_/  
''')

print( Fore.LIGHTMAGENTA_EX + 'AutoCtrl+V' + Fore.CYAN + ' by ' + Fore.MAGENTA + '@Lolemploi5\n' + Fore.RESET)
print( Fore.YELLOW + 'Press ' + Fore.GREEN +'F1 ' + Fore.YELLOW + 'to ' + Fore.GREEN + 'start ' + Fore.YELLOW + '/ ' + Fore.RED + 'stop ' + Fore.YELLOW + ' the script\n' + Fore.RESET)



interrupteur = False

Key = 'f1'  # Replace F1 by the key you want
DELAY = 3  # Delay between each Ctrl + V

def on_key_press(e):
    global interrupteur
    
    if e.name == Key:  
        print(Fore.YELLOW + f'[AutoCtrl+V] Key {Key} pressed')
        logging.info(f'[AutoCtrl+V] Key {Key} pressed')
        interrupteur = not interrupteur

keyboard.on_press(on_key_press)

while True:
    try:
        if interrupteur:
            pyautogui.hotkey('ctrl', 'v')
            logging.info('[AutoCtrl+V] Ctrl + V [OK]')  
            pyautogui.press('enter')
            logging.info('[AutoCtrl+V] Enter [OK]')  
            time.sleep(DELAY)
    except pyautogui.FailSafeException:
        logging.error('[AutoCtrl+V] Error: Fail safe triggered, mouse moved to upper-left corner')  
    except Exception as e:
        logging.error(f'[AutoCtrl+V] Unexpected error: {e}')  