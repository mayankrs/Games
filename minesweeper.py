import pygame
import random

black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
red = ( 255,   0,   0)
blue = (   0,   0, 255)

pygame.init()

grid = [[0 for i in range(9)] for j in range(9)]
num_of_mines = 10
while num_of_mines > 0:
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                if random.randint(0,9) == 9:
                    grid[i][j] = 9
                    num_of_mines -= 1

for i in range(9):
    for j in range(9):
        num_around = 0
        if grid[i][j] == 0:
            if i > 0 and grid[i - 1][j] == 9:
                num_around += 1

            if i < 8 and grid[i + 1][j] == 9:
                num_around += 1

            if j > 0 and grid[i][j - 1] == 9:
                num_around += 1

            if j < 8 and grid[i][j + 1] == 9:
                num_around += 1

            if i > 0 and j > 0 and grid[i - 1][j - 1] == 9:
                num_around += 1

            if i < 8 and j < 8 and grid[i + 1][j + 1] == 9:
                num_around += 1

            if i > 0 and j < 8 and grid[i - 1][j + 1] == 9:
                num_around += 1

            if i < 8 and j > 0 and grid[i + 1][j - 1] == 9:
                num_around += 1

            grid[i][j] = num_around

font = pygame.font.Font(None, 25)

size = (500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Minesweeper")

clock = pygame.time.Clock()

done = False

side = 30
x = y = 10
button = 2
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            y = (pos[0] - 100) / side
            x = (pos[1] - 100) / side
            if event.button == 1:
                button = 0
            elif event.button == 3:
                button = 1
            print x, y
    # Logic here

    if x in range(9) and y in range(9):
        if grid[x][y] == 9:
            print 'Game over! You lose'
            break

    screen.fill(white)
    # Draw here
    for i in range(9):
        for j in range(9):
            if button == 0 and i == x and y == j:
                number = font.render(str(grid[i][j]), False, black)
                screen.blit(number, [100 + (j + 0.3) * side, 100 + (i + 0.3) * side])
            elif button == 1 and i == x and y == j:
                color = red
                pygame.draw.rect(screen, color, [100 + side * j, 100 + side * i, side, side], 0)
            else:
                color = blue
                pygame.draw.rect(screen, color, [100 + side * j, 100 + side * i, side, side], 0)
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
            color = white
            #number = font.render(str(grid[i][j]), False, black)
            #screen.blit(number, [100 + (j + 0.3) * side, 100 + (i + 0.3) * side])
            pygame.draw.rect(screen, color, [100 + side * j, 100 + side * i, side, side], 0)
            pygame.draw.rect(screen, black, [100 + side * j, 100 + side * i, side, side], 2)

    pygame.display.flip()

    clock.tick(10)
pygame.quit()
