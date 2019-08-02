import pygame, sys, random, pandas as pd
from player import Player
from lava import Lava

playercol = input("What color? (colors are red, green, blue, and yellow) ")
if playercol == "red":
    playercol = (255, 0, 0)
if playercol == "green":
    playercol = (0, 255, 0)
if playercol == "blue":
    playercol = (0, 0, 255)
if playercol == "yellow":
    playercol = (255, 255, 0)
player = Player(playercol)

pygame.init()
screen = pygame.display.set_mode((1300, 500))
clock = pygame.time.Clock()

info = pd.read_csv("data.csv")
numlevels = info["level"].min()
level = info["level"].min()
levelInfo = info.iloc[level]
lavas = []

def init():
    global lavas, player
    player.xleft = 10
    player.yup = 10
    lavas = []
    levelInfo = info.iloc[level]
    for i in range(levelInfo["numlava"]):
        lavas.append(Lava(random.randint(50, 1300), random.randint(0, 500), random.randint(20, 50)))

init()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit("Thanks for playing!")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit("Thanks for playing!")
            if event.key == pygame.K_UP:
                player.jump(8)
            if event.key == pygame.K_LEFT:
                player.xvelocity -= 7
            if event.key == pygame.K_RIGHT:
                player.xvelocity += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.xvelocity = 0
            if event.key == pygame.K_RIGHT:
                player.xvelocity = 0
    for lava in lavas:
        pygame.draw.rect(screen, (91, 229, 227), pygame.Rect(lava.x + (lava.size / 2), lava.y + (lava.size / 2), lava.size, lava.size), 0)
        if player.yup < -50 or player.yup > 550 or player.yup > lava.y and player.yup < lava.y + lava.size and player.xleft > lava.x and player.xleft < lava.x + lava.size:
            init()
    pygame.draw.rect(screen, player.color, pygame.Rect(player.xleft, player.yup, player.width, player.height), 0)
    player.applygravity(0.4)
    player.move()
    if player.xleft > 1280:
        level += 1
        if level == 5:
            sys.exit("You win!")
        init()
    pygame.display.flip()
    screen.fill((255, 255, 255))