import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        # call the parent class (Sprite) constructor
        super().__init__()

        # make a wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # make our top-left corner the passed-in location
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
