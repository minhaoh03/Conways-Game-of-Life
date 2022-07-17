import pygame
from copy import copy, deepcopy
import time

BLACK = (0,0,0)
GREY = (211,211,211)
WHITE = (255,255,255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

gridSize = 20

def makeEmpty(matrix, alsoDraw):
    for y in range(0, SCREEN_HEIGHT, 20):
        inMatrix = []
        for x in range(0, SCREEN_WIDTH, 20):
            inMatrix.append(False)
            if alsoDraw:
                pygame.draw.rect(SCREEN, BLACK, (x, y, gridSize - 1, gridSize - 1) )
        matrix.append(inMatrix)

def update(grids):
    updatedGrids = []
    makeEmpty(updatedGrids, False)
    for y in range(0, SCREEN_HEIGHT, 20):
        for x in range(0, SCREEN_WIDTH, 20):
            neighbors = 0
            if x//20 != 0 and grids[y//20][x//20-1]:
                neighbors+=1
            if y//20 != 0 and grids[y//20-1][x//20]:
                neighbors+=1
            if x//20 <= len(grids[0])-2 and grids[y//20][x//20+1]:
                neighbors+=1
            if y//20 <= len(grids)-2 and grids[y//20+1][x//20]:
                neighbors+=1
            if x//20 != 0 and y//20 != 0 and grids[y//20-1][x//20-1]:
                neighbors+=1
            if x//20 != 0 and y//20 <= len(grids)-2 and grids[y//20+1][x//20-1]:
                neighbors+=1
            if y//20 != 0 and x//20 <= len(grids[0])-2 and grids[y//20-1][x//20+1]:
                neighbors+=1
            if x//20 <= len(grids[0])-2 and y//20 <= len(grids)-2 and grids[y//20+1][x//20+1]:
                neighbors+=1
                
            if grids[y//20][x//20] and (neighbors < 2 or neighbors > 3):
                updatedGrids[y//20][x//20] = False
                pygame.draw.rect(SCREEN, BLACK, (x, y, gridSize - 1, gridSize - 1))
            elif (not grids[y//20][x//20] and neighbors == 3) or (grids[y//20][x//20] and neighbors == 2 or neighbors == 3):
                updatedGrids[y//20][x//20] = True
                pygame.draw.rect(SCREEN, WHITE, (x, y, gridSize - 1, gridSize - 1))

    return updatedGrids
            
                
def draw(x, y, alive):
    grid = pygame.Rect(x, y, gridSize - 1, gridSize - 1) 
    if alive:
        pygame.draw.rect(SCREEN, WHITE, grid)
    else:
        pygame.draw.rect(SCREEN, BLACK, grid)

def main():
    pygame.init()
    
    grids = []
    running = True
    start = False

    SCREEN.fill(GREY)
    makeEmpty(grids, True)
    
    pygame.display.flip()
    pygame.display.update()
    
    loop = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = not start
                    update(grids)
                    pygame.display.update()
                
            if pygame.mouse.get_pressed()[0]:
                coord = pygame.mouse.get_pos()
                grids[coord[1] // 20][coord[0] // 20] = True
                print(coord[1] // 20 , coord[0] // 20)
                draw(coord[0]-coord[0]%20, coord[1]-coord[1]%20, True)
                pygame.display.update()
        
        if start:
            grids = update(grids)
            pygame.display.update()
            time.sleep(.1)
            
        pygame.display.update()
        

main()
    

    

            
