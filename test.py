# импортируем библиотеки
import pygame
import sys
import copy
import random
import time

# инициализируем pygame
# задаём ширину и высоту экрана
width = 500
height = 500

# инициализируем переменные
scale = 10
score = 0
food_x = 10
food_y = 10

# создаем объект окна с заданной  шириной и высотой
display = pygame.display.set_mode((width, height))

# устанавливаем заголовок окна
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Инициализируем переменные
background = (23, 32, 42)
snake_colour = (236, 240, 241)
food_colour = (148, 49, 38)
snake_head = (247, 220, 111)


# Пока!

