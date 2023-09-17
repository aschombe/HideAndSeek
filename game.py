# import numpy as np
import pygame
import sys
import time

# import reinforcement_learning_from_scratch as rlfs
from wall import Wall
import player

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (255, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BROWN = (52, 28, 2)

height = 500
width = 500
max_frames = 1800
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Hide and Seek")
pygame.init()

FPS = 60
clock = pygame.time.Clock()


def run(hider, seeker, draw=False):
    if draw:
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Hide and Seek")

    # Set up board
    board = []
    for i in range(10):
        board.append([])
        for j in range(10):
            board[i].append(0)

    # Set up players
    seek = player.Player(50, 400, RED, 20, True)
    hide = player.Player(50, 50, BROWN, 20, False)

    characters = [seek, hide]
    models = [seeker, hider]

    # obstacles
    walls = []
    walls.append(Wall(0, 110, 100, 10, PURPLE))
    walls.append(Wall(160, 0, 10, 100, PURPLE))

    start_time = time.time()
    running = True
    frames = 0
    while running:
        now = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        if draw:
            # Draw the background onto the surface
            screen.fill(WHITE)

            # Draw the board onto the surface
            for i in range(10):
                pygame.draw.line(screen, BLACK, (0, i * 50), (500, i * 50))
                pygame.draw.line(screen, BLACK, (i * 50, 0), (i * 50, 500))

            for wall in walls:
                wall.draw(screen)

        seen = False
        for character in characters:
            if draw:
                character.draw(screen)
            character.collision_wall(walls)
            if character.canSee:
                if draw:
                    if character.sees(characters[1], walls, screen) == True:
                        seen = True
                elif character.sees(characters[1], walls) == True:
                    # end = time.time()
                    seen = True

        time_since_start = time.time() - start_time

        for model, character in zip(models, characters):
            magnitude, rotation = model.forward(frames / FPS)
            # if frames % 50 == 0:
            #     # if draw:
            #     #     print(magnitude, rotation)
            character.move(magnitude, rotation)

        # Update the display
        if draw:
            pygame.display.update()

        if draw == True:
            clock.tick(FPS)

        frames += 1
        if seen or frames > max_frames:
            end = time.time()
            running = False


    time_elapsed = end - start_time
    # print("Seeker Score: " + str(characters[0].score))
    # print("Hider Score: " + str(characters[1].score))
    # print("Time elapsed: " + str(time_elapsed))
    # print("Frames: " + str(frames))
    # print("Average FPS: " + str(frames / time_elapsed))
    return frames / FPS
