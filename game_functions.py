# -*- coding: utf-8 -*-
"""
Created on 2018/10/18 - the current system date.

__auther__ = 'xiaoliang'
"""
import sys
import pygame


def check_events(ship):
    # monitor the keyboard and mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        # move the ship to the right
        # ship.rect.centerx +=1
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.update()
    ship.blitme()
    pygame.display.flip()
