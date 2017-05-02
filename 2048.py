import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("2048")

clock = pygame.time.Clock()

done = False
font = pygame.font.Font(None, 50)

grid = [[0 for i in range(4)] for j in range(4)]
initial = 2

def Generate():
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    if grid[x][y] == 0:
        grid[x][y] = random.choice([2, 4])
        return 1
    else:
        return 0

def Shift(arrow):
    if arrow == 1:
        for i in range(4):
            for j in range(4):
                if grid[i][j] != 0:
                    last = -1
                    for k in range(j):
                        if grid[i][k] != 0:
                            last = k
                    if last != -1 and grid[i][last] == grid[i][j]:
                        grid[i][last] += grid[i][j]
                        if last != j:
                            grid[i][j] = 0
                    last = -1
                    for k in range(j):
                        if grid[i][k] == 0:
                            last = k
                            break
                    if last != -1:
                        grid[i][last] = grid[i][j]
                        grid[i][j] = 0

    elif arrow == 2:
        for i in range(4):
            for j in range(3, -1, -1):
                if grid[i][j] != 0:
                    last = -1
                    for k in range(3, j, -1):
                        if grid[i][k] != 0:
                            last = k
                    if last != -1 and grid[i][last] == grid[i][j]:
                        grid[i][last] += grid[i][j]
                        if last != j:
                            grid[i][j] = 0
                    last = -1
                    for k in range(3, j, -1):
                        if grid[i][k] == 0:
                            last = k
                            break
                    if last != -1:
                        grid[i][last] = grid[i][j]
                        grid[i][j] = 0

    elif arrow == 3:
        for i in range(4):
            for j in range(4):
                if grid[j][i] != 0:
                    last = -1
                    for k in range(j):
                        if grid[k][i] != 0:
                            last = k
                    if last != -1 and grid[last][i] == grid[j][i]:
                        grid[last][i] += grid[j][i]
                        if last != j:
                            grid[j][i] = 0
                    last = -1
                    for k in range(j):
                        if grid[k][i] == 0:
                            last = k
                            break
                    if last != -1:
                        grid[last][i] = grid[j][i]
                        grid[j][i] = 0

    elif arrow == 4:
        for i in range(4):
            for j in range(3, -1, -1):
                if grid[j][i] != 0:
                    last = -1
                    for k in range(3, j, -1):
                        if grid[k][i] != 0:
                            last = k
                    if last != -1 and grid[last][i] == grid[j][i]:
                        grid[last][i] += grid[j][i]
                        if last != j:
                            grid[j][i] = 0
                    last = -1
                    for k in range(3, j, -1):
                        if grid[k][i] == 0:
                            last = k
                            break
                    if last != -1:
                        grid[last][i] = grid[j][i]
                        grid[j][i] = 0

while initial > 0:
    if Generate():
        initial -= 1

side = 100

while not done:
    keystroke = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keystroke = 1
            elif event.key == pygame.K_RIGHT:
                keystroke = 2
            elif event.key == pygame.K_UP:
                keystroke = 3
            elif event.key == pygame.K_DOWN:
                keystroke = 4

    # Logic here
    if keystroke != 0:
        Shift(keystroke)
        while 1:
            if Generate():
                break

    screen.fill(WHITE)
    # Draw here
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                number = font.render(str(grid[i][j]), True, BLACK)
                screen.blit(number, [50 + side * (j + 0.38), 50 + side * (i + 0.38)])
            pygame.draw.rect(screen, BLACK, [50 + side * j, 50 + side * i, side, side], 1)
    pygame.display.flip()

    clock.tick(10)
pygame.quit()
