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
food = snake.copy()
food.center = get_random_position()
snake_dir = (0, 0)
time, time_step = 0, 110
screen = py.display.set_mode([WINDOW] * 2)
clock = py.time.Clock()
dirs = {py.K_w: 1, py.K_s: 1, py.K_a: 1, py.K_d: 1}

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_w and dirs[py.K_w]:
                snake_dir = (0, -TILE_SIZE)
                dirs = {py.K_w: 1, py.K_s: 0, py.K_a: 1, py.K_d: 1}
            if event.key == py.K_s and dirs[py.K_s]:
                snake_dir = (0, TILE_SIZE)
                dirs = {py.K_w: 0, py.K_s: 1, py.K_a: 1, py.K_d: 1}
            if event.key == py.K_a and dirs[py.K_a]:
                snake_dir = (-TILE_SIZE, 0)
                dirs = {py.K_w: 1, py.K_s: 1, py.K_a: 1, py.K_d: 0}
            if event.key == py.K_d and dirs[py.K_d]:
                snake_dir = (TILE_SIZE, 0)
                dirs = {py.K_w: 1, py.K_s: 1, py.K_a: 0, py.K_d: 1}
    screen.fill('black')
    [py.draw.rect(screen, 'green', segment) for segment in segments]
    py.draw.rect(screen, 'red', food)
    time_now = py.time.get_ticks()
    self_eating = py.Rect.collidelist(snake, segments[:-1]) != -1 
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0,0)
        segments = [snake.copy()]
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]
    py.display.flip()
    clock.tick(60)
