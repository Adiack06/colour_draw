import pygame
import time

pygame.init()
screen = pygame.display.set_mode((640, 480))

running = True

lasttime = time.time()
lasttimefps = time.time()

while running:
    lasttime = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    deltatime = time.time() - lasttime

    if deltatime < 1/60:
        time.sleep(1/60 - deltatime)

    deltafps = (time.time() - lasttimefps)
    if deltafps > 0:
        print(1/deltafps)
    lasttimefps = time.time()