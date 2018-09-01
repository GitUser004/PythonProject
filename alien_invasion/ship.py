import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super(Ship, self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        self.image=pygame.image.load("images/ship.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.xcenter=float(self.rect.centerx)
        self.ycenter=float(self.rect.centery)

        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.xcenter+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.xcenter-=self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top>0:
            self.ycenter-=self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.ycenter+=self.ai_settings.ship_speed_factor

        self.rect.centerx=self.xcenter
        self.rect.centery=self.ycenter

    def center_ship(self):
        """Center the ship on the screen."""
        self.xcenter = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.ycenter = float(self.rect.centery)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

