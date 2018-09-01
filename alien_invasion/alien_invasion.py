import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from back_ground import BackGround
from scoreboard import Scoreboard
from game_stats import GameStats
from button import Button
from game_functions import check_events,update_screen,update_bullets,create_fleet
from game_functions import update_aliens

def run_game():
    # 初始化游戏并创建一个屏幕对象
    ai_settings=Settings()
    pygame.init()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")

    ship=Ship(ai_settings,screen)
    back_ground=BackGround(screen)
    bullets=Group()
    aliens=Group()

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    create_fleet(ai_settings,screen,ship,aliens)

    # 开始游戏的主循环 
    while True:
        check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        update_screen(ai_settings, screen, back_ground, stats, sb, ship, aliens, bullets, play_button)

run_game()
