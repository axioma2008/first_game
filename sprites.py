import pygame
from settings import *
import random


class Plane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/plane.png")
        self.rect = self.image.get_rect()
        self.rect.y = HEIGHT // 2 - self.rect.height // 2

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= 2.5
        if keys[pygame.K_DOWN] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += 2.5


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bird.png")
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - 40
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)

    def update(self) -> None:
        self.rect.x -= 1
        if self.rect.x < 0 - self.rect.width:
            self.kill()

