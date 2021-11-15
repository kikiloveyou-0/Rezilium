import pygame as pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load('sprites/Player.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, directionX=0, directionY=0):
        if not self.collideWall(directionX, directionY) and not self.collideCamera(directionX, directionY):
            self.x += directionX
            self.y += directionY

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def collideWall(self, directionX=0, directionY=0):
        for wall in self.game.walls:
            if wall.x == self.x + directionX and wall.y == self.y + directionY:
                return True
        return False

    def collideCamera(self, directionX=0, directionY=0):
        for camera in self.game.cameras:
            if camera.x == self.x + directionX and camera.y == self.y + directionY:
                return True
        return False

    def push(self):
        for box in self.game.boxes:
            if box.x == self.x and box.y == self.y:
                return True
        return False




class Door(pygame.sprite.Sprite):
    def __init__(self,game, x, y):
        self.game = game
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load('Tiles/images/Tilemap_20.png')
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
        self.image = pygame.image.load('sprites/cle.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Camera(pygame.sprite.Sprite):
    def __init__(self, game, x, y, facing):
        self.groups = game.allSprites, game.cameras
        self.game = game
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.facing = facing
        if self.facing == "up":
            IMAGE = pygame.image.load('sprites/camera/camera_detecté/camera_up.png').convert_alpha()
        elif self.facing == "down":
            IMAGE = pygame.image.load('sprites/camera/camera_detecté/camera_down.png').convert_alpha()
        elif self.facing == "right":
            IMAGE = pygame.image.load('sprites/camera/camera_detecté/camera_right.png').convert_alpha()
        elif self.facing == "left":
            IMAGE = pygame.image.load('sprites/camera/camera_detecté/camera_left.png').convert_alpha()


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
        self.groups = game.allSprites, game.views
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE*5, TILESIZE*2))
        self.image.fill(RED)
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
        self.image = pygame.image.load('sprites/wall.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        if self.x == 0:
            if self.y == 0:
                self.image = pygame.image.load('sprites/murs/mur_upleft.png')
            elif self.y > ((HEIGHT / TILESIZE)-2):
                self.image = pygame.image.load('sprites/murs/mur_downleft.png')
            else:
                self.image = pygame.image.load('sprites/murs/mur_left.png')
        elif self.y == 0:
            if self.x == 0:
                self.image = pygame.image.load('sprites/murs/mur_upleft.png')
            elif self.x > ((WIDTH / TILESIZE)-2):
                self.image = pygame.image.load('sprites/murs/mur_upright.png')
            else:
                self.image = pygame.image.load('sprites/murs/mur_up.png')
        elif self.x > ((WIDTH / TILESIZE)-2):
            if self.y == 0:
                self.image = pygame.image.load('sprites/murs/mur_upleft.png')
            elif self.y > ((HEIGHT / TILESIZE)-2):
                self.image = pygame.image.load('sprites/murs/mur_downright.png')
            else:
                self.image = pygame.image.load('sprites/murs/mur_right.png')
        elif self.y > ((HEIGHT / TILESIZE)-2):
            if self.x == 0:
                self.image = pygame.image.load('sprites/murs/mur_downleft.png')
            elif self.x > ((WIDTH / TILESIZE)-2):
                self.image = pygame.image.load('sprites/murs/mur_downright.png')
            else:
                self.image = pygame.image.load('sprites/murs/mur_down.png')
        else:
            self.image.fill((165,165,165))

class Titre(pygame.sprite.Sprite):
    def __init__(self, game, x, y,):
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load('sprites/menue/zgegos.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Fleches(pygame.sprite.Sprite):
    def __init__(self, game, x, y,):
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load('sprites/menue/zgegis.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class E(pygame.sprite.Sprite):
    def __init__(self, game, x, y,):
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load('sprites/menue/zgegas.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Noms(pygame.sprite.Sprite):
    def __init__(self, game, x, y,):
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load('sprites/menue/zgegons.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class PressEnter(pygame.sprite.Sprite):
    def __init__(self, game, x, y,):
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load('sprites/menue/zgegus.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Plaque(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.allSprites
        self.game = game
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load('sprites/plaques/plaque_non_pressé.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Box(pygame.sprite.Sprite):
    def __init__(self,game, x, y):
        self.game = game
        self.groups = game.allSprites, game.boxes
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load('Tiles/images/Box.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def move(self, directionX=0, directionY=0):
        if not self.collideWall(directionX, directionY) and not self.collideCamera(directionX, directionY):
            self.x += directionX
            self.y += directionY

    def collideWall(self, directionX=0, directionY=0):
        for wall in self.game.walls:
            if wall.x == self.x + directionX and wall.y == self.y + directionY:
                return True
        return False

    def collideCamera(self, directionX=0, directionY=0):
        for camera in self.game.cameras:
            if camera.x == self.x + directionX and camera.y == self.y + directionY:
                return True
        return False


class Bouton(pygame.sprite.Sprite):
    def __init__(self, game, x, y, facing):
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.facing = facing
        if self.facing == "up":
            IMG = pygame.image.load('sprites/outon/outon.png').convert_alpha()
        self.image = IMG
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Follower(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.image.load('sprites/Follower.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, directionX=0, directionY=0):
        if not self.collideWall(directionX, directionY) and not self.collideCamera(directionX, directionY):
            self.x += directionX
            self.y += directionY

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def collideWall(self, directionX=0, directionY=0):
        for wall in self.game.walls:
            if wall.x == self.x + directionX and wall.y == self.y + directionY:
                return True
        return False

    def collideCamera(self, directionX=0, directionY=0):
        for camera in self.game.cameras:
            if camera.x == self.x + directionX and camera.y == self.y + directionY:
                return True
        return False

    def push(self):
        for box in self.game.boxes:
            if box.x == self.x and box.y == self.y:
                return True
        return False







