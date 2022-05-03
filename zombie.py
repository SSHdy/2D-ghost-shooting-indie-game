import pygame
from pygame.sprite import Sprite
class Zombie(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load(r'E:\IBDP\CS\IA\zombiemoveright.png')
        self.rect=self.image.get_rect()
        self.x=self.rect.width
        self.y=self.rect.height
        self.x=float(self.rect.x)
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    