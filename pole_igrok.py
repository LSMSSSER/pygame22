import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)
LEFT = 1073741904
TOP = 1073741906
RIGHT = 1073741903


def keys():
    return LEFT, TOP, RIGHT


def swap(l, t, r):
    global LEFT, TOP, RIGHT
    LEFT = l
    TOP = t
    RIGHT = r


class Board_player:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 360
        self.top = 350
        self.cell_size = 37
        self.image_mainpos = pygame.image.load("data/mainpos.jpg")
        self.image_mainpos = pygame.transform.scale(self.image_mainpos, (50, 70))
        self.image_mainpos.set_colorkey(WHITE)
        self.image_left = pygame.image.load("data/left.jpg")
        self.image_left = pygame.transform.scale(self.image_left, (50, 70))
        self.image_left.set_colorkey(WHITE)
        self.image_right = pygame.image.load("data/right.jpg")
        self.image_right = pygame.transform.scale(self.image_right, (50, 70))
        self.image_right.set_colorkey(WHITE)
        self.image_mainpos2 = pygame.image.load("data/right.jpg")
        self.image_mainpos2 = pygame.transform.scale(self.image_mainpos2, (50, 70))
        self.image_mainpos2.set_colorkey(WHITE)

        self.mainpos = True

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        x = self.left
        y = self.top
        for j in range(self.width):
            if self.mainpos == True:
                screen.blit(self.image_mainpos, (414, 350))
            else:
                if j == 0 and self.board[0][j] == 1:
                    screen.blit(self.image_left, (x, y))
                if j == 2 and self.board[0][j] == 1:
                    screen.blit(self.image_right, (x, y))
                if j == 1 and self.board[0][j] == 1:
                    screen.blit(self.image_mainpos2, (380, 350))
            x += self.cell_size

    def get_click(self, key):
        if key == LEFT:
            arrow = 1
        elif key == RIGHT:
            arrow = 3
        elif key == TOP:
            arrow = 2
        else:
            return None
        self.on_click(arrow)
        return arrow

    def on_click(self, arrow):
        if arrow == 1:
            self.board[0][0] = 1
        elif arrow == 2:
            self.board[0][1] = 1
        elif arrow == 3:
            self.board[0][2] = 1

    def get_coords(self):
        for i in range(3):
            if self.board[0][i] == 1:
                return(self.top, self.left + (self.cell_size + 20) * i)
        return None


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    shar = Board_player(3, 1)
    shar.set_view(shar.left, shar.top, shar.cell_size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                shar.get_click(event.key)
                mainpos_stat = False
        screen.fill((0, 0, 0))
        shar.render(screen)
        pygame.display.flip()
    pygame.quit()

