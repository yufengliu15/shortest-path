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
    # prevents drawing on start and finish points
    if (blockCoorX == 0 and blockCoorY == 0) or (blockCoorX == (GRID_WIDTH - BLOCKSIZE) and (blockCoorY == (GRID_HEIGHT - BLOCKSIZE))):
        return
    drawBlock(blockCoorX,blockCoorY,_colour, screen)

def text(screen,textToDisplay, location):
    pygame.font.init()
    textFont = pygame.font.SysFont('arialrounded', BLOCKSIZE)
    textSurface = textFont.render(textToDisplay, False, WHITE)
    screen.blit(textSurface, (location[0], location[1]))

def buttonPressed(mousePos, locationList, locationIndexNum):
    return (mousePos[0] >= locationList[locationIndexNum][0] and mousePos[0] <= (locationList[locationIndexNum][0] + locationList[locationIndexNum][2])) and ((mousePos[1] >= locationList[locationIndexNum][1]) and mousePos[1] <= (locationList[locationIndexNum][1] + locationList[locationIndexNum][3]))

def drawGui(screen):
    CHECKBOX_WIDTH_START = GRID_WIDTH + 2*BLOCKSIZE
    TEXT_WIDTH_START = GRID_WIDTH + 4 * BLOCKSIZE
    text(screen, 'Green = Start', (CHECKBOX_WIDTH_START, BLOCKSIZE))
    text(screen, 'Blue = Finish', (CHECKBOX_WIDTH_START, 2*BLOCKSIZE))
    text(screen, 'Red = Walls', (CHECKBOX_WIDTH_START, 3*BLOCKSIZE))
    text(screen, 'Left Click to Draw', (CHECKBOX_WIDTH_START, 4*BLOCKSIZE))
    text(screen, 'Right Click to Remove', (CHECKBOX_WIDTH_START, 5*BLOCKSIZE))
    
    visualizationCheckLocation = [CHECKBOX_WIDTH_START, 7*BLOCKSIZE, BLOCKSIZE, BLOCKSIZE]
    visualizationCheck = pygame.Rect(visualizationCheckLocation[0], visualizationCheckLocation[1], visualizationCheckLocation[2], visualizationCheckLocation[3])
    pygame.draw.rect(screen, WHITE, visualizationCheck, 1)
    text(screen, 'Visualization?', (TEXT_WIDTH_START, 7*BLOCKSIZE-2))
    
    runButtonLocation = [(GRID_WIDTH + WINDOW_WIDTH)/2 - 4*BLOCKSIZE, GRID_HEIGHT - 4*BLOCKSIZE, 8 * BLOCKSIZE, 3*BLOCKSIZE]
    runButton = pygame.Rect(runButtonLocation[0], runButtonLocation[1], runButtonLocation[2], runButtonLocation[3])
    pygame.draw.rect(screen, WHITE, runButton, 1)
    text(screen, 'RUN', ((GRID_WIDTH + WINDOW_WIDTH)/2 - BLOCKSIZE, GRID_HEIGHT - 3*BLOCKSIZE))
    
    locationList = [visualizationCheckLocation, runButtonLocation]
    
    return locationList
    
def main():
    pygame.init()
    displayWindow = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    mousePos = None
    visualizationCheck = False
    
    # start and finish blocks
    drawBlock(0,0,GREEN,displayWindow)
    drawBlock(GRID_WIDTH - BLOCKSIZE,GRID_HEIGHT - BLOCKSIZE, BLUE, displayWindow)
    
    while True:
        drawGrid(displayWindow)
        locationList = drawGui(displayWindow)
        # if a left click occurs
        if pygame.mouse.get_pressed(num_buttons=3) == (1,0,0):
            mousePos = pygame.mouse.get_pos()
            if not(mousePos[0] >= GRID_WIDTH):
                updateGrid(mousePos[0], mousePos[1], displayWindow, RED)
            else:
                # if user clicks on visualization checkbox
                if buttonPressed(mousePos, locationList, 0):
                    if visualizationCheck:
                        updateGrid(mousePos[0], mousePos[1], displayWindow, BLACK)
                    else:
                        updateGrid(mousePos[0], mousePos[1], displayWindow, RED)
                    visualizationCheck = not(visualizationCheck)
                    pygame.display.update()
                    pygame.time.delay(100)
                # if user clicks on run button
                elif buttonPressed(mousePos,locationList,1):
                    print ("RUNNING")
                    pygame.time.delay(100)
        # if a right click occurs
        elif pygame.mouse.get_pressed(num_buttons=3) == (0,0,1):
            mousePos = pygame.mouse.get_pos()
            if not(mousePos[0] >= GRID_WIDTH):
                updateGrid(mousePos[0], mousePos[1], displayWindow, BLACK)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.update()

main()