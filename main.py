import pygame as pygame
import sys
from settings import *
from sprites import *
from file import *
from os import path

class Game:
    def __init__(self):
        # on initialise python
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 100)
        self.loadData()
        self.keyFound = False
        self.doorOpen = False

    def loadData(self):
        self.currentLevel = 0
        gameFolder = path.dirname(__file__)
        self.mapData = []
        # les niveaux sont codés dans des fichiers txt, on apporte le fichier txt du niveau 1
        with open(path.join(gameFolder,'level1.txt'), 'rt') as f:
            for line in f:
                self.mapData.append(line)



    def new(self):
        #Initialise toutes les variables et commence une nouvelle instance du jeu mais uniquement pour le menu
        # on créer les groupes de sprites
        self.allSprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.boxes = pygame.sprite.Group()
        self.keyGroup = pygame.sprite.Group()
        self.cameras = pygame.sprite.Group()
        self.views = pygame.sprite.Group()
        self.door = pygame.sprite.Group()
        #enumerate = return la valeur de la liste ET son index.
        # on passe sur le fichier txt et selon le caractère, on créer des sprites
        for row, tiles in enumerate(self.mapData):
            for colone, tile in enumerate(tiles):
                if tile == 'w':
                    self.wall = Wall(self,colone, row)

                if tile == '8':
                    self.camera = Camera(self, colone, row, "up")
                if tile == '2':
                    self.camera = Camera(self, colone, row, "down")
                if tile == '6':
                    self.camera = Camera(self, colone, row, "right")
                if tile == '4':
                    self.camera = Camera(self, colone, row, "left")

                if tile == 'l':
                    self.plaque = Plaque(self,colone,row)

                if tile == 'k':
                    self.key = Key(self,colone,row)

                if tile == 'v':
                    self.view = View(self, colone, row)

                if tile == 'd':
                    self.door = Door(self, colone, row)

                if tile == 'p':
                    self.player = Player(self, colone, row)

                if tile == 'b':
                    self.box = Box(self,colone, row)

                if tile == 'f':
                    self.follower = Follower(self,colone, row)

                if tile == 'u':
                    self.bouton = Bouton(self,colone, row, "up")

        # on créer les champs de vision des caméras
        self.view1 = View(self, 9, 15)
        self.view2 = View(self, 15, 16)
        # on rend le joueur vivant, mais le jeu ne commence pas, on initialise le menu
        self.alive = True
        self.gamestart = False
        self.menu()
        
    def respawnnew(self):
        #Initialise toutes les variables et commence une nouvelle instance du jeu mais uniquement pour les respawns
        # on créer les groupes de sprites
        self.allSprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.boxes = pygame.sprite.Group()
        self.keyGroup = pygame.sprite.Group()
        self.cameras = pygame.sprite.Group()
        self.views = pygame.sprite.Group()
        self.bouton = pygame.sprite.Group()
        #enumerate = return la valeur de la liste ET son index.
        # on passe sur le fichier txt et selon le caractère, on créer des sprites
        for row, tiles in enumerate(self.mapData):
            for colone, tile in enumerate(tiles):
                if tile == 'w':
                    self.wall = Wall(self,colone, row)

                if tile == '8':
                    self.camera = Camera(self, colone, row, "up")
                if tile == '2':
                    self.camera = Camera(self, colone, row, "down")
                if tile == '6':
                    self.camera = Camera(self, colone, row, "right")
                if tile == '4':
                    self.camera = Camera(self, colone, row, "left")

                if tile == 'l':
                    self.plaque = Plaque(self,colone,row)

                if tile == 'k':
                    self.key = Key(self,colone,row)

                if tile == 'v':
                    self.view = View(self, colone, row)

                if tile == 'd':
                    self.door = Door(self, colone, row)

                if tile == 'p':
                    self.player = Player(self, colone, row)

                if tile == 'b':
                    self.box = Box(self,colone, row)

                if tile == 'f':
                    self.follower = Follower(self,colone, row)

                if tile == 'u':
                    self.bouton = Bouton(self,colone, row, "up")

        # on créer les champs de vision des caméras
        self.view1 = View(self, 9, 15)
        self.view2 = View(self, 15, 16)
        # on rend le joueur vivant, le jeu commence, on initialise pas le menu
        self.activationCamera = True
        self.alive = True
        self.gamestart = True
        self.fileFollower = File()


    def menu(self):
        # les élements du menu et leurs placements
        self.titre = Titre(self, 11, 10)
        self.fleches = Fleches(self, 1, 0.5)
        self.e = E(self, 8, 2.5)
        self.noms = Noms(self, 25, 19)
        self.pressEnter = PressEnter(self, 12.5, 12)

    def menu_keys(self):
        # quand on appuie sur entrée, le jeu se re-créer, sans le menu avec la méthode respawnnew
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("test")
                    self.gamestart = True
                    game = Game()
                    while True:
                        game.respawnnew()
                        game.run()



    def run(self):
        self.playing = True
        #On raffraichit tant que le programme tourne
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.update()
            self.draw()
            # si le jeu n'a pas commencé, on peut le commencer en appuyant sur entrée
            if self.gamestart == False:
                self.menu_keys()
            '''' test si le jeu à commencé (si le joueur a appuyé sur entrée sur le menu), si oui l'autorise à se déplacer, et initialise les clés, la mort
            la détection par les plaques de pression et la desactivation des caméras'''
            if self.gamestart == True:
                self.mouvement()
                self.mouvementFollower()
                self.keySystem()
                self.doorSystem()

                if self.activationCamera == True:
                    self.detection()

                self.death()
                self.plaqueDetection()
                self.desactivateCameras()


    def quit(self):
        # méthode appeler si l'on doit quitter
        pygame.quit()
        sys.exit()

    def update(self):
        # méthode rafraichissant les sprites
        self.allSprites.update()

    def draw_grid(self):
        # méthode mettant en place la grille
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, FLOORGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, FLOORGREY, (0, y), (WIDTH, y))

    def draw(self):
        # méthode dessinant le background, la grille et les sprites
        self.screen.fill(BACKGROUNDCOLOR)
        self.draw_grid()
        self.allSprites.draw(self.screen)
        pygame.display.flip()

    def mouvement(self):
        # méthode récuperant les inputs du joueur pour les convertir en mouvement pour les sprites du joueur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

                if event.key == pygame.K_LEFT:
                    self.player.move(directionX=-1)
                    self.fileFollower.enfiler("left")
                    if self.player.push():
                        self.box.move(directionX=-1)
                if event.key == pygame.K_RIGHT:
                    self.player.move(directionX=1)
                    self.fileFollower.enfiler("right")
                    if self.player.push():
                        self.box.move(directionX=1)
                if event.key == pygame.K_UP:
                    self.player.move(directionY=-1)
                    self.fileFollower.enfiler("up")
                    if self.player.push():
                        self.box.move(directionY=-1)
                if event.key == pygame.K_DOWN:
                    self.player.move(directionY=1)
                    self.fileFollower.enfiler("down")
                    if self.player.push():
                        self.box.move(directionY=1)

                if event.key == pygame.K_e:
                    if self.bouton.x == self.player.x and self.bouton.y == self.player.y:
                        print("appuye")
                        #bouton.appuye = True

    def keySystem(self):
        # méthode faisant disparaître la clé si elle est recuperé
        if self.player.rect.colliderect(self.key.rect):
            self.keyFound = True
            print("True")

        if self.keyFound == True:
            pygame.sprite.spritecollide(self.player, self.keyGroup, True)
            self.currentLevel = 1

        if self.follower.rect.colliderect(self.key.rect):
            self.keyFound = True
            print("True")

        if self.keyFound == True:
            pygame.sprite.spritecollide(self.follower, self.keyGroup, True)

    def doorSystem(self):
            if self.player.rect.colliderect(self.door.rect):
                self.doorOpen = True
                print("True")

            if self.doorOpen == True:
                door.facing = "down"



    def detection(self):
        # méthode codant les champs de détection des caméras
        if self.view1.x <= self.player.x < self.view1.x1 and self.view1.y <= self.player.y < self.view1.y1:
            print("detecté")
            self.alive = False

        if self.view2.x <= self.player.x < self.view2.x1 and self.view2.y <= self.player.y < self.view2.y1:
            print("detecté")
            self.alive = False

    def plaqueDetection(self):
        # méthode codant les plaques de pression et la détection de celles-ci
        if self.plaque.x == self.player.x and self.plaque.y == self.player.y:
            print("plaque pressé")
            self.activationCamera = False
            self.plaque.image = pygame.image.load('sprites/plaques/plaque_pressé.png').convert_alpha()
        if not self.plaque.x == self.player.x or not self.plaque.y == self.player.y:
            self.plaque.image = pygame.image.load('sprites/plaques/plaque_non_pressé.png').convert_alpha()
            self.activationCamera = True
            print("plaque non-pressé")


    def desactivateCameras(self):
        # méthode désactivant les caméras au besoin
        if self.activationCamera == False:
            if self.camera.facing == "up":
                IMAGE = pygame.image.load('sprites/camera/camera_non_detecté/camera_up.png').convert_alpha()
            elif self.camera.facing == "down":
                IMAGE = pygame.image.load('sprites/camera/camera_non_detecté/camera_down.png').convert_alpha()
            elif self.camera.facing == "right":
                IMAGE = pygame.image.load('sprites/camera/camera_non_detecté/camera_right.png').convert_alpha()
            elif self.camera.facing == "left":
                IMAGE = pygame.image.load('sprites/camera/camera_non_detecté/camera_left.png').convert_alpha()

            self.view1.image.fill(GREEN)
            self.view1.image.set_alpha(125)

            self.view2.image.fill(GREEN)
            self.view2.image.set_alpha(125)

    def death(self):
        # méthode faisant mourrir le joueur au besoin
        if self.alive == False:
            print("vous êtes mort")
            game = Game()
            while True:
                game.respawnnew()
                game.run()

    def mouvementFollower(self):
        # mouvements du follower implementées grâce à une FILE
        if len(self.fileFollower.couloir) == 2:
            if self.fileFollower.couloir[0] == "left":
                self.follower.move(directionX=-1)
                if self.follower.push():
                    self.box.move(directionX=-1)
                self.fileFollower.defiler()

            if self.fileFollower.couloir[0] == "right":
                self.follower.move(directionX=1)
                if self.follower.push():
                    self.box.move(directionX=1)
                self.fileFollower.defiler()

            if self.fileFollower.couloir[0] == "up":
                self.follower.move(directionY=-1)
                if self.follower.push():
                    self.box.move(directionY=-1)
                self.fileFollower.defiler()

            if self.fileFollower.couloir[0] == "down":
                self.follower.move(directionY=1)
                if self.follower.push():
                    self.box.move(directionY=1)
                self.fileFollower.defiler()


        pass

# on lance le jeu dans une variable game
game = Game()
while True:
    game.new()
    game.run()
