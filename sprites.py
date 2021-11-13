import pygame as pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.image.load('Tiles/images/Player.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, directionX=0, directionY=0):
        if not self.collide(directionX, directionY):
            self.x += directionX
            self.y += directionY

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
    
    def collide(self, directionX=0, directionY=0):
        for wall in self.game.walls:
            if wall.x == self.x + directionX and wall.y == self.y + directionY:
                return True
        return False


class Door(pygame.sprite.Sprite):
    def __init__(self,game, x, y):
        self.game = game
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load('sprites/porte/porte_down.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Key(pygame.sprite.Sprite):
    def __init__(self,game, x, y):
        self.groups = game.allSprites, game.keyGroup
        self.game = game
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load('Tiles/images/Key.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Camera(pygame.sprite.Sprite):
    def __init__(self, game, x, y, facing):
        # le sprite de la caméra ne s'affiche pas car je n'arrive pas à créer et faire co-exister plusieurs sprites
        self.groups = game.allSprites
        self.game = game
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.facing = facing
        if self.facing == "up":
            IMAGE = pygame.image.load('Tiles/images/Tilemap_15.png').convert_alpha()
        self.image = IMAGE
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class View(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE*5, TILESIZE*2))
        self.image.fill(GREEN)
        self.image.set_alpha(125)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.x1 = self.x + 5
        self.y1 = self.y + 2

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.allSprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        if self.x == 0:
            if self.y == 0:
                self.image = pygame.image.load('Tiles/images/Tilemap_04.png')
            elif self.y > ((HEIGHT / TILESIZE)-2):
                self.image = pygame.image.load('Tiles/images/Tilemap_05.png')
            else:
                self.image = pygame.image.load('Tiles/images/Tilemap_08.png')
        elif self.y == 0:
            if self.x == 0:
                self.image = pygame.image.load('Tiles/images/Tilemap_04.png')
            elif self.x > ((WIDTH / TILESIZE)-2):
                self.image = pygame.image.load('Tiles/images/Tilemap_03.png')
            else:
                self.image = pygame.image.load('Tiles/images/wall.png')
        elif self.x > ((WIDTH / TILESIZE)-2):
            if self.y == 0:
                self.image = pygame.image.load('Tiles/images/Tilemap_04.png')
            elif self.y > ((HEIGHT / TILESIZE)-2):
                self.image = pygame.image.load('Tiles/images/Tilemap_07.png')
            else:
                self.image = pygame.image.load('Tiles/images/Tilemap_10.png')
        elif self.y > ((HEIGHT / TILESIZE)-2):
            if self.x == 0:
                self.image = pygame.image.load('Tiles/images/Tilemap_05.png')
            elif self.x > ((WIDTH / TILESIZE)-2):
                self.image = pygame.image.load('Tiles/images/Tilemap_07.png')
            else:
                self.image = pygame.image.load('Tiles/images/Tilemap_09.png')
        else:
            self.image.fill((195,197,183))

