import pygame as pygame
import sys
from settings import *
from sprites import *
import os

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.load_data()
        self.keyFound = False

    def load_data(self):
        pass

    def new(self):
        #Initialise toutes les variables et commence une nouvelle instance du jeu
        self.allSprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.player = Player(self, 10, 10)
        self.door = Door(self, 30, 20)
        self.key = Key(self,20,10)
        self.camera = Camera(self, 20, 20, "up")
        self.view = View(self, 18, 18)

    def run(self):
        self.playing = True
        #On raffraichit tant que le programme tourne
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.mouvement()
            self.update()
            self.draw()
            self.keySystem()
            self.detection()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.allSprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, FLOORGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, FLOORGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BACKGROUNDCOLOR)
        self.draw_grid()
        self.allSprites.draw(self.screen)
        pygame.display.flip()

    def mouvement(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_LEFT:
                    self.player.move(directionX=-1)
                if event.key == pygame.K_RIGHT:
                    self.player.move(directionX=1)
                if event.key == pygame.K_UP:
                    self.player.move(directionY=-1)
                if event.key == pygame.K_DOWN:
                    self.player.move(directionY=1)

    def keySystem(self):
        if self.player.rect.colliderect(self.key.rect):
            self.keyFound = True
            print("True")

        if self.keyFound == True:
            pass

    def detection(self):
        if self.view.x <= self.player.x < self.view.x1 and self.view.y <= self.player.y < self.view.y1:
            print("detecté")
            self.view.image.fill(RED)
            self.camera.image = pygame.image.load('sprites\camera\camera_detecté\camera_up.png').convert_alpha()
        pass

game = Game()
while True:
    game.new()
    game.run()
