import random

import pyautogui as pg

import time

animal=('Intellegent','Genious','Clever','Sharp','Good','Excellent','Super')

time.sleep(10)

for i in range(1000):
    a=random.choice(animal)
    pg.write('You Are a ' + a)
    pg.press('enter')