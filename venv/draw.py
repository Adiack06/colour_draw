import random
import pygame
import time
import json


#file exporer
from tkinter import filedialog



pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1920, 900))
def openfile():
    filepath = filedialog.SaveFileDialog


lasttime = time.time()
size = 10

red = 10
blue = 10
green = 10
running = True
circles = []
save1 = []
length_circles = 0
words = []
save_file = []
save_file_load = []
word = 1
filepath = 1

class Circle:
    def __init__(self, colour, position, size):
        self.colour = colour
        self.position = position
        self.size = size


def handle_event(event):
    global running
    global size
    global red
    global green
    global blue
    global save1
    global circles
    global length_circles
    global words
    global save_file_load
    global save_file
    global word
    global file
    keys = pygame.key.get_pressed()

    if event.type == pygame.QUIT:
        running = False
    #colour and size change
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 5:
            delta = -10
        elif event.button == 4:
            delta = 10
        else:
            delta = 0

        if keys[pygame.K_q]: red += delta
        if keys[pygame.K_w]: green += delta
        if keys[pygame.K_e]: blue += delta

        if red > 255: red = 255
        if green > 255: green = 255
        if blue > 255: blue = 255

        if red < 0: red = 0
        if green < 0: green = 0
        if blue < 0: blue = 0
        if size < 0: size = 0


        print(f"red{red}, green{green}, blue{blue}, size{size}")


        if (not keys[pygame.K_q]) and (not keys[pygame.K_w]) and (not keys[pygame.K_e]):
            size += delta
    #saves
    if keys[pygame.K_1]:
        circles.clear()
        circles = save1.copy()

    if keys[pygame.K_2]:
        save1 = circles.copy()


    #undo
    length_circles = len(circles)
    if (keys[pygame.K_z]) and (not length_circles == 0):
        circles.pop(length_circles-1)

    #radom words
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
            word = (words.__getitem__(random.randint(1, (len(words) - 1))))
            print(word)

    with open("words.txt") as words_file:
        words = words_file.readlines()



    # saving

    if keys[pygame.K_s]:
        filepath = filedialog.asksaveasfilename()
        save_obj = {"circles": []}
        for circle in circles:
            save_obj["circles"].append({"colour": circle.colour, "position": circle.position, "size": circle.size})
        with open(filepath, "w") as f:
            f.write(json.dumps(save_obj))

    # loading
    if keys[pygame.K_l]:
        filepath = filedialog.askopenfilename()
        with open(filepath, "r") as f:
            circles = []
            for data in json.loads(f.read())["circles"]:
                circles.append(Circle(data["colour"], data["position"], data["size"]))

    #optomise
    if keys[pygame.K_c]:
        print(len(circles))

    #rest
    if keys[pygame.K_DELETE]:
        circles.clear()



while running:
    deltatime = time.time() - lasttime
    lasttime = time.time()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        handle_event(event)

    if pygame.mouse.get_pressed(3)[0]:
        circles.append(Circle((red, green, blue), pygame.mouse.get_pos(), size))

    for circle in circles:
        pygame.draw.circle(screen, circle.colour, circle.position, circle.size)

    #curser
    pygame.draw.circle(screen, (red, green, blue), pygame.mouse.get_pos(), size)
    #colour icon
    pygame.draw.circle(screen, (0, 0, 0), (70, 70), 70)
    pygame.draw.circle(screen, (255, 255, 255), (70, 70), 65)
    pygame.draw.circle(screen, (red, green, blue), (70,70), 60)

    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    textsurface = myfont.render(str(word), False, (0, 0, 0))
    screen.blit(textsurface, (10, 200))







    pygame.display.flip()

#time.deltatime

