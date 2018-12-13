# -*- coding: utf-8 -*-
"""
Created on 2018/10/17 - the current system date.

__auther__ = 'xiaoliang'
"""
import pygame

class Ship():
    def __init__(self,ai_settings, screen):
        """init the boat and set the initial location"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load the image of boat and get the rectangle
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put the boat at the center of the bottom line
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.ship_speed_factor = 1.5
        self.center = float(self.rect.centerx)

    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # if self.rect.centerx < 600:
            self.center += self.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        """draw boat at the sepcified location"""
        self.screen.blit(self.image, self.rect)
