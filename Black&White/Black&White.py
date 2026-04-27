import pygame as py

py.init()
py.display.set_caption("Black&White")
root = py.display.set_mode((400, 400))
block_size = 20
blocks = [] 

def create_blocks():
    global blocks #making the value publicly available
    for i in range(20):
        row_of_blocks = []
        for j in range(20):
            row_of_blocks.append(False)
        blocks.append(row_of_blocks)


class Background():
    @staticmethod
    def create_background():
        for column in range(len(blocks)):
            for element in range(len(blocks[column])):
                if(blocks[column][element]): color = 'white'
                elif(not blocks[column][element]): color = 'black'
                py.draw.rect(root, color, py.Rect(column*20, element*20, 20, 20))

create_blocks()

running = True

while running:
    Background.create_background()
    for ev in py.event.get():
        if ev.type == py.QUIT:
            running = False
        if ev.type == py.MOUSEBUTTONUP:
            location = py.mouse.get_pos() #getting mouse's click position
            x = location[0]//20
            y = location[1]//20
            blocks[x][y] = not blocks[x][y] #change value to opposite
    py.display.update() #updating of main error
    
py.quit()

