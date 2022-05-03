import pygame
from pygame.locals import *

class Player():
    def __init__(self,screen):
        self.mr=pygame.image.load(r'E:\IBDP\CS\Pictures\playerstandingright.png')
        self.ml=pygame.image.load(r'E:\IBDP\CS\Pictures\playerstandingleft.png')
        self.mu=pygame.image.load(r'E:\IBDP\CS\Pictures\playerstandingup.png')
        self.md=pygame.image.load(r'E:\IBDP\CS\Pictures\playerstandingdown.png')
        self.mr1=pygame.image.load(r'E:\IBDP\CS\Pictures\playermovingright.png')
        self.mr2=pygame.image.load(r'E:\IBDP\CS\Pictures\playermovingright1.png')
        self.ml1=pygame.image.load(r'E:\IBDP\CS\Pictures\playermovingleft.png')
        self.ml2=pygame.image.load(r'E:\IBDP\CS\Pictures\playermovingleft1.png')
        self.mu1=pygame.image.load(r'E:\IBDP\CS\Pictures\playermovingup.png')
        self.mu2=pygame.image.load(r'E:\IBDP\CS\Pictures\playermovingup1.png')
        self.md1=pygame.image.load(r'E:\IBDP\CS\Pictures\playermovingdown.png')
        self.md2=pygame.image.load(r'E:\IBDP\CS\Pictures\playermovingdown1.png')
        #initializing the image
        self.rr=[self.mr,self.mr1,self.mr2]
        self.ll=[self.ml,self.ml1,self.ml2]
        self.dd=[self.md,self.md1,self.md2]
        self.uu=[self.mu,self.mu1,self.mu2]
        # the dictionary that contains the parts of movements
        self.speed=5.0
        self.pic=self.md
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.flag=1
        self.rect=self.md.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        self.keyup=""
        self.picnum=0
    def update(self):
        if self.moving_left and self.rect.centerx > 0:
            self.picnum+=1
            self.rect.centerx -= self.speed
            self.picnum=self.picnum%3
            self.pic=self.ll[self.picnum]
            self.flag=1
        if self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.picnum+=1
            self.rect.centerx += self.speed
            self.picnum=self.picnum%3
            self.pic=self.rr[self.picnum]
            self.flag=2
        if self.moving_up and self.rect.y>0:
            self.picnum+=1
            self.rect.y -= self.speed
            self.picnum=self.picnum%3
            self.pic=self.uu[self.picnum]
            self.flag=3
        if self.moving_down and self.rect.y<self.screen_rect.bottom:
            self.picnum+=1
            self.rect.y += self.speed
            self.picnum=self.picnum%3
            self.pic=self.dd[self.picnum]
            self.flag=4
        if self.keyup:
            if self.keyup == K_d:
                self.picnum=0
                self.pic=self.mr
            elif self.keyup == K_w:
                self.picnum=0
                self.pic=self.mu
            elif self.keyup== K_a:
                self.picnum=0
                self.pic=self.ml
            elif self.keyup== K_s:
                self.picnum=0
                self.pic=self.md
    # movement of the main character
        
    def blitme(self):
        self.screen.blit(self.pic,self.rect)

    def center_myself(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)



        






