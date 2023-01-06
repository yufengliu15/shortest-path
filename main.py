import pygame
from collections import deque # queue

# --------------------------- CONSTANTS (FEEL FREE TO CHANGE VALUES) ---------------------
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
BLOCKSIZE = 20
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 800
GRID_WIDTH = 500
GRID_HEIGHT = 500

# --------------------------- DRAWS USER GRID ----------------------------
def drawGrid(screen):
    for y in range(0, GRID_WIDTH, BLOCKSIZE):
        for x in range (0, GRID_HEIGHT, BLOCKSIZE):
            rect = pygame.Rect(x,y,BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)
    return

# --------------------------- FILLS BLOCKS WITH COLOUR -------------------
def drawBlock(x,y, screen,_colour):
    for j in range(y, y + BLOCKSIZE, 1):
        for i in range(x, x + BLOCKSIZE, 1):
            screen.set_at((i,j), _colour)
    return

# --------------------------- RETURNS BOOL BASED OFF OF INPUT COLOUR -----
def checkColour(coords,screen, _colour):
    if screen.get_at((coords[0],coords[1])) == _colour:
        return True
    return False

# --------------------------- CALCULATES BLOCK X & Y COORDS --------------
def updateGrid(x,y, screen, _colour):
    integerX = x // BLOCKSIZE
    integerY = y // BLOCKSIZE
    blockCoorX = integerX * BLOCKSIZE
    blockCoorY = integerY * BLOCKSIZE
    # prevents drawing on start and finish points
    if (blockCoorX == 0 and blockCoorY == 0) or (blockCoorX == (GRID_WIDTH - BLOCKSIZE) and (blockCoorY == (GRID_HEIGHT - BLOCKSIZE))):
        return
    drawBlock(blockCoorX,blockCoorY,screen, _colour)

# --------------------------- GENERATES TEXT -----------------------------
def text(screen,textToDisplay, location):
    pygame.font.init()
    textFont = pygame.font.SysFont('arialrounded', BLOCKSIZE)
    textSurface = textFont.render(textToDisplay, False, WHITE)
    screen.blit(textSurface, (location[0], location[1]))

# --------------------------- FINDS IF MOUSE CLICK IS WITHIN BUTTON ------
def buttonPressed(mousePos, locationList, locationIndexNum):
    return (mousePos[0] >= locationList[locationIndexNum][0] and mousePos[0] <= (locationList[locationIndexNum][0] + locationList[locationIndexNum][2])) and ((mousePos[1] >= locationList[locationIndexNum][1]) and mousePos[1] <= (locationList[locationIndexNum][1] + locationList[locationIndexNum][3]))

# --------------------------- GENERATES THE GUI SCREEN -------------------
def drawGui(screen, resetCheck):
    CHECKBOX_WIDTH_START = GRID_WIDTH + 2*BLOCKSIZE
    TEXT_WIDTH_START = GRID_WIDTH + 4 * BLOCKSIZE
    text(screen, 'Green = Start', (CHECKBOX_WIDTH_START, BLOCKSIZE))
    text(screen, 'Blue = Finish', (CHECKBOX_WIDTH_START, 2*BLOCKSIZE))
    text(screen, 'Red = Walls', (CHECKBOX_WIDTH_START, 3*BLOCKSIZE))
    text(screen, 'Left Click to Draw', (CHECKBOX_WIDTH_START, 4*BLOCKSIZE))
    text(screen, 'Right Click to Remove', (CHECKBOX_WIDTH_START, 5*BLOCKSIZE))
    
    if resetCheck:
        resetButtonLocation = [(GRID_WIDTH + WINDOW_WIDTH)/2 - 4*BLOCKSIZE, GRID_HEIGHT - 4*BLOCKSIZE, 8 * BLOCKSIZE, 3*BLOCKSIZE]
        resetButton = pygame.Rect(resetButtonLocation[0], resetButtonLocation[1], resetButtonLocation[2], resetButtonLocation[3])
        pygame.draw.rect(screen, WHITE, resetButton, 1)
        text(screen, 'RESET', ((GRID_WIDTH + WINDOW_WIDTH)/2 - 2*BLOCKSIZE, GRID_HEIGHT - 3*BLOCKSIZE))
        
        continueButtonLocation = [(GRID_WIDTH + WINDOW_WIDTH)/2 - 4*BLOCKSIZE, GRID_HEIGHT - 8 * BLOCKSIZE, 8*BLOCKSIZE, 3*BLOCKSIZE]
        continueButton = pygame.Rect(continueButtonLocation[0],continueButtonLocation[1],continueButtonLocation[2],continueButtonLocation[3])
        pygame.draw.rect(screen,WHITE, continueButton,1)
        text(screen, 'CONTINUE', ((GRID_WIDTH + WINDOW_WIDTH)/2 - 2.5*BLOCKSIZE, GRID_HEIGHT - 7 * BLOCKSIZE))
        
        locationList = [resetButtonLocation, continueButtonLocation]
    else:
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

# --------------------------- RESETS GUI ---------------------------------
def resetGui(screen):
    guiReset = pygame.Surface((WINDOW_WIDTH - GRID_WIDTH, GRID_HEIGHT))
    guiReset.fill(BLACK)
    screen.blit(guiReset,(GRID_WIDTH, 0))
    
# --------------------------- RESETS MAZE --------------------------------
def resetMaze(screen):
    characterMatrix = inputCharacterMatrix(screen)
    for y in range(len(characterMatrix)):
        for x in range(len(characterMatrix[y])):
            if characterMatrix[y][x] == 'C':
                drawBlock(x*BLOCKSIZE,y*BLOCKSIZE,screen, BLACK)
    
# --------------------------- CREATES A CHARACTER MATRIX OF THE GRID -----
def inputCharacterMatrix(screen):
    matrix = []
    for y in range(1,GRID_HEIGHT,BLOCKSIZE):
        tempMatrix = []
        for x in range(1,GRID_WIDTH, BLOCKSIZE):
            if checkColour((x,y), screen, RED):
                tempMatrix.append('W')
            elif checkColour((x,y), screen, BLACK):
                tempMatrix.append('P')
            elif checkColour((x,y),screen, GREEN):
                tempMatrix.append('S')
            elif checkColour((x,y), screen, BLUE):
                tempMatrix.append('F')
            elif checkColour((x,y),screen, CYAN):
                tempMatrix.append('C')
        matrix.append(tempMatrix)
    return matrix

def init2dArray(input):
    _visited = []
    for y in range(GRID_HEIGHT//BLOCKSIZE):
        tempVisited = []
        for x in range(GRID_WIDTH//BLOCKSIZE):
            tempVisited.append(input)
        _visited.append(tempVisited)
    return _visited

# --------------------------- SEARCHING ALGORITHM ------------------------
def searchAlgorithm(screen, visualizationCheck):
    # Global variables
    ROWS = GRID_HEIGHT / BLOCKSIZE
    COLUMNS = GRID_WIDTH / BLOCKSIZE
    characterMatrix = inputCharacterMatrix(screen)
    startR, startC = 0,0
    rowQ, columnQ = deque(), deque()
    # North, south, east, west direction vectors
    rowDirection = [-1,1,0,0]
    columnDirection = [0,0,1,-1]
    
    # Variables used to track the number of steps taken
    moveCount = 0
    nodesLeftInLayer = 1
    nodesInNextLayer = 0
    
    reachedEnd = False
    # rows x columns matrix to track whether a node has been visited
    visted = init2dArray(False)
    order = []
    prev = init2dArray(None)
    
    # Solving
    rowQ.append(startR)
    columnQ.append(startC)
    visted[startR][startC] = True
    while len(rowQ) > 0:
        rows = rowQ.popleft()
        columns = columnQ.popleft()
        if characterMatrix[rows][columns] == 'F':
            reachedEnd = True
            break
        # explores the neighbouring cells
        for i in range(4):
            rr = rows + rowDirection[i]
            cc = columns + columnDirection[i]
            # skip out of bounds locations
            if rr < 0 or cc < 0: continue
            if rr >= ROWS or cc >= COLUMNS: continue
            # skip visted locations or walls
            if visted[rr][cc]: continue
            if characterMatrix[rr][cc] == 'W': continue
            
            rowQ.append(rr)
            columnQ.append(cc)
            visted[rr][cc] = True
            if visualizationCheck:
                drawBlock(cc*BLOCKSIZE,rr*BLOCKSIZE,screen,CYAN)
                drawGrid(screen)
                pygame.display.update()
                pygame.time.delay(15)
            nodesInNextLayer += 1
            prev[rr][cc] = (rows,columns)
        # accounts for number of steps to get to exit
        nodesLeftInLayer -= 1
        if nodesLeftInLayer == 0:
            nodesLeftInLayer = nodesInNextLayer
            nodesInNextLayer = 0
            moveCount += 1
    if reachedEnd:
        #path = []
        #for i in prev:
        #    if i != None:
        #        path.append()
        return moveCount
    return -1


# --------------------------- MAIN ---------------------------------------
def main():
    pygame.init()
    displayWindow = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    mousePos = None
    visualizationCheck = False
    resetCheck = False
    
    while True:
        drawGrid(displayWindow)
        locationList = drawGui(displayWindow, resetCheck)
        # start and finish blocks
        drawBlock(0,0,displayWindow,GREEN)
        drawBlock(GRID_WIDTH - BLOCKSIZE,GRID_HEIGHT - BLOCKSIZE, displayWindow, BLUE)
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
                # ----------- ALGORITHM RUNNING ------------------------------------
                elif buttonPressed(mousePos,locationList,1):
                    result = searchAlgorithm(displayWindow, visualizationCheck)
                    if result == -1:
                        print ("Path to exit was blocked")
                    resetCheck = True
                    resetGui(displayWindow)
                    locationList = drawGui(displayWindow,resetCheck)
                    drawGrid(displayWindow)
                    pygame.display.update()
                    pygame.time.delay(100)
                    
                    while resetCheck:
                        for event in pygame.event.get():
                            if (event.type == pygame.MOUSEBUTTONDOWN) and event.button == 1:
                                mousePos = pygame.mouse.get_pos()
                                # if user clicks reset
                                if buttonPressed(mousePos,locationList,0):
                                    displayWindow.fill(BLACK)
                                    resetCheck = False
                                    pygame.time.delay(100)
                                    break
                                # if user clicks continue
                                elif buttonPressed(mousePos,locationList,1):
                                    resetGui(displayWindow)
                                    resetCheck = False
                                    pygame.time.delay(100)
                                    resetMaze(displayWindow)
                                    break
                            elif event.type == pygame.QUIT:
                                pygame.quit()
                    
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