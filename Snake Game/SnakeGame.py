import pygame as py
import time
from random import randint

x, y = 400, 440
py.init()
py.display.set_caption("Snake Game")
root = py.display.set_mode((x, y))
square = py.image.load("square.png")
pointsPrinter = py.font.SysFont("Arial", 30)
points = 0
directionX = 1
directionY = 0
applePosX = applePosY = 11
clock = py.time.Clock()
snake = [[7, 11], [6, 11]]
running = True

while running:
    root.fill("white")
    printPoints = pointsPrinter.render(f'POINTS: {points}', 1, 'black') 
    apple = py.Rect(applePosX*20 + 2, applePosY*20 + 2, 16, 16)
    root.blit(printPoints, (5, 5))
    for i in range(20):
        for j in range(20):
            root.blit(square, (i*20, j*20+40))
    
    for ev in py.event.get():
        if ev.type == py.QUIT:
            running = False
        if ev.type == py.KEYDOWN:
            if ev.key == py.K_LEFT and directionX != 1:
               directionX, directionY = -1, 0
            if ev.key == py.K_RIGHT and directionX != -1:
               directionX, directionY = 1, 0
            if ev.key == py.K_UP and directionY != 1:
               directionX, directionY = 0, -1
            if ev.key == py.K_DOWN and directionY != -1:
               directionX, directionY = 0, 1

    py.draw.rect(root, "red", apple)
    
    headOfSnake = py.Rect(snake[0][0]*20, snake[0][1]*20, 20, 20)

    new_segment = snake[-1].copy()

    if headOfSnake.colliderect(apple):
        points += 1
        snake.append(new_segment)
        applePosX, applePosY = randint(0, 19), randint(2, 21)

    for i in range(len(snake)-1, 0, -1):
        snake[i][0], snake[i][1] = snake[i-1][0], snake[i-1][1]

    snake[0][0] = snake[0][0] + directionX
    snake[0][1] = snake[0][1] + directionY

    for element in snake:
        rectangle = py.Rect(element[0]*20, element[1]*20, 20, 20)
        py.draw.rect(root, "blue", rectangle)

    if snake[0][0] <= 0 or snake[0][0] >= 19:
       running = False 
    if snake[0][1] <= 2 or snake[0][1] >= 21:
       running = False
        
    if snake[0] in snake[1:]:
        running = False

    clock.tick(5)
    py.display.update()


py.quit()

