import pygame
import math
from constants import *

class ModernPlayer:
    def __init__(self):
        self.width = 60
        self.height = 40
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - self.height - 20
        self.speed = PLAYER_SPEED
        self.thrust_animation = 0
        
    def move(self, direction: int):
        self.x += direction * self.speed
        self.x = max(0, min(self.x, SCREEN_WIDTH - self.width))
        
    def update(self):
        self.thrust_animation = (self.thrust_animation + 0.1) % (2 * math.pi)
        
    def draw(self, screen):
        # Draw modern spaceship
        points = [
            (self.x + self.width//2, self.y),  # nose
            (self.x + self.width, self.y + self.height),  # right bottom
            (self.x + self.width//2, self.y + self.height * 0.8),  # bottom middle
            (self.x, self.y + self.height),  # left bottom
        ]
        
        # Draw ship body
        pygame.draw.polygon(screen, BLUE, points)
        pygame.draw.polygon(screen, LIGHT_BLUE, points, 2)
        
        # Draw engine glow
        thrust_height = 10 + math.sin(self.thrust_animation) * 5
        thrust_points = [
            (self.x + self.width * 0.3, self.y + self.height),
            (self.x + self.width * 0.5, self.y + self.height + thrust_height),
            (self.x + self.width * 0.7, self.y + self.height)
        ]
        pygame.draw.polygon(screen, LIGHT_BLUE, thrust_points)

class ModernBullet:
    def __init__(self, x: int, y: int):
        self.width = 4
        self.height = 16
        self.x = x
        self.y = y
        self.speed = BULLET_SPEED
        self.trail_points = []
        
    def move(self):
        self.y -= self.speed
        self.trail_points.append((self.x + self.width/2, self.y + self.height))
        if len(self.trail_points) > 5:
            self.trail_points.pop(0)
            
    def draw(self, screen):
        # Draw energy beam
        pygame.draw.rect(screen, LIGHT_BLUE,
                        (self.x - 1, self.y, self.width + 2, self.height))
        pygame.draw.rect(screen, BLUE,
                        (self.x, self.y, self.width, self.height))