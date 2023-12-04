import pygame as py
from random import randrange
from enum import Enum
from collections import namedtuple

WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = py.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments= [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 110
screen = py.display.set_mode([WINDOW] * 2)
clock = py.time.Clock()

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_w:
                snake_dir = (0, -TILE_SIZE)
            if event.key == py.K_s:
                snake_dir = (0, TILE_SIZE)
            if event.key == py.K_a:
                snake_dir = (-TILE_SIZE, 0)
            if event.key == py.K_d:
                snake_dir = (TILE_SIZE, 0)
    screen.fill('black')
    [py.draw.rect(screen, 'green', segment) for segment in segments]
    time_now = py.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
    py.display.flip()
    clock.tick(60)
