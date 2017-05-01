import pygame
import random

black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red = ( 255,   0,   0)
blue = (   0,   0, 255)

pygame.init()

grid = [[[0, 0] for i in range(9)] for j in range(9)]
num_of_mines = 10
while num_of_mines > 0:
    x = random.randint(0, 8)
    y = random.randint(0 ,8)
    if grid[x][y][0] != 9:
        grid[x][y][0] = 9
        num_of_mines -= 1

for i in range(9):
    for j in range(9):
        num_around = 0
        if grid[i][j][0] == 0:
            if i > 0 and grid[i - 1][j][0] == 9:
                num_around += 1

            if i < 8 and grid[i + 1][j][0] == 9:
                num_around += 1

            if j > 0 and grid[i][j - 1][0] == 9:
                num_around += 1

            if j < 8 and grid[i][j + 1][0] == 9:
                num_around += 1

            if i > 0 and j > 0 and grid[i - 1][j - 1][0] == 9:
                num_around += 1

            if i < 8 and j < 8 and grid[i + 1][j + 1][0] == 9:
                num_around += 1

            if i > 0 and j < 8 and grid[i - 1][j + 1][0] == 9:
                num_around += 1

            if i < 8 and j > 0 and grid[i + 1][j - 1][0] == 9:
                num_around += 1

            grid[i][j][0] = num_around

def open_grid(i, j):
    if grid[i][j][1] == 0:
        grid[i][j][1] = 1
        if grid[i][j][0] == 0:
            if i > 0 and grid[i - 1][j][1] != 2:
                grid[i - 1][j][1] == 1
                if grid[i - 1][j][0] == 0:
                    open_grid(i - 1, j)

            if i < 8 and grid[i + 1][j][1] != 2:
                grid[i + 1][j][1] == 1
                if grid[i + 1][j][0] == 0:
                    open_grid(i + 1, j)

            if j > 0 and grid[i][j - 1][1] != 2:
                grid[i][j - 1][1] == 1
                if grid[i][j - 1][0] == 0:
                    open_grid(i, j - 1)

            if j < 8 and grid[i][j + 1][1] != 2:
                grid[i][j + 1][1] == 1
                if grid[i][j + 1][0] == 0:
                    open_grid(i, j + 1)

            if i > 0 and j > 0 and grid[i - 1][j - 1][1] != 2:
                grid[i - 1][j - 1][1] = 1
                if grid[i - 1][j - 1][0] == 0:
                    open_grid(i - 1, j - 1)

            if i < 8 and j < 8 and grid[i + 1][j + 1][1] != 2:
                grid[i + 1][j + 1][1] = 1
                if grid[i + 1][j + 1][0] == 0:
                    open_grid(i + 1, j + 1)

            if i > 0 and j < 8 and grid[i - 1][j + 1][1] != 2:
                grid[i - 1][j + 1][1] = 1
                if grid[i - 1][j + 1][0] == 0:
                    open_grid(i - 1, j + 1)

            if i < 8 and j > 0 and grid[i + 1][j - 1][1] != 2:
                grid[i + 1][j - 1][1] = 1
                if grid[i + 1][j - 1][0] == 0:
                    open_grid(i + 1, j - 1)

font = pygame.font.Font(None, 25)

size = (500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Minesweeper")

clock = pygame.time.Clock()

done = False

side = 30
x = y = 10
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            y = (pos[0] - 100) / side
            x = (pos[1] - 100) / side
            if event.button == 1:
                open_grid(x, y)
            elif event.button == 3:
                if grid[x][y][1] == 0:
                    grid[x][y][1] = 2
                elif grid[x][y][1] == 2:
                    grid[x][y][1] = 0
            #print x, y


    # Logic here

    if x in range(9) and y in range(9):
        if grid[x][y][0] == 9:
            print 'Game over! You lose'
            done = True

    count = 0

    for i in range(9):
        for j in range(9):
            if grid[i][j][1] == 1:
                count += 1

    if count == 71:
        print 'You win!'
        done = True

    screen.fill(white)
    # Draw here
    for i in range(9):
        for j in range(9):
            if grid[i][j][1] == 1:
                if grid[i][j][0] == 0:
                    color = white
                    pygame.draw.rect(screen, color, [100 + side * j, 100 + side * i, side, side], 0)
                else:
                    number = font.render(str(grid[i][j][0]), False, black)
                    screen.blit(number, [100 + (j + 0.3) * side, 100 + (i + 0.3) * side])
            elif grid[i][j][1] == 2:
                color = red
                pygame.draw.rect(screen, color, [100 + side * j, 100 + side * i, side, side], 0)
            else:
                color = blue
                pygame.draw.rect(screen, color, [100 + side * j, 100 + side * i, side, side], 0)
            #number = font.render(str(grid[i][j][0]), False, black)
            #screen.blit(number, [100 + (j + 0.3) * side, 100 + (i + 0.3) * side])
            pygame.draw.rect(screen, black, [100 + side * j, 100 + side * i, side, side], 2)

    pygame.display.flip()

    clock.tick(10)

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    screen.fill(white)
    # Draw here
    for i in range(9):
        for j in range(9):
            if grid[i][j][1] == 1:
                if grid[i][j][0] == 0:
                    color = white
                    pygame.draw.rect(screen, color, [100 + side * j, 100 + side * i, side, side], 0)
                else:
                    number = font.render(str(grid[i][j][0]), False, black)
                    screen.blit(number, [100 + (j + 0.3) * side, 100 + (i + 0.3) * side])
            elif grid[i][j][0] == 9:
                color = red
                pygame.draw.rect(screen, color, [100 + side * j, 100 + side * i, side, side], 0)
            else:
                color = blue
                pygame.draw.rect(screen, color, [100 + side * j, 100 + side * i, side, side], 0)
            #number = font.render(str(grid[i][j][0]), False, black)
            #screen.blit(number, [100 + (j + 0.3) * side, 100 + (i + 0.3) * side])
            pygame.draw.rect(screen, black, [100 + side * j, 100 + side * i, side, side], 2)

    pygame.display.flip()

    clock.tick(10)
pygame.quit()
