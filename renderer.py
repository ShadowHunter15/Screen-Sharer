import pygame
import os
import time
pygame.init()


display_width = int(input("w: "))
display_height = int(input("h: "))
frames = int(input("frames: "))
gameDisplay = pygame.display.set_mode((display_width,display_height))

i = 0

while True:
    try:
        image = pygame.image.load(str(i) + "s.jpg")
        image = pygame.transform.scale(image, (display_width, display_height))
        gameDisplay.blit(image, (0,0))
        i += 1
        time.sleep(1/frames)
        
        pygame.display.update()
    except:
        pass

