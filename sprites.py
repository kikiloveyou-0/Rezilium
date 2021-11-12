import pygame as pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, directionX=0, directionY=0):
        self.x += directionX
        self.y += directionY

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Door(pygame.sprite.Sprite):
    def __init__(self,game, x, y):
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
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
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
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.facing = facing
        if self.facing == "up":
            IMAGE = pygame.image.load('sprites/camera/camera_detecté/camera_up.png').convert_alpha()
        self.image = IMAGE
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def View(self, game, x, y):
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        #pygame.sprite.Sprite.add(self, self.groups) probablement la bonne méthode pour créer plusieurs sprites mais ne marche pas

        '''self.imageview = pygame.Surface((TILESIZE*5, TILESIZE*2))
        self.imageview.fill(GREEN)
        self.rectview = self.imageview.get_rect()
        self.xview = x
        self.yview = y''' # j'ai aussi testé ça mais ça ne marche pas

        # pour faire un cône, on peux juste faire deux rectangles, mais je n'arrive pas à créer plusieurs sprites

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
        ''' self.rect.x = self.xview * TILESIZE
        self.rect.y = self.yview * TILESIZE'''
