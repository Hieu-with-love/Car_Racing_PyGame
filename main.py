import pygame
import time
import math
from utils import scale_image, blit_rotate_center

pygame.init()
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

# constant with convention is capital all character
GRASS = scale_image(pygame.image.load("imgs/grass.jpg"), 2.5)
TRACK = scale_image(pygame.image.load("imgs/track.png"), 0.9)

TRACK_BODER = scale_image(pygame.image.load("imgs/track-border.png"), 0.9)
FINISH = pygame.image.load("imgs/finish.png")

RED_CAR = scale_image(pygame.image.load("imgs/red-car.png"), 0.55)
GREEN_CAR = scale_image(pygame.image.load("imgs/green-car.png"), 0.55)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
if HEIGHT > screen_height:
    HEIGHT = screen_height - 100  # Trừ đi 100 để có thể nhìn thấy thanh tiêu đề
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")

FPS = 60

class AbstractCar:
    IMG = RED_CAR

    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        # start at angle 0, then turn right or turn left
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.1

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel
    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()
    
    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

class PlayerCar(AbstractCar):
    IMG = RED_CAR
    START_POS = (180, 200)

def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img,pos)
    
    player_car.draw(win)
    pygame.display.update()

running = True
# Set up clock
clock = pygame.time.Clock()
images = [(GRASS, (0,0)), (TRACK, (0,0))]
player_car = PlayerCar(4,4)

while running:
    # this loop, cannot run faster FPS = 60 as i set
    clock.tick(FPS)

    draw(WIN, images, player_car)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        player_car.move_forward()

pygame.quit()