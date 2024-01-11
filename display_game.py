import pygame
from Player import Player
from tkinter import simpledialog
from pygame.locals import *

pygame.init()

# Set up the window
window_height = 800
window_width = 800
window_surface = pygame.display.set_mode((window_width, window_height), 0, 32)
pygame.display.set_caption('Game')

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Grid
grid_size = 40
grid = []
for x in range(0, window_width, grid_size):
    for y in range(0, window_height, grid_size):
        grid.append((x, y))

# Walls
walls = []

hiders = []
seekers = []

# Clock
clock = pygame.time.Clock()

while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                exit()
            if event.key == ord('l'):
                #filename = input('Filename: ')
                filename = simpledialog.askstring('Filename', 'Enter the name of the level file')
                if filename != None and filename != '':
                    level_file = open(filename, 'r')
                    level_coord = []
                    for line in level_file:
                        for char in line:
                            if char != '\n':
                                level_coord.append(int(char))
                    level_file.close()

                    grid_coords = []
                    for x in range(0, window_width, grid_size):
                        for y in range(0, window_height, grid_size):
                            grid_coords.append((x, y))

                    walls = []
                    for i in range(len(level_coord)):
                        if level_coord[i] == 1:
                            walls.append(grid_coords[i])

                    for i in range(len(level_coord)):
                        if level_coord[i] == 2:
                            # player is position, color
                            hiders.append(Player(grid_coords[i], (0, 255, 0)))
                        elif level_coord[i] == 3:
                            seekers.append(Player(grid_coords[i], (0, 0, 255)))

    # Fill the background
    window_surface.fill(white)

    # Draw grid
    for x, y in grid:
        pygame.draw.rect(window_surface, black, (x, y, grid_size, grid_size), 1)

    # Draw walls
    for x, y in walls:
        pygame.draw.rect(window_surface, red, (x, y, grid_size, grid_size))

    # Draw players (pygame sprites) as circles
    for player in hiders:
        pygame.draw.circle(window_surface, player.color, player.position, player.radius)
    for player in seekers:
        pygame.draw.circle(window_surface, player.color, player.position, player.radius)

    #for player in players:
    #    pygame.draw.circle(window_surface, player.color, player.position, player.radius)

    # Update the display
    pygame.display.update()
    clock.tick(60)
