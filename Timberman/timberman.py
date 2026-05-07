import pygame as py
from random import choice
from time import sleep

py.init()
x = y = 400
record = 0
root = py.display.set_mode((x, y))
py.display.set_caption('Timberman') 
gamerPos = py.Rect(100, 330, 40, 40)

class Branches():
    @staticmethod
    def displayBranches():
        global branches, y1
        if(len(branches) < 5):
            newBranch = choice(['left', 'right'])    
            if(newBranch == 'left'):
                branch = [60, y1, 100 , 40]
                branches.append(branch)
            elif(newBranch == 'right'):
                branch = [240, y1, 100 , 40]
                branches.append(branch)
            y1 -= 80

        for branch in branches:
            py.draw.rect(root, 'green', py.Rect(branch))


running = False

while True:
    root.fill('white')
    points = 0
    bigText = py.font.SysFont('Arial', 50)
    text = py.font.SysFont('Arial', 30)
    mainText = bigText.render('TIMBERMAN GAME!', 1, 'black')
    recordText = text.render(f'Your record: {record}', 1, 'black')
    startText = text.render('PRESS SPACE TO START', 1, 'black')
    root.blit(mainText, (0, 50))
    root.blit(recordText, (50, 150))
    root.blit(startText, (30, 250))
    for ev in py.event.get():
        if ev.type == py.KEYDOWN:
            if ev.key == py.K_SPACE:
                y1 = 240
                branches = []
                running = True
        if ev.type == py.QUIT:
            py.quit()
    while running:
        tree = py.Rect(160, 0, 80, y)
        root.fill('white')
        py.draw.rect(root, 'brown', tree)
        Branches.displayBranches()
        for ev in py.event.get():
            if ev.type == py.QUIT:
                py.quit()
            if ev.type == py.KEYDOWN:
                if ev.key == py.K_LEFT:
                    points += 100
                    gamerPos = py.Rect(100, 330, 40, 40)
                    for i in range(0, len(branches)):
                        branches[i][1] = branches[i][1] + 80
                        y1 += 80
                if ev.key == py.K_RIGHT:
                    points += 100
                    gamerPos = py.Rect(260, 330, 40, 40)
                    for i in range(0, len(branches)):
                        branches[i][1] = branches[i][1] + 80
                        y1 += 80
        if gamerPos.colliderect(py.Rect(branches[0])):
            if(points > record):
                record = points
            running = False
        elif branches[0][1] >= 340:
            del branches[0]
            newBranch = choice(['left', 'right'])
            if newBranch == 'left':
                branch = [60, branches[-1][1] - 80, 100 , 40]
            else:
                branch = [240, branches[-1][1] - 80, 100 , 40]
            branches.append(branch)
        typeOfText = py.font.SysFont('Arial', 20)
        pointsPrinter = typeOfText.render(f'Points: {points}', True, 'black')
        root.blit(pointsPrinter, (5, 5))
        py.draw.rect(root, 'red', gamerPos)
        py.display.update()
    py.display.update()