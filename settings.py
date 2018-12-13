# -*- coding: utf-8 -*-
"""
Created on 2018/10/15 - the current system date.

__auther__ = 'xiaoliang'
"""
class Settings():
    """save all settings for alien_invasion"""

    def __init__(self):
        """init the settings for screen"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        """init the settings for bullet"""
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed_factor = 1
        self.bullet_color = 60,60,60


