# -*- coding:utf-8 -*-

import os
import sys
from env import BASE_DIR

# переписать через os.path.join
AUDIO_DIR = BASE_DIR + '/../audio'

mp3 = os.listdir(AUDIO_DIR)
for i in range(len(mp3)):
    mp3[i] = AUDIO_DIR + '/' + mp3[i]


#import pyfmodex
#system = pyfmodex.System()
#system.init()
#sound = system.create_sound(mp3[1])
#sound.play()

import time, sys
import pygame
from pygame import *

pygame.mixer.init()
pygame.mixer.music.load(mp3[1])
pygame.mixer.music.play()

time.sleep(15)

# mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
# pygame.init()
# print pygame.mixer.get_init()
# screen=pygame.display.set_mode((400,400),0,32)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == KEYDOWN:
#             if event.key==K_ESCAPE:
#                  pygame.quit()
#                  sys.exit()
#             elif event.key==K_UP:
#                 s = pygame.mixer.Sound('/home/daniil/Project/timemaster/src/audio/3285.wav')
#                 ch = s.play()
#                 while ch.get_busy():
#                     pygame.time.delay(100)
#     pygame.display.update()