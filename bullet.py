import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, centerx, centery):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/graphics/Bullets/PeaNormal/PeaNormal_0.png')
        self.rect = self.image.get_rect()
        self.rect.center = (centerx, centery)
        self.speed = 1

    def update(self):
        self.rect.x += self.speed