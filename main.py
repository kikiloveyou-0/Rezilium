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
        #Initialise toutes les variables et commence une nouvelle instance du jeu mais uniquement pour le menu
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
        self.alive = True
        self.gamestart = False
        self.menu()

    def weirdnew(self):
        #Initialise toutes les variables et commence une nouvelle instance du jeu mais uniquement pour les respawns
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
        self.alive = True
        self.gamestart = True

    def menu(self):
        self.titre = Titre(self, 11, 10)
        self.fleches = Fleches(self, 1, 0.5)
        self.e = E(self, 8, 2.5)
        self.noms = Noms(self, 25, 19)
        self.pressEnter = PressEnter(self, 12.5, 12)

    def menu_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("test")
                    self.gamestart = True
                    game = Game()
                    while True:
                        game.weirdnew()
                        game.run()



    def run(self):
        self.playing = True
        #On raffraichit tant que le programme tourne
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.update()
            self.draw()

            if self.gamestart == False:
                self.menu_keys()
            # test si le jeu à commencé (si le joueur a appuyé sur entrée sur le menu), si oui l'autorise à se déplacer
            if self.gamestart == True:
                print("test")
                self.mouvement()
                self.keySystem()
                self.detection()
                self.death()


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
            self.camera.image = pygame.image.load('sprites\camera\camera_detecté\camera_up.png').convert_alpha()
            self.alive = False

    def death(self):
        if self.alive == False:
            print("vous êtes mort")
            game = Game()
            while True:
                game.weirdnew()
                game.run()

game = Game()
while True:
    game.new()
    game.run()
