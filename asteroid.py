import pygame
from constants import *
from circleshape import CircleShape
from constants import LINE_WIDTH
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface, color: str = "white", x: float = None, y: float = None, radius: float = None, line_width: int = LINE_WIDTH) -> None:
        pygame.draw.circle(screen, color, (self.position.x, self.position.y), self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            vec1 = self.velocity.rotate(angle)
            vec2 = self.velocity.rotate(-angle)
            Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = vec1 * 1.2
            Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS).velocity = vec2 * 1.2
