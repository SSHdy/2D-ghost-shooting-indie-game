import pygame
from pygame.locals import *
from random import randint, choice
from pygame.math import *
from Addons import State, Statemachine
from pygame.sprite import Sprite
class World(object):
    def __init__(self):
        self.entities = {}
        self.entity_id = 0
    # constructor
    def add_entity(self, entity):
        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1
    # add the entity to the world
    def remove_entity(self, entity):
        del self.entities[entity.id]
 
    def get(self, entity_id):
        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None
    # get entity that exists
    def process(self, time_passed):
        time_passed_seconds = time_passed / 1000.0
        for entity in self.entities.values():
            entity.process(time_passed_seconds)
    
    def render(self, surface):
        for entity in self.entities.values():
            if entity.name == "mob":
                entity.render(surface)
    # draw the image
    def get_close_entity(self, name, location, range=100.):
        location = Vector2(*location)
        for entity in self.entities.values():
            if entity.name == name:
                distance = location.distance_to(entity.location)
                if distance < range:
                    return entity
        return None
    # get the close entity, in order to chase player
class GameEntity(Sprite):
    
    def __init__(self, world, name, image):
        super().__init__()
        self.world = world
        self.name = name
        self.image = image
        self.location = Vector2(0, 0)
        self.destination = Vector2(0, 0)
        self.speed = 0.
        self.brain = Statemachine()
        self.id = 0
        self.rect=self.image.get_rect()
        

    def render(self, surface):
        x, y = self.location
        w, h = self.image.get_size()
        surface.blit(self.image, (x-w/2, y-h/2))   
 
    def process(self, time_passed):
        self.brain.think()
        if self.speed > 0. and self.location != self.destination:
            vec_to_destination = self.destination - self.location
            distance_to_destination = vec_to_destination.length()
            heading = vec_to_destination.normalize()
            travel_distance = min(distance_to_destination, time_passed * self.speed)
            self.location += travel_distance * heading
            self.rect.x, self.rect.y= self.location
    
class Searching(State):
    def __init__(self, mob):
        State.__init__(self,"Searching")
        self.mob=mob 
    def randsearch(self):
        w = 1077
        h = 500
        self.mob.destination=Vector2(randint(0,w),randint(0,h))
    def do_actions(self):
        if randint(1,20) == 1:
            self.randsearch()
    def check_conditions(self):
        player = self.mob.world.get_close_entity("player", self.mob.location)
        if player is not None:
            if self.mob.location.distance_to(player.location) < 100.:
                self.mob.player_id=player.id 
                return "Seeking"
            return None
    def entry_actions(self):
        self.mob.speed=120 + randint(-30,30)
        self.randsearch()
# Searching Stage
class Seeking(State):
    def __init__(self,mob):
        State.__init__(self, "Seeking")
        self.mob=mob
        self.player_id=None
    def check_conditions(self):
        player=self.mob.world.get(self.mob.player_id)
        if player is None:
            return "Searching"
        if self.mob.location.distance_to(player.location) <5.0:
            return "Hunting"
    def entry_actions(self):
        player=self.mob.world.get(self.mob.player_id)
        if player is not None:
            self.mob.destination=player.location
            self.mob.speed = 160.0 + randint(-20, 20)
# Seeking STage
    
class Hunting(State):
    def __init__(self, mob):
        State.__init__(self,"Hunting")
        self.mob=mob
        self.got_kill=False          
    def check_conditions(self):
        player=self.mob.world.get(self.mob.player_id)
        if player is None:
            return "Searching"
        if self.got_kill == False:
            if self.mob.location.distance_to(player.location) > 1.0:
                return "Seeking"

    def entry_actions(self):
        self.speed=160.0+randint(0,50)
    def exit_actions(self):
        self.got_kill=False
# Hunting Stage
class Mobs(GameEntity):
    def __init__(self, world, image):
        GameEntity.__init__(self, world, "mob", image)
        Searching_state=Searching(self) 
        Seeking_state=Seeking(self)
        Hunting_state=Hunting(self)
        self.brain.add_state(Searching_state)
        self.brain.add_state(Seeking_state)
        self.brain.add_state(Hunting_state)
    
    def blitme(self, surface):
        GameEntity.render(self, surface)
# Ghost class
class PlayerS(GameEntity):
    def __init__(self,world, image):
        GameEntity.__init__(self, world, "player", image)
        self.location=Vector2(0,0)
    def updatelocation(self,x , y):
        self.location=Vector2(x,y)
# player class, used to trace player





            


            



