# This is the level editor.  It allows users to place walls in a level and save.
# It also allows users to load levels and remove walls.
# left click draws walls, right click removes walls.
# Pressing 's' saves the level, pressing 'l' loads the level.
# Pressing 'c' clears the level.
# Pressing 'q' quits the program.

# The level editor will just be a box with a grid.  The user can click on the grid
# to place walls.  The walls will be saved in a list of tuples, where each tuple
# is a coordinate pair.  The level editor will use keyboard shortcuts to save and
# load levels.  The level editor will also have a key to clear the level.

import pygame
import sys
import math
import pickle
import time
import random
from pygame.locals import *
    
# Initialize pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 800
window_surface = pygame.display.set_mode((window_width, window_height), 0, 32)
pygame.display.set_caption('Level Editor')

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)
red = (255, 0, 0)

# Set up the grid
grid_size = 40
grid = []
for x in range(0, window_width, grid_size):
    for y in range(0, window_height, grid_size):
        grid.append((x, y))


# Set up the walls
walls = []

# Set up the clock
clock = pygame.time.Clock()

# Set up the mouse
mousex = 0
mousey = 0

# Set up the mouse buttons
left_button_down = False
right_button_down = False

quitting = False

# Set up the main loop
while quitting == False:
    # Set up the event loop
    for event in pygame.event.get():
        if event.type == QUIT:
            quitting = True
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                left_button_down = True
            elif event.button == 3:
                right_button_down = True
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                left_button_down = False
            elif event.button == 3:
                right_button_down = False
        elif event.type == KEYDOWN:
            if event.key == ord('s'):
                # Save the level
                filename = input('Enter the filename to save the level as: ') 

                # Create a list of all the grid coordinates
                grid_coords = []
                for x in range(0, window_width, grid_size):
                    for y in range(0, window_height, grid_size):
                        grid_coords.append((x, y))
                        
                # Create a list of all the walls
                wall_coords = []
                for x, y in walls:
                    wall_coords.append((x, y))
                    
                # Create a list of all the empty spaces
                empty_coords = []
                for x, y in grid_coords:
                    if (x, y) not in wall_coords:
                        empty_coords.append((x, y))

                # Create a list of all the coordinates in the level
                level_coords = []
                for x, y in grid_coords:
                    if (x, y) in wall_coords:
                        level_coords.append(1)
                    else:
                        level_coords.append(0)

                # Save the level to a text file
                level_file = open(filename, 'w')
                for i in range(0, len(level_coords), 40):
                    for j in range(0, 40):
                        level_file.write(str(level_coords[i + j]))
                    level_file.write('\n')
                level_file.close()
            elif event.key == ord('l'):
                # Load the level
                filename = input('Enter the filename to load the level from: ')
                
                # Open the level file
                level_file = open(filename, 'r')
                level_coords = []
                for line in level_file:
                    for char in line:
                        if char != '\n':
                            level_coords.append(int(char))
                level_file.close()
                
                # Create a list of all the grid coordinates
                grid_coords = []
                for x in range(0, window_width, grid_size):
                    for y in range(0, window_height, grid_size):
                        grid_coords.append((x, y))

                # Create a list of all the walls
                walls = []
                for i in range(0, len(level_coords)):
                    if level_coords[i] == 1:
                        walls.append(grid_coords[i])

            elif event.key == ord('c'):
                # Clear the level
                walls = []
            elif event.key == ord('q'):
                # Quit the program
                quitting = True

    # Draw the black background onto the surface
    window_surface.fill(black)

    # Draw the grid
    for x, y in grid:
        pygame.draw.rect(window_surface, gray, (x, y, grid_size, grid_size), 1)

    # The outer edges of the grid are walls by default
    for x in range(0, window_width, grid_size):
        pygame.draw.rect(window_surface, red, (x, 0, grid_size, grid_size))
        pygame.draw.rect(window_surface, red, (x, window_height - grid_size, grid_size, grid_size))
        walls.append((x, 0))
        walls.append((x, window_height - grid_size))

    for y in range(0, window_height, grid_size):
        pygame.draw.rect(window_surface, red, (0, y, grid_size, grid_size))
        pygame.draw.rect(window_surface, red, (window_width - grid_size, y, grid_size, grid_size))
        walls.append((0, y))
        walls.append((window_width - grid_size, y))

    # Draw the walls
    for x, y in walls:
        pygame.draw.rect(window_surface, red, (x, y, grid_size, grid_size))

    # Draw a wall at the mouse position as long as the mouse is held down
    while left_button_down:
        # Draw a wall at the mouse position
        mousex = int(math.floor(mousex / grid_size) * grid_size)
        mousey = int(math.floor(mousey / grid_size) * grid_size)
        if (mousex, mousey) not in walls:
            walls.append((mousex, mousey))
            pygame.draw.rect(window_surface, red, (mousex, mousey, grid_size, grid_size))
        # Update the display
        pygame.display.update()
        # Set the frame rate
        clock.tick(30)
        # Check for events
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                left_button_down = False
            elif event.type == KEYDOWN:
                if event.key == ord('q'):
                    quitting = True
                    left_button_down = False
                    right_button_down = False
                    break


    # Remove a wall at the mouse position as long as the mouse is held down
    while right_button_down:
        # Remove a wall at the mouse position
        mousex = int(math.floor(mousex / grid_size) * grid_size)
        mousey = int(math.floor(mousey / grid_size) * grid_size)
        if (mousex, mousey) in walls:
            walls.remove((mousex, mousey))
            pygame.draw.rect(window_surface, black, (mousex, mousey, grid_size, grid_size))
        # Update the display
        pygame.display.update()
        # Set the frame rate
        clock.tick(30)
        # Check for events
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                right_button_down = False
            elif event.type == KEYDOWN:
                if event.key == ord('q'):
                    quitting = True
                    left_button_down = False
                    right_button_down = False
                    break

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(30)

# Quit the program
pygame.quit()
sys.exit()
