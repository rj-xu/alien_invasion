import os

import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并获取其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外界矩形
        file_path_ship = os.path.join('alien_invasion/images', 'ship.bmp')
        self.image = pygame.image.load(file_path_ship)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小树枝
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

        # 根据 self.centerx 更新 rect 对象
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
