import pygame
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((1000, 700))

# title and icon
pygame.display.set_caption("Pong")
icon = pygame.image.load('football1.png')
pygame.display.set_icon(icon)
# Score
P1_score = 0
P2_score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
# Ball
ballImg = pygame.image.load('football2.png')
ballX = 480
ballY = 350
velX = -5
velY = -5

# P1
playerX = 0
playerY = 300
movement1 = 0


def show_score(x, y):
    score = font.render("P1: " + str(P1_score) + " " + "P2: " + str(P2_score), True, (255, 255, 255))
    screen.blit(score, (x, y))


def drawP1(x, y):
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 20, 50))


# P2
player2Y = 350
player2X = 980
movement2 = 10


def drawP2(x, y):
    # screen.blit(P2, (x, y))
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 20, 50))


def ball(x, y):
    screen.blit(ballImg, (x, y))


def isCollisionwP1(ballX, ballY, playerX, playerY):
    distance = math.sqrt(math.pow(ballX - playerX, 2) + (math.pow(ballY - playerY, 2)))
    if distance < 50:
        return True
    else:
        return False


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                movement1 = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                movement1 += -5
            if event.key == pygame.K_DOWN:
                movement1 += 5

    playerY += movement1
    # no out of bounds
    if playerY <= 5:
        movement1 = 0
    elif playerY >= 610:
        movement1 = 0
    # player2 movement

    if player2Y == 610:
        movement2 = -10
    elif player2Y == 0:
        movement2 = 10
    player2Y += movement2
    # INVINCIBLE
    # player2Y = ballY
    # Collision
    collision1 = isCollisionwP1(ballX, ballY, playerX, playerY)
    collision2 = isCollisionwP1(ballX, ballY, player2X, player2Y)
    # ball movement
    if ballX == 0:
        if collision1:
            velX = 5
            pongsound = mixer.Sound("pong.wav")
            pongsound.play()
        else:
            ballX = 500
            ballY = 350
            P2_score += 1
            print("P2 scores!")
            print("P1:" + str(P1_score) + " P2:" + str(P2_score))

    elif ballX == 970:
        if collision2:
            velX = -5
            pongsound = mixer.Sound("pong.wav")
            pongsound.play()
        else:
            ballX = 500
            ballY = 350
            P1_score += 1
            print("P1 scores!")
            print("P1:" + str(P1_score) + " P2:" + str(P2_score))

    if ballY == 0:
        velY = 5
    elif ballY == 630:
        velY = -5

    ballX += velX
    ballY += velY

    # screen updates

    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (500, 0), (500, 800))
    show_score(textX, textY)
    ball(ballX, ballY)
    drawP1(playerX, playerY)
    drawP2(player2X, player2Y)
    # Update Screen
    pygame.display.update()
