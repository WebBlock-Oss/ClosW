import subprocess
import pygame
import os

x = -200
y = 45
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

pygame.init()
screen = pygame.display.set_mode((10, 10))

while True:
    subprocess.call("taskkill /f /im chrome.exe", shell=True)
    subprocess.call("taskkill /f /im msedge.exe", shell=True)
    subprocess.call("taskkill /f /im firefox.exe", shell=True)
