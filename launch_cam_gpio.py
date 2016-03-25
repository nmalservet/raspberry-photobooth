import picamera
import time
import pygame
import random
from time import sleep
from gpiozero import Button


WIDTH=1280
HEIGHT=1024
FONTSIZE=50

def quote():
    options = ["bizarre",
               "Vous devez sous-rire",
               "kamoulox",
               "etes vous un modele-photo",
               "Vous avez grandi depuis la derniere fois?",
               "Pourquoi faites-vous cette tete?"
               ]
    return random.choice(options)

#init camera
camera = picamera.PiCamera()
camera.vflip = False
camera.hflip = False
camera.brightness = 50
#init button gpio port gpio 17
button = Button(17)

#build screen
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
black = pygame.Color(0,0,0)
textcol = pygame.Color(255,255,0)
screen.fill(black)

done = False
while not done:
    #Take a photo
    #
    camera.start_preview()
    button.wait_for_press()
    name=time.strftime("%Y%m%d_%H_%M_%S")+'.jpg'
    camera.capture(name)
    screen.fill(black)
    pygame.display.update()
    camera.stop_preview()

    #read image and put on screen
    img = pygame.image.load(name)
    screen.blit(img,(0,0))

    #overlay captions as text
    mytext = quote()
    font = pygame.font.Font('freesansbold.ttf',FONTSIZE)
    font_surf = font.render(mytext,True,textcol)
    font_rect = font_surf.get_rect()
    font_rect.left = 100
    font_rect.top = 100
    screen.blit(font_surf, font_rect)
    pygame.display.update()

    #if esc pressed or "a" escape the program
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_a:
                done = true
    sleep(3)

pygame.quit()



#camera.start_recording('video.h264')
#sleep(5)
#camera.stop_recording()

