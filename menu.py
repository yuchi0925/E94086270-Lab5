import pygame
import os

# 上傳圖片
MENU_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
UPGRADE_IMAGE = pygame.image.load(os.path.join("images", "upgrade.png"))
SELL_IMAGE = pygame.image.load(os.path.join("images", "sell.png"))

# 定義圖片尺寸
MENU_SIZE = (150, 150)
UPGRADE_SIZE = (50, 30)
SELL_SIZE = (30, 30)

class UpgradeMenu:
    def __init__(self, x, y):
        self.menu_image = pygame.transform.scale(MENU_IMAGE, MENU_SIZE)
        self.upgrade_image = pygame.transform.scale(UPGRADE_IMAGE, UPGRADE_SIZE)
        self.sell_image = pygame.transform.scale(SELL_IMAGE, SELL_SIZE)

        # 獲取圖片大小
        self.menu_rect = self.menu_image.get_rect()
        self.upgrade_rect = self.upgrade_image.get_rect()
        self.sell_rect = self.sell_image.get_rect()

        # 設定圖片位置
        self.menu_rect.center = (x, y)
        self.upgrade_rect.center = (x, y + 55)
        self.sell_rect.center = (x, y - 53)

        # (Q2) Add buttons here
        self.__buttons = [Button(self.upgrade_image, 'upgrade', self.upgrade_rect.center[0], self.upgrade_rect.center[1]),\
                          Button(self.sell_image, 'sell', self.sell_rect.center[0], self.sell_rect.center[1])]


    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.menu_image, self.menu_rect)
        # draw button
        # (Q2) Draw buttons here
        win.blit(self.upgrade_image, self.upgrade_rect)
        win.blit(self.sell_image, self.sell_rect)


    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """

        # 判斷是否點擊在範圍內
        if self.rect.collidepoint(x, y):
            return True
        else:
            return False

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name






