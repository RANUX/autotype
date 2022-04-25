# 1 start
import pygame
import sys
import copy
import random
import time
# 1 end
# 2 start
pygame.init()

width = 500
height = 500
scale = 10
score = 0

food_x = 10
food_y = 10
# 2 end

# 3 start
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

background = (23, 32, 42)
snake_colour = (236, 240, 241)
food_colour = (148, 49, 38)
snake_head = (247, 220, 111)
# 3 end

# 4 start
print('Press ctrl+shift+1 to start and esc to exit')
print('Press ctrl+shift+2 to skip to next')
# 4 end