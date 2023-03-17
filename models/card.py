# class Card:
#     def __init__(
#             self, 
#             title: str, 
#             image: str, 
#             hp: int, 
#             ad: int, 
#             desc: str, 
#             cost: int, 
#             onShow, 
#             onAttack
#             ):

#         self._title = title
#         self._image = image
#         self._hp = hp
#         self._ad = ad
#         self._desc = desc
#         self._cost = cost
#         self._onShow = onShow
#         self._onAttack = onAttack

#     def onShow(self):
#         self._onShow()

#     def onAttack(self):
#         self._onAttack()


import pygame


class Card(pygame.sprite.Sprite):
    def __init__(self, name, cost, attack, health, image, desc):
        super().__init__()
        self.name = name
        self.cost = cost
        self.attack = attack
        self.health = health
        self.image = image
        self.rect = self.image.get_rect()
        self.desc = desc

    def draw(self, surface, x, y):
        self.rect.x = x
        self.rect.y = y
        surface.blit(self.image, self.rect)
        font = pygame.font.Font("assets/fonts/nunito_bold.ttf", 18)
        text = font.render(self.name, True, (255, 255, 255))
        surface.blit(text, (x + 5, y + 5))
        text = font.render(str(self.cost), True, (255, 255, 255))
        surface.blit(text, (x + 5, y + self.rect.height - 25))
        text = font.render(str(self.attack), True, (255, 255, 255))
        surface.blit(text, (x + self.rect.width - 25, y + 5))
        text = font.render(str(self.health), True, (255, 255, 255))
        surface.blit(text, (x + self.rect.width - 25, y + self.rect.height - 25))
