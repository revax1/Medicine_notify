# Application: Raspberry Pi sing the national anthem
# Rev 1.0.3 (12-August-2013)
# Made By : ChokeLive (chokelive@gmail.com)
# website: www.chokelive.com

import time
import pygame

pygame.init()
clock = pygame.time.Clock()

while True:
        clock.tick(1)
        theTime=time.strftime("%H:%M:%S", time.localtime())
        print(theTime)

        if theTime == "23:47:00":
                print("Play Sound!!")
                pygame.mixer.init()
                pygame.mixer.music.load("onepiece.mp3")
                pygame.mixer.music.play()