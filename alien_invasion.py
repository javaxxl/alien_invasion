# -*- coding: utf-8 -*-
"""
Created on 2018/10/12 - the current system date.

__auther__ = 'xiaoliang'
"""
# import  sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # init game and create a window object
    pygame.init()
    ai_settings = Settings()
    pygame.display.set_caption("Alien_Invasion")
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # print(ai_settings.screen_width)
    # bg_color = (230,230,230)
    ship = Ship(ai_settings, screen)

    # start the main loop for game
    while True:
        # monitor the keyboard and mouse event
        gf.check_events(ship)
        # make the latest drawn screen visible
        gf.update_screen(ai_settings, screen, ship)


run_game()
