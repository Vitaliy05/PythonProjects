import pygame

class Alien():
	def __init__(self, screen):
		"""Инициирует персонажа и задает его начальную позицию"""
		self.screen = screen
		
		#Загрузка изображения персонажа.
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		#Каждый новый персонаж появляется в центре экрана.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	def blitme(self):
		"""Рисует корабль в текущей позции"""
		self.screen.blit(self.image, self.rect)

