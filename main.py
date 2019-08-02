import pygame, sys, random, pandas as pd
from player import Player
from lava import Lava

playercol = input("What color? (colors are red, green, blue, and yellow) ")
if playercol == "red":
    playercol = (255, 0, 0)
elif playercol == "green":
    playercol = (0, 255, 0)
elif playercol == "blue":
    playercol = (0, 0, 255)
elif playercol == "yellow":
    playercol = (255, 255, 0)
else:
    playercol = (0, 0, 0)
player = Player(playercol)

pygame.init()
screen = pygame.display.set_mode((1300, 500))
clock = pygame.time.Clock()

info = pd.read_csv("data.csv")
numlevels = info["level"].min()
level = info["level"].min()
levelInfo = info.iloc[level]
lavas = []

font = pygame.font.SysFont("comicsansms", 72)

def init():
    global lavas, player
    player.xleft = 10
    player.yup = 10
    lavas = []
    try:
        levelInfo = info.iloc[level]
    except:
        sys.exit("You win!")
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
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.jump(8)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.xvelocity -= 7
            if event.key == pygame.K_RIGHT or event.key == pygame.K_s:
                player.xvelocity += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.xvelocity = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_s:
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
        if level < numlevels:
            sys.exit("You win!")
        init()
    text = font.render(str(level + 1), True, (238,130,238))
    screen.blit(text, (40 - text.get_width() // 2, 470 - text.get_height() // 2))
    pygame.display.flip()
    screen.fill((255, 255, 255))