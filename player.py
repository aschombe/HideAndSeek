import pygame
import math

FPS = 60


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color, radius, canSee):
        self.x = x
        self.y = y
        self.color = color

        # Direction will be between 0 and 2pi
        self.direction = 0
        self.radius = 10
        self.canSee = canSee

        self.image = pygame.Surface([radius * 2, radius * 2])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(
            surface,
            (255, 255, 255),
            (
                int(self.x + math.cos(self.direction) * self.radius),
                int(self.y + math.sin(self.direction) * self.radius),
            ),
            3,
        )

    def move(self, magnitude, rotation_input):
        self.x += math.cos(self.direction) * magnitude / FPS
        self.y += math.sin(self.direction) * magnitude / FPS
        self.turn(rotation_input)

        # Keeps the player in the screen
        if self.x + self.radius > 500:
            self.x = 500 - self.radius
        elif self.x - self.radius < 0:
            self.x = 0 + self.radius
        if self.y + self.radius > 500:
            self.y = 500 - self.radius
        elif self.y - self.radius < 0:
            self.y = 0 + self.radius

    # Rotates the player
    def turn(self, rotation):
        self.direction += rotation / FPS
        self.direction %= 2 * math.pi
        # make self.direction between -pi and pi
        if self.direction > math.pi:
            self.direction -= 2 * math.pi
        elif self.direction < -math.pi:
            self.direction += 2 * math.pi

    # Returns true if the player can see the other player
    def sees(self, otherPlayer, walls, surface=None):
        if self.canSee:
            # list of lines that each connect to a pixel on the other player
            lines = []
            for x in range(int(otherPlayer.x - otherPlayer.radius), int(otherPlayer.x + otherPlayer.radius)):
                y = math.sqrt(abs(otherPlayer.radius**2 - (x - otherPlayer.x) ** 2)) + otherPlayer.y
                other_y = -math.sqrt(abs(otherPlayer.radius**2 - (x - otherPlayer.x) ** 2)) + otherPlayer.y
                lines.append((self.x, self.y, x, y))
                lines.append((self.x, self.y, x, other_y))

            # if any line intersect with a wall, return false
            found = False
            for line in lines:
                clipping_with_any = False
                for wall in walls:
                    if not wall.rect.clipline(line[0], line[1], line[2], line[3]):
                        found = True
                    else:
                        clipping_with_any = True

                current_direction = math.atan2(otherPlayer.y - self.y, otherPlayer.x - self.x)
                if not clipping_with_any and (
                    abs(current_direction - self.direction) < math.pi / 9
                    or abs(current_direction - self.direction) > 2 * math.pi - math.pi / 9
                ):
                    if surface is not None:
                        pygame.draw.line(surface, (0, 255, 0), (line[0], line[1]), (line[2], line[3]), 1)
                elif not clipping_with_any:
                    if surface is not None:
                        pygame.draw.line(surface, (255, 255, 0), (line[0], line[1]), (line[2], line[3]), 1)
                else:
                    if surface is not None:
                        pygame.draw.line(surface, (255, 0, 0), (line[0], line[1]), (line[2], line[3]), 1)

            current_direction = 0
            current_direction = math.atan2(otherPlayer.y - self.y, otherPlayer.x - self.x)

            # If the average direction is within 20 degrees of the player's direction, return true
            if not clipping_with_any:
                if (
                    abs(current_direction - self.direction) < math.pi / 9
                    or abs(current_direction - self.direction) > 2 * math.pi - math.pi / 9
                ):
                    return found

            return False
        else:
            return False

    # def collision_player(self, otherPlayer):
    #     # Circle sprite collision
    #     if math.sqrt((self.x - otherPlayer.x) ** 2 + (self.y - otherPlayer.y) ** 2) < self.radius + otherPlayer.radius:
    #         self.x = otherPlayer.x + math.cos(self.direction) * (self.radius + otherPlayer.radius)
    #         self.y = otherPlayer.y + math.sin(self.direction) * (self.radius + otherPlayer.radius)

    def collision_wall(self, walls):
        for wall in walls:
            if self.x + self.radius >= wall.rect.x and self.x - self.radius <= wall.rect.x + wall.rect.width:
                if self.y + self.radius >= wall.rect.y and self.y - self.radius <= wall.rect.y + wall.rect.height:
                    if self.x + self.radius >= wall.rect.x and self.x - self.radius <= wall.rect.x + wall.rect.width:
                        if (
                            self.y + self.radius >= wall.rect.y
                            and self.y - self.radius <= wall.rect.y + wall.rect.height
                        ):
                            if self.x > wall.rect.x + wall.rect.width:
                                self.x = wall.rect.x + wall.rect.width + self.radius
                            elif self.x < wall.rect.x:
                                self.x = wall.rect.x - self.radius
                            elif self.y > wall.rect.y + wall.rect.height:
                                self.y = wall.rect.y + wall.rect.height + self.radius
                            elif self.y < wall.rect.y:
                                self.y = wall.rect.y - self.radius
