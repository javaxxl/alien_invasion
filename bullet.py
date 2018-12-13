# -*- coding: utf-8 -*-
"""
Created on 2018/12/12 - the current system date.

__auther__ = 'xiaoliang'
"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        """create a bullet class at the location of ship"""
        super(Bullet, self).__init__()
        self.screen = screen

        # create rect and set up location
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # save the location of bullet
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """move up the bullet"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)




