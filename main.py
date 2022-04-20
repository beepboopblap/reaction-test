import pygame
from pygame import *
import time
import random
from sigfig import round

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

pygame.init()
pygame.font.init()
pygame.mixer.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Reaction Game for Children")

# colors
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
brown = (165, 42, 42)
pink = (247, 49, 188)

# fonts
Calibri60 = pygame.font.SysFont("Calibri", 60)
Calibri100 = pygame.font.SysFont("Calibri", 100)
Calibri120 = pygame.font.SysFont("Calibri", 120)
Calibri40 = pygame.font.SysFont("Calibri", 40)

# variables
running = True
screen = False
red_screen = True
green_screen = False
can_click = False
click = False
game = True
retry = False
random_time = random.randint(3,7)
x = random_time + time.time()

while running == True:


    if game == True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if can_click == True:
                    start = time.time()
                    click = True
                    if click == True:
                        end = time.time()
                        final = end - start
                        final = int(final)
                        final = round(final, sigfig = 4)
                        can_click = False
                        retry = True

                else:
                    click = False


            elif event.type == pygame.MOUSEBUTTONUP:
                click = False

            elif event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    if can_retry == True:
                        x = time.time() + random_time
                        retry = False
                        red_screen = True
                        pass


        # graphics


        if time.time() >= x:
            red_screen = False
            window.fill(green)
            can_click = True

        if red_screen == True:
            window.fill(red)

        if retry == True:
            window.fill(red,)
            score = Calibri40.render(f"Score: {final} seconds off", 1, white)
            retry_text = Calibri60.render(f"Press 'Enter' to retry", 1, white)
            window.blit(retry_text, (35,200))
            window.blit(score, (0,0))
            can_retry = True



    # update
    pygame.display.update()
    fps.tick(10)
