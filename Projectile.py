import pygame

class Projectile():

    def __init__(self,name, color, x, y, radius, facing, speed):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.facing = facing
        self.speed = speed
