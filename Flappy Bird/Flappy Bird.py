import pygame as py
from random import randint
import time

class Obstacles:
    def create_obstacles():
        global obstacles
        if len(obstacles) < 3:
            obstacles.append([obstacles[len(obstacles)-1][0]+400, randint(100, y - 300)])
    def show_obstacles():
        for i in range(len(obstacles)):
            py.draw.rect(root, 'green', py.Rect(obstacles[i][0], 0, 100, obstacles[i][1]))
            py.draw.rect(root, 'green', py.Rect(obstacles[i][0], obstacles[i][1] + 200, 100, y - (obstacles[i][1] + 200)))
    def change_position():
        for i in range(len(obstacles)):
            obstacles[i][0] -= 10
    def count_points():
        global points
        if obstacles[0][0] <= -200:
            obstacles.pop(0)
            points += 1
    def check_collision(pawn):
        global running
        object1 = py.Rect(obstacles[0][0], 0, 100, obstacles[0][1])
        object2 = py.Rect(obstacles[0][0], obstacles[0][1] + 200, 100, y - (obstacles[0][1] + 200))
        if py.Rect(pawn).colliderect(object1) or py.Rect(pawn).colliderect(object2):
            running = False

working = True

py.init()

start_texts_font = py.font.SysFont('Arial', 100) 
start_text = start_texts_font.render('PRESS SPACE', 1, 'white')

while working:
    x, y = 800, 600
    root = py.display.set_mode((x, y))
    py.display.set_caption('Flappy Bird')
    pawn_size = 40
    points = 0
    root.fill('black')
    root.blit(start_text, (100, 200))
    pawn = [50, y/2-40, pawn_size, pawn_size]
    obstacles = [[600, randint(100, y - 300)]]
    clock = py.time.Clock()
    FPS = 30
    running = False
    for ev in py.event.get():
        if ev.type == py.QUIT:
            working = False
        if ev.type == py.KEYDOWN:
            if ev.key == py.K_SPACE:
                running = True
    py.display.update()
    points_texts_font = py.font.SysFont('Arial', 50) 
    while running:
        root.fill('black')
        py.draw.rect(root, 'red', py.Rect(pawn))
        pawn[1] += 10
        Obstacles.create_obstacles()
        Obstacles.show_obstacles()
        Obstacles.change_position()  
        Obstacles.count_points()
        Obstacles.check_collision(pawn)
        points_text = points_texts_font.render(f'points: {points}', 1, 'blue')
        root.blit(points_text, (600, 20))
        for ev in py.event.get():
            if ev.type == py.KEYDOWN:
                if ev.key == py.K_SPACE:
                    pawn[1] -= 100
        if pawn[1] >= y - pawn_size or pawn[1] <= 0:
            running = False
        clock.tick(FPS)
        py.display.update()

py.quit