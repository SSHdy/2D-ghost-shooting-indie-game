import sys
import pygame
from bullet import Bullet
from zombie import Zombie
from Mobs import Mobs
def check_events(gamestats, state, link,screen,bullets, play_button, replay_button,respawn_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y=pygame.mouse.get_pos()
            check_play_button(gamestats, state, play_button, mouse_x, mouse_y, replay_button,respawn_button)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,link,screen,bullets)
            link.keyup=""
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,link,screen,bullets)
            link.keyup = event.key
# Check all the keyboard events

def check_play_button(gamestats, state,play_button, mouse_x, mouse_y, replay_button, respawn_button):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        state.game_active=True
    if replay_button.rect.collidepoint(mouse_x,mouse_y):
        gamestats.lossthegame=False
        
    if respawn_button.rect.collidepoint(mouse_x,mouse_y):
        gamestats.pausethegame=False
# check mouse click
def check_keydown_events(event,link, screen, bullets):
    if event.key == pygame.K_a:
        link.moving_left=True
    elif event.key == pygame.K_w:
        link.moving_up=True
    elif event.key == pygame.K_d:
        link.moving_right=True
    elif event.key == pygame.K_s:
        link.moving_down=True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(screen, link)
        bullets.add(new_bullet)
# check key down
def check_keyup_events(event,link,screen,bullets):
    if event.key == pygame.K_a:
        link.moving_left=False
    elif event.key == pygame.K_w:
        link.moving_up=False
    elif event.key == pygame.K_d:
        link.moving_right=False
    elif event.key == pygame.K_s:
        link.moving_down=False
# check key up
def update_screen(screen, link,bullets,zombies,mobs):
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    link.blitme()
    mobs.draw(screen)
# draw all the things
def create_fleet(screen, zombies):
    zombie = Zombie(screen)
    zombie_width = zombie.rect.width
    available_space_x=1070 - 2*zombie_width
    number_zombies_x=int(available_space_x/(2*zombie_width))

    for zombie_number in range(number_zombies_x):
        zombie = Zombie(screen)
        zombie.x = zombie_width+2*zombie_width*zombie_number
        zombie.rect.x = zombie.x
        zombies.add(zombie)
