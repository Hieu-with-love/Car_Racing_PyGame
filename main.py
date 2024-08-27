import pygame
import time
import math

pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

# constant with convention is capital all character
GRASS = pygame.image.load("imgs/grass.jpg")
TRACK = pygame.image.load("imgs/track.png")

TRACK_BODER = pygame.image.load("imgs/track-border.png")
FINISH = pygame.image.load("imgs/finish.png")

RED_CAR = pygame.image.load("imgs/red-car.png")
GREEN_CAR = pygame.image.load("imgs/green-car.png")

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
if HEIGHT > screen_height:
    HEIGHT = screen_height - 100  # Trừ đi 100 để có thể nhìn thấy thanh tiêu đề
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")

FPS = 60

running = True
# Set up clock
clock = pygame.time.Clock()


while running:
    # this loop, cannot run faster FPS = 60 as i set
    clock.tick(FPS)

    WIN.blit(GRASS, (0,0))
    WIN.blit(TRACK, (0,0))
    WIN.blit(FINISH, (0,0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

pygame.quit()