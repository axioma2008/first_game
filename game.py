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
        self.birds_call_down = 0
        self.background = pygame.image.load("images/sky.png")

    def new(self):
        # start a new game
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        # Game Loop
        while self.running:
            self.clock.tick(FPS)
            self.create_bird()
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
                self.running = False

    def draw(self):
        # Game Loop - draw
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        self.birds_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()

    def create_bird(self):
        if self.birds_call_down == 120:
            bird = Bird()
            self.birds_sprites.add(bird)
            self.birds_call_down = 0
        self.birds_call_down += 1


player = Plane()
g = Game(player)
while g.running:
    g.new()
pygame.quit()
