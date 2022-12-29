import pygame

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
BLOCKSIZE = 20
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

def drawGrid(screen):
    for y in range(0, WINDOW_WIDTH, BLOCKSIZE):
        for x in range (0, WINDOW_HEIGHT, BLOCKSIZE):
            rect = pygame.Rect(x,y,BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)
    return
         
def updateGrid(x,y, screen, colour):
    integerX = x // BLOCKSIZE
    integerY = y // BLOCKSIZE
    blockCoorX = integerX * BLOCKSIZE
    blockCoorY = integerY * BLOCKSIZE
    if (blockCoorX == 0 and blockCoorY == 0) or (blockCoorX == (WINDOW_WIDTH - BLOCKSIZE) and (blockCoorY == (WINDOW_HEIGHT - BLOCKSIZE))):
        return
    for y in range(blockCoorY, blockCoorY + BLOCKSIZE, 1):
        for x in range(blockCoorX, blockCoorX + BLOCKSIZE, 1):
            screen.set_at((x,y),colour)
            
def main():
    pygame.init()
    displayWindow = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    mousePos = None
    
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