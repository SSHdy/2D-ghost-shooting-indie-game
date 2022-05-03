import pygame
from pygame.sprite import Sprite
from pygame.locals import *
class Bullet(Sprite):
    def __init__(self,screen,link):
        super().__init__()
        self.screen = screen
        self.image=pygame.image.load(r'E:\IBDP\CS\Pictures\Fireblastdown.png')
        self.rect=self.image.get_rect()
        self.rect.centerx = link.rect.centerx
        self.rect.top=link.rect.top
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)
        self.color = (255, 20, 147)
        self.speed_factor = 6.0
        self.determinant=link.flag
        
    def update(self):
        if self.determinant == 1:
            self.x -= self.speed_factor
            self.rect.x=self.x
            self.image=pygame.image.load(r'E:\IBDP\CS\Pictures\Fireblastleft.png')
        elif self.determinant == 2:
            self.x += self.speed_factor
            self.rect.x=self.x
            self.image=pygame.image.load(r'E:\IBDP\CS\Pictures\Fireblastright.png')
        elif self.determinant == 3:
            self.y -=self.speed_factor
            self.rect.y=self.y
            self.image=pygame.image.load(r'E:\IBDP\CS\Pictures\Fireblastup.png')
        elif self.determinant == 4:
            self.y +=self.speed_factor
            self.rect.y=self.y
            self.image=pygame.image.load(r'E:\IBDP\CS\Pictures\Fireblastdown.png')
    def draw_bullet(self):
        #pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)
    def detectcollide(self, target):
        self.flag=self.rect.colliderect(target.rect)
        
        

