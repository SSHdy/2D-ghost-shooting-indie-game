import pygame.font
class Button():
    def __init__(self,screen,msg):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.width=300
        self.height=70
        self.color=(0,0,0)
        self.textcolor=(255,255,255)
        self.font=pygame.font.SysFont(None,48)
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        self.editmsg(msg)
    def editmsg(self,msg):
        self.image=self.font.render(msg,True, self.textcolor ,self.color)
        self.image_rect=self.image.get_rect()
        self.image_rect.center=self.rect.center
    def draw_button(self):
        self.screen.fill(self.color,self.rect)
        self.screen.blit(self.image,self.image_rect)
    
    def edit_location(self):
        self.image_rect.y-=5
# created to draw the buttons on screen

class State():
    def __init__(self,condition):
        self.game_active=condition

