import os

import pygame

import random

START = start_x, start_y = 360, 165
BOARD = BOARD_WIDTH, BOARD_HEIGHT = 130, 215


def load_image(name, x, y, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image = pygame.transform.scale(image, (x, y))
    return image


class Ball(pygame.sprite.Sprite):
    image = load_image('ball_skin.png', 8, 8)

    def __init__(self, group_1, group_2, wind, shadow):
        super().__init__(group_1)
        self.add(group_2)
        self.wind = wind
        self.shadow = shadow
        self.image = Ball.image
        self.rect = self.image.get_rect()

        self.start_x = start_x
        self.start_y = start_y

        self.rect.x = start_x + BOARD_WIDTH // 2
        self.rect.y = start_y

        self.a_coord = 1
        self.p_coord = 0

        self.vx = 1
        self.vy = -4

        self.collide_flag = False
        self.wind_flag = False
        self.wind_move = 0

        self.enemy_flag = False

    def update(self, border, barrier):
        if pygame.sprite.spritecollideany(self, border):
            self.p_coord = random.randint(0, 2)
            self.vy = 4
            self.collide_flag = False
            self.enemy_flag = True

        if pygame.sprite.spritecollideany(self, barrier):
            if self.shadow:
                if self.vy < 0:
                    self.image = pygame.Surface([0, 0])
                else:
                    self.image = Ball.image
            if not self.collide_flag:
                self.collide_flag = True
                if random.randint(0, 3) == 0:
                    self.wind_flag = True
                    if abs(self.a_coord - self.p_coord) == 1:
                        if self.p_coord > self.a_coord:
                            self.wind_move = 1
                            self.p_coord -= 2
                        else:
                            self.wind_move = -1
                            self.p_coord += 2
                    elif abs(self.p_coord - self.a_coord) == 2:
                        if self.p_coord > self.a_coord:
                            self.wind_move = 2
                            self.p_coord -= 4
                        else:
                            self.wind_move = -2
                            self.p_coord += 4

        if abs(self.a_coord - self.p_coord) == 2:
            if self.p_coord > self.a_coord:
                if self.vy > 0:
                    self.vx = 2
                else:
                    self.vx = -2
            else:
                if self.vy > 0:
                    self.vx = -2
                else:
                    self.vx = 2
        elif abs(self.a_coord - self.p_coord) == 1:
            if self.p_coord > self.a_coord:
                if self.vy > 0:
                    self.vx = 1
                else:
                    self.vx = -1
            else:
                if self.vy > 0:
                    self.vx = -1
                else:
                    self.vx = 1
        else:
            self.vx = 0
        self.rect = self.rect.move(self.vx, self.vy)
        if self.enemy_flag:
            self.enemy_flag = False
            if self.rect.x - self.start_x > BOARD_WIDTH // 3:
                return 1
            else:
                return 2
        else:
            return None

    def get_coords(self):
        return self.rect.y, self.rect.x


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface([x2 - x1, 1])
        self.rect = pygame.Rect(x1, y1, x2 - x1, 5)


class Barrier(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, *groups):
        super().__init__(*groups)
        self.image = load_image('setka.png', 130, 23)
        self.rect = pygame.Rect(x1 - 1, y1 - 15, x2 - x1 + 1, 5)


class Animated_enemy(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, *groups):
        super().__init__(*groups)
        self.frames = []
        self.frame = 0
        self.cut_sheet(sheet, columns, rows)
        self.image = self.frames[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                    sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, x, y, frame):
        self.rect.x = x
        self.rect.y = y
        self.image = self.frames[frame]


class Table(pygame.sprite.Sprite):
    def __init__(self, x, y, image, *groups):
        super().__init__(*groups)
        self.image = load_image(image, BOARD_WIDTH, BOARD_HEIGHT)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Particle(pygame.sprite.Sprite):
    image = load_image('particle.jpg', 5, 5)

    def __init__(self, x, y, *groups):
        super().__init__(groups)
        self.image = Particle.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y