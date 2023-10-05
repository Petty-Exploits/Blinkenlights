import os
import pygame
from time import sleep
from pathlib import Path


LINES_PER_FRAME = 14
DELAY = 67


pygame.mixer.init()
pygame.mixer.music.load('Limewired.mp3')

pygame.mixer.music.play()
with open(Path(__file__).parent / 'blinkenlightsOffline.txt', 'r') as f:
    film_data = f.read().split('\n')

os.system('clear')
for i in range(0, len(film_data), LINES_PER_FRAME):
    lines = film_data[i+1:i+LINES_PER_FRAME]
    print("\033[{0}A\033[J{1}".format(LINES_PER_FRAME, '\n'.join(lines)))
    sleep(float(film_data[i]) * DELAY / 1000)


