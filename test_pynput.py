from pynput.keyboard import Key, Controller
from time import sleep

kbd = Controller()
sleep(3)
for _ in range(5):
    kbd.press('d')
    sleep(2)
    kbd.release('d')

