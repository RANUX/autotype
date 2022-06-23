# 1 start
# импортируем библиотеки
"""!
импортируем основные библиотеки
"""
import pygame
import sys
import copy
import random
import time
# 1 end

# 2 start
# инициализируем pygame
"""!
инициализируем пайгейм
"""
pygame.init()
# 2 end

# 3 start
# задаём ширину и высоту экрана
"""!
задаём ширину и высоту экрана
"""
width = 500
height = 500
# 3 end

# 4 start
# инициализируем переменные
"""!
инициализируем основные переменные
и задаем значения в виде целых чисел
"""
scale = 10
score = 0
food_x = 10
food_y = 10
# 4 end

# 5 start
# создаем объект окна с заданной  шириной и высотой
"""!
создаем объект окн+а с заданной шириной и высотой
"""
display = pygame.display.set_mode((width, height))
# 5 end

# 6 start
# устанавливаем заголовок окна
"""!
устанавливаем заголовок окн+а
"""
pygame.display.set_caption("Snake Game")
# 6 end

# 7 start
"""!
создаем объект часов и присваиваем значение переменной клок
"""
clock = pygame.time.Clock()
# 7 end

# 8 start
# Инициализируем переменные
"""!
Инициализируем переменные цвета в кортеже
"""
background = (23, 32, 42)
snake_colour = (236, 240, 241)
food_colour = (148, 49, 38)
snake_head = (247, 220, 111)
# 8 end

# 9 start
#! Запустим программу
# 9 end

# 10 start
# Пока!
# 10 end