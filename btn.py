import pygame
import level_load
from get_score import get_score
from clear import dell


class Button:
    def __init__(self, width, height, screen, main, ls=None, msc=None):
        self.width = width
        self.height = height
        self.screen = screen
        self.main = main
        self.ls = ls
        self.music = msc

    def print_text(self, msg, x, y):
        pygame.init()
        font_type = pygame.font.Font('data/font.ttf', 15)
        text = font_type.render(msg, True, (0, 0, 0))
        self.screen.blit(text, (x, y))

    def draw(self, x, y, msg, action=level_load, number=1):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(self.screen, (200, 110, 6), (x, y, self.width, self.height))
            if 1 <= number <= 7:
                o = 120
                lis = self.ls[number]
                lis = lis[1:4]
                self.print_text('Режимы на уровне:', 200, 20)
                if lis[0] == 1:
                    self.print_text('Теневая зона', 370, 20)
                if lis[1] == 1:
                    self.print_text('Ветер', 510, 20)
                if lis[2] == 1:
                    self.print_text('Двойной мяч', 580, 20)
                self.print_text('Таблица лидеров ТОП 10', 400, 100)
                res = get_score(number)
                for i in res:
                    self.print_text(f'{i[0]} - {i[1]}', 400, o)
                    o += 20
            if click[0] == 1 and action:
                clc = pygame.mixer.Sound('Music/btn_sound.wav')
                clc.play()
                pygame.time.delay(300)
                if number == 69:
                    dell()
                    return
                if number == 99:
                    action(self.main)
                if number == 456:
                    self.main(action)
                if number == 101:
                    action(self.main)
                if number == 100:
                    action()
                if number == 31:
                    self.main(1)
                    return
                if number == 32:
                    self.main(2)
                    return
                if number == 33:
                    self.main(3)
                    return
                if number == 11:
                    action()
                if number == 43:
                    self.main(self.music)
                if number == 201:
                    self.main()
                if number == 202:
                    self.main()
                if number == 203:
                    self.main()
                else:
                    level_load.level_load(number, self.main, self.music)

        else:
            pygame.draw.rect(self.screen, (255, 100, 0), (x, y, self.width, self.height))
        self.print_text(msg, x + 10, y + 10)