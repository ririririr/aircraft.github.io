import pygame
import math
from constants import *

class ExplosionEffect:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = 0
        self.max_radius = 40
        self.speed = 2
        self.active = True
        self.particles = [(math.cos(angle) * 20, math.sin(angle) * 20) 
                         for angle in range(0, 360, 30)]
        
    def update(self):
        self.radius += self.speed
        if self.radius >= self.max_radius:
            self.active = False
            
    def draw(self, screen):
        for dx, dy in self.particles:
            radius = self.radius / 2
            x = self.x + dx * (self.radius / self.max_radius)
            y = self.y + dy * (self.radius / self.max_radius)
            pygame.draw.circle(screen, self.color, (int(x), int(y)), int(radius))

class FeedbackText:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.alpha = 255
        self.active = True
        self.speed = 1
        
    def update(self):
        self.y -= self.speed
        self.alpha -= 5
        if self.alpha <= 0:
            self.active = False
            
    def draw(self, screen):
        text_surface = FONT_SMALL.render(self.text, True, self.color)
        text_surface.set_alpha(self.alpha)
        screen.blit(text_surface, (self.x, self.y))