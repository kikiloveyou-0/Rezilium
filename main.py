import pygame as pygame
import sys
from settings import *
from sprites import *
from os import path

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.loadData()
        self.keyFound = False


    def loadData(self):
        gameFolder = path.dirname(__file__)
        self.mapData = []
        with open(path.join(gameFolder,'level1.txt'), 'rt') as f:
            for line in f:
                self.mapData.append(line)
 
    def new(self):
        #Initialise toutes les variables et commence une nouvelle instance du jeu
        self.allSprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.keyGroup = pygame.sprite.Group()
        #enumerate = return la valeur de la liste ET son index.
        for row, tiles in enumerate(self.mapData):
            for colone, tile in enumerate(tiles):
                if tile == 'w':
                    self.wall = Wall(self,colone, row)
                    
                if tile == 'c':
                    self.camera = Camera(self, colone, row, "up")

                if tile == 'k':
                    self.key = Key(self,colone,row)

                if tile == 'v':
                    self.view = View(self, colone, row)

                if tile == 'd':
                    self.door = Door(self, colone, row)

                if tile == 'p':
                    self.player = Player(self, colone, row)



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
            pygame.sprite.spritecollide(self.player, self.keyGroup, True)

    def detection(self):
        if self.view.x <= self.player.x < self.view.x1 and self.view.y <= self.player.y < self.view.y1:
            print("detecté")
            self.view.image.fill(RED)
            self.camera.image = pygame.image.load('Tiles/images/Tilemap_15.png').convert_alpha()
        pass
    
    def bouton_appuye(self):
        if self.bouton1.x == self.player and self.bouton1.y == self.player.y:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        print("appuye")
                        self.bouton1.image = pygame.image.load('sprites\outon\outon_bas.png').convert_alpha()
    pass


game = Game()
while True:
    game.new()
    game.run()
