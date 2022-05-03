import pygame
import sys
from player import Player
from pygame.locals import *
from bullet import Bullet
from pygame.sprite import Group
import gamefunction as gf
from zombie import Zombie
from Mobs import World
from Mobs import Mobs
from Mobs import PlayerS
from random import randint, choice
from pygame.math import *
from Button import Button
from Button import State
from Game_stats import Gamestats
from time import sleep
def run_game():
    pygame.init()
    fps = pygame.time.Clock()
    screen = pygame.display.set_mode((1077,500))
    pygame.display.set_caption("GhostShooting")
    background = pygame.image.load(r"E:\IBDP\CS\IA\Background_of_Dungeon.png")
    link=Player(screen)
    bullets=Group()
    zombies=Group() 
    mobs=Group()
    gf.create_fleet(screen,zombies)
    world = World()
    w= 1077
    h= 500
    clock = pygame.time.Clock()
    player=PlayerS(world, pygame.image.load(r'E:\IBDP\CS\Pictures\ghostgreen.png'))
    world.add_entity(player)
    gamestats=Gamestats()
    # initiating all the variables
    for x in range(15):
        if x% 2==0 :
            mob_image=pygame.image.load(r'E:\IBDP\CS\Pictures\ghostgreen.png')
        elif x%3 ==0 :
            mob_image=pygame.image.load(r'E:\IBDP\CS\Pictures\ghostgrey.png')
        else:
            mob_image=pygame.image.load(r'E:\IBDP\CS\Pictures\ghostwhite.png')
        mob= Mobs(world,mob_image)
        mob.location= Vector2(randint(0,w),randint(0,h))
        mob.brain.set_state("Searching")
        world.add_entity(mob)
        mobs.add(mob)
    #creating the mobs group
    play_button=Button(screen,"Play")
    replay_button=Button(screen,"Replay")
    respawn_button=Button(screen, "Respawn")
    win_button=Button(screen,"You Win!")
    #creating the buttons
    stats=State(False)
    score=0
    def player_got_hit():
        gamestats.lives_left-=1
        bullets.empty()
        mobs.empty()
        for x in range(10):
            if x% 2==0 :
                mob_image=pygame.image.load(r'E:\IBDP\CS\Pictures\ghostgreen.png')
            elif x%3 ==0 :
                mob_image=pygame.image.load(r'E:\IBDP\CS\Pictures\ghostgrey.png')
            else:
                mob_image=pygame.image.load(r'E:\IBDP\CS\Pictures\ghostwhite.png')
            mob= Mobs(world,mob_image)
            mob.location= Vector2(randint(0,w),randint(0,h))
            mob.brain.set_state("Searching")
            world.add_entity(mob)
            mobs.add(mob)
        link.center_myself()
        sleep(0.3)
    print("Welcome to GhostShooting Game!\n")
    print("Click the button at the center to start the game and here are some instructions!\n")
    print("In the game, you have 4 lives and there will be 10 ghosts in the game that will chase you\n")
    print("use your magic power to kill all the mobs that randomly spawns in the place\n")
    print("If you kill all of them, You will win the game!\n")
    print("The direction of the character is controlled by keys WASD, and the attack button is SPACE\n")
    print("Enjoy!")
    #CLI lines
    #the core loop of the game
    while True:
        gf.check_events(gamestats, stats,link, screen,bullets,play_button,replay_button,respawn_button)
        screen.blit(background,(0,0)) 
        if stats.game_active==False:
            play_button.draw_button()
            
        time_passed=clock.tick(30)
         
        if stats.game_active==True and gamestats.lossthegame==False and gamestats.winthegame==False and gamestats.pausethegame==False:
            player.updatelocation(link.rect.x,link.rect.y)
            link.update()
            bullets.update()
            gf.update_screen(screen, link, bullets, zombies,mobs)
            if pygame.sprite.spritecollideany(link,mobs):
                print("Got hit! You are dead! "+str(gamestats.lives_left)+" lives left\n")
                print("Click Respawn Button to respawn")
                player_got_hit()
                gamestats.pausethegame=True
                score=0
            if gamestats.lives_left ==0:
                gamestats.lossthegame=True
                gamestats.lives_left=4
                print("you lose! click replay to try again!")
            world.process(time_passed)
            collisions=pygame.sprite.groupcollide(bullets,mobs,True,True)
            if collisions:
                score+=1
            if score==10:
                gamestats.winthegame=True
                print("Congratulation! You won the Game!")
                
        if gamestats.pausethegame==True:
            respawn_button.draw_button()
        # Respawn stage
        if gamestats.lossthegame==True:
                replay_button.draw_button()
        # Replay Stage
        if gamestats.winthegame==True:
                win_button.draw_button()
        # Win Stage
        fps.tick(60)
        pygame.display.flip()


run_game()
