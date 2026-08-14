import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from circleshape import CircleShape
from constants import LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface, color: str = "white", x: float = None, y: float = None, radius: float = None, line_width: int = LINE_WIDTH) -> None:
        pygame.draw.circle(screen, color, (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
    