import pygame
import math

def create_gradient_surface(width, height, color1, color2):
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    for y in range(height):
        ratio = y / height
        color = [
            color1[i] * (1 - ratio) + color2[i] * ratio
            for i in range(3)
        ]
        pygame.draw.line(surface, color, (0, y), (width, y))
    return surface

def draw_neon_text(surface, text, font, color, pos, glow_color, glow_radius=2):
    # Draw glow
    for offset in range(1, glow_radius + 1):
        glow_surface = font.render(text, True, glow_color)
        for dx, dy in [(-offset, 0), (offset, 0), (0, -offset), (0, offset)]:
            surface.blit(glow_surface, (pos[0] + dx, pos[1] + dy))
    
    # Draw main text
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)

def create_hexagon(radius, color):
    surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    points = []
    for i in range(6):
        angle = math.pi / 3 * i
        points.append((
            radius + radius * math.cos(angle),
            radius + radius * math.sin(angle)
        ))
    pygame.draw.polygon(surface, color, points)
    return surface