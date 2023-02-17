import random
import pygame
import maths


class Particle:
    def __init__(self, x, y, id, mols, chemical, temperature):
        self.x = x
        self.y = y
        self.speed_x = random.uniform(-5, 5)
        self.speed_y = random.uniform(-5, 5)
        self.id = id
        self.mols = mols
        self.chemical = chemical
        self.radius = maths.find_radius_from_volume(mols * chemical.molarVolume, 4, 10)
        self.state = chemical.state_STP
        self.temperature = temperature

        self.name = chemical.name

    def update(self, screen_width, screen_height, temperature):
        multiplier = 0
        if temperature > 0:
            multiplier = temperature/1000


        if self.state == "gas":
            self.x += self.speed_x*multiplier + random.uniform(-2, 2)
            self.y += self.speed_y*multiplier + random.uniform(-2, 2)
            self.radius = maths.find_radius_from_volume(self.mols * 22400, 4, 10)
        elif self.state == "noble":
            self.x += self.speed_x*5
            self.y += self.speed_y*5
        elif self.state == "liquid":
            self.x += random.uniform(-multiplier, multiplier) + self.speed_x*.02
            self.y += random.uniform(-multiplier, multiplier) + self.speed_y*.02
            self.radius = maths.find_radius_from_volume(self.mols * self.chemical.molarVolume, 4, 10)
        elif self.state == "solid":
            self.radius = maths.find_radius_from_volume(self.mols * self.chemical.molarVolume, 4, 10)
            pass


        if self.state != "noble":
            if self.x - (self.radius) <= 0:
                self.x = self.radius
                self.speed_x = -self.speed_x
            if self.x + (self.radius) >= screen_width:
                self.x = screen_width - self.radius
                self.speed_x = -self.speed_x
            if self.y - (self.radius) <= 0:
                self.y = self.radius
                self.speed_y = -self.speed_y
            if self.y + (self.radius) >= screen_height:
                self.y = screen_height - self.radius
                self.speed_y = -self.speed_y
            if self.x - (self.radius) <= 0 and self.x + (self.radius) >= screen_width:
                self.x = screen_width / 2
            if self.y - (self.radius) <= 0 and self.y + (self.radius) >= screen_height:
                self.y = screen_height / 2

    def draw(self, screen):
        draw_radius = self.radius
        draw_color = self.chemical.color
        draw_name = self.chemical.name
        dark_color = (max(0, draw_color[0] / 2), max(0, draw_color[1] / 2), max(0, draw_color[2] / 2))
        font = pygame.font.Font(None, 15, bold=True)
        text = font.render(draw_name, True, (255, 255, 255) if sum(draw_color) / 3 < 128 else (0, 0, 0), draw_color)


        if self.state == "gas" or self.state == "noble":
            pygame.draw.circle(screen, draw_color, (int(self.x), int(self.y)), draw_radius, 2)
            text = font.render(draw_name, True, (255, 255, 255))
        elif self.state == "liquid":
            pygame.draw.circle(screen, draw_color, (int(self.x), int(self.y)), draw_radius + 2, 2)
            pygame.draw.circle(screen, draw_color, (int(self.x), int(self.y)), draw_radius - 2)

        elif self.state == "solid":
            pygame.draw.circle(screen, draw_color, (int(self.x), int(self.y)), draw_radius)

        pygame.draw.circle(screen, dark_color, (int(self.x), int(self.y)), maths.find_radius_from_volume(self.chemical.molarVolume, 4, 10), 1)
        screen.blit(text, (int(self.x - text.get_width() / 2), int(self.y - text.get_height() / 2)))