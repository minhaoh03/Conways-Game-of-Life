import pygame
from copy import copy, deepcopy
import time

BLACK = (0,0,0)
GREY = (211,211,211)
WHITE = (255,255,255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Size of each square
gridSize = 20

# Method for making an empty array for matrix, alsoDraw allow to also draw the empty parameter
def makeEmpty(matrix, alsoDraw):
    for y in range(0, SCREEN_HEIGHT, 20):
        inMatrix = []
        for x in range(0, SCREEN_WIDTH, 20):
            inMatrix.append(False)
            if alsoDraw:
                pygame.draw.rect(SCREEN, BLACK, (x, y, gridSize - 1, gridSize - 1) )
        matrix.append(inMatrix)

# Method for updating each grid in grids
def update(grids):
    updatedGrids = []
    makeEmpty(updatedGrids, False)                  # Make an empty updated grid to store new grids that will later be displayed
    
    for y in range(0, SCREEN_HEIGHT, 20):
        for x in range(0, SCREEN_WIDTH, 20):
            neighbors = 0
            if x//20 != 0 and grids[y//20][x//20-1]:        # Left
                neighbors+=1
            if y//20 != 0 and grids[y//20-1][x//20]:        # Up
                neighbors+=1
            if x//20 <= len(grids[0])-2 and grids[y//20][x//20+1]:      # Right
                neighbors+=1
            if y//20 <= len(grids)-2 and grids[y//20+1][x//20]:         # Down
                neighbors+=1
            if x//20 != 0 and y//20 != 0 and grids[y//20-1][x//20-1]:   # Top Left
                neighbors+=1
            if x//20 != 0 and y//20 <= len(grids)-2 and grids[y//20+1][x//20-1]:    # Bottom Left
                neighbors+=1
            if y//20 != 0 and x//20 <= len(grids[0])-2 and grids[y//20-1][x//20+1]:     #Top Right
                neighbors+=1
            if x//20 <= len(grids[0])-2 and y//20 <= len(grids)-2 and grids[y//20+1][x//20+1]:      #Bottom Right
                neighbors+=1
            
            # Rules for Conway's Game of Life
            if grids[y//20][x//20] and (neighbors < 2 or neighbors > 3):
                updatedGrids[y//20][x//20] = False
                pygame.draw.rect(SCREEN, BLACK, (x, y, gridSize - 1, gridSize - 1))             # Draw for each time a grid is updated
            elif (not grids[y//20][x//20] and neighbors == 3) or (grids[y//20][x//20] and neighbors == 2 or neighbors == 3):
                updatedGrids[y//20][x//20] = True
                pygame.draw.rect(SCREEN, WHITE, (x, y, gridSize - 1, gridSize - 1))             # Draw for each time a grid is updated

    return updatedGrids         # return the updated grids after following the rules

def main():
    pygame.init()
    
    # grids is the actual board, running is to continue the program, start is to pause or unpause the game
    grids = []
    running = True
    start = False

    # to setup the board in the beginning
    SCREEN.fill(GREY)
    makeEmpty(grids, True)
    
    # update the board with latest changes
    pygame.display.flip()
    pygame.display.update() 
    
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       # Quit when the X button on the top right is pressed
                running = False
            elif event.type == pygame.KEYDOWN:          
                if event.key == pygame.K_SPACE:         # If space is pressed on the keyboard, pause/unpause the game
                    start = not start
                    update(grids)
                    pygame.display.update()
                
            if pygame.mouse.get_pressed()[0]:           # If the mouse left-click button is pressed, update the board with the new alive grids
                coord = pygame.mouse.get_pos()
                grids[coord[1] // 20][coord[0] // 20] = True
                print(coord[1] // 20 , coord[0] // 20)
                pygame.draw.rect(SCREEN, WHITE, pygame.Rect(coord[0]-coord[0]%20, coord[1]-coord[1]%20, gridSize - 1, gridSize - 1))
                pygame.display.update()
        
        if start:                       # Once the game has started, continuously update the board
            grids = update(grids)           # Update
            pygame.display.update()
            time.sleep(.1)              # Cooldown timer for each update
            
        pygame.display.update()
        
if __name__ == "__main__":
    main()
    

    

            
