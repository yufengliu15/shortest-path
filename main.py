import pygame

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLOCKSIZE = 20
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 800
GRID_WIDTH = 500
GRID_HEIGHT = 500

def drawGrid(screen):
    for y in range(0, GRID_WIDTH, BLOCKSIZE):
        for x in range (0, GRID_HEIGHT, BLOCKSIZE):
            rect = pygame.Rect(x,y,BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)
    return
         
def drawBlock(x,y,_colour, screen):
    for j in range(y, y + BLOCKSIZE, 1):
        for i in range(x, x + BLOCKSIZE, 1):
            screen.set_at((i,j),_colour)
    return
         
def updateGrid(x,y, screen, _colour):
    integerX = x // BLOCKSIZE
    integerY = y // BLOCKSIZE
    blockCoorX = integerX * BLOCKSIZE
    blockCoorY = integerY * BLOCKSIZE
    if (blockCoorX == 0 and blockCoorY == 0) or (blockCoorX == (GRID_WIDTH - BLOCKSIZE) and (blockCoorY == (GRID_HEIGHT - BLOCKSIZE))) or (x>= GRID_WIDTH):
        return
    drawBlock(blockCoorX,blockCoorY,_colour, screen)
            
def main():
    pygame.init()
    displayWindow = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    mousePos = None
    
    # start and finish blocks
    drawBlock(0,0,GREEN,displayWindow)
    drawBlock(GRID_WIDTH - BLOCKSIZE,GRID_HEIGHT - BLOCKSIZE, BLUE, displayWindow)
    
    while True:
        drawGrid(displayWindow)
               
        if pygame.mouse.get_pressed(num_buttons=3) == (1,0,0):
            mousePos = pygame.mouse.get_pos()
            updateGrid(mousePos[0], mousePos[1], displayWindow, RED)
        elif pygame.mouse.get_pressed(num_buttons=3) == (0,0,1):
            mousePos = pygame.mouse.get_pos()
            updateGrid(mousePos[0], mousePos[1], displayWindow, BLACK)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.update()

main()