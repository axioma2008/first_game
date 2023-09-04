import time

import pygame
from settings import *
from sprites import Plane, Bird


class Game:
    def __init__(self, player):
        # initialize game window, etc
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.player = player
        self.all_sprites = pygame.sprite.Group()
        self.birds_sprites = pygame.sprite.Group()
        self.running = True
        self.call_down = 0
        self.background = pygame.image.load("images/sky.png")
        self.score = 0
        self.font = pygame.font.Font(None, 14)

    def new(self):
        # start a new game
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        # Game Loop
        while self.running:
            self.clock.tick(FPS)
            self.create_bird()
            self.score_counter()

            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        self.birds_sprites.update()

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                print(self.score)
                self.running = False
        if pygame.sprite.spritecollideany(self.player, self.birds_sprites):
            self.show_end_screen()
            self.running = False
            print(self.score)

    def draw(self):
        # Game Loop - draw
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        self.birds_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        text = self.font.render(f"SCORE: {self.score}", True, BLACK)
        self.screen.blit(text, (0, 0))
        pygame.display.flip()

    def create_bird(self):
        if self.call_down == 120:
            bird = Bird()
            self.birds_sprites.add(bird)
            self.call_down = 0
        self.call_down += 1

    def score_counter(self):
        if self.call_down == 60:
            self.score += 2

    def show_start_screen(self):
        image = pygame.image.load('images/first_screen.png')
        self.screen.blit(image, (0, 0))
        pygame.display.flip()
        self.wait_for_key()

    def show_end_screen(self):
        image = pygame.image.load('images/2627196.png')
        self.screen.blit(image, (0, 0))
        pygame.display.flip()
        self.running = False
        self.wait_for_key()

    def wait_for_key(self):
        a = True
        while a:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    a = False
                if event.type == pygame.QUIT:
                    a = False
                    self.running = False


player = Plane()
g = Game(player)
g.show_start_screen()
while g.running:
    g.new()
pygame.quit()
