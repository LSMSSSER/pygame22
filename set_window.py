from btn import Button
import pole_igrok
flag_l = False
flag_t = False
flag_r = False
LEFT, TOP, RIGHT = pole_igrok.keys()


def flag_swap(n):
    global flag_t, flag_r, flag_l
    if n == 1:
        flag_l = not flag_l
    elif n == 2:
        flag_t = not flag_t
    else:
        flag_r = not flag_r


def swap_keys(n, key):
    global LEFT, TOP, RIGHT
    if n == 1:
        LEFT = key
    elif n == 2:
        TOP = key
    else:
        RIGHT = key
    return


def set_screen(a):
    import pygame
    from main import SIZE, show_menu
    font = pygame.font.Font('data/font.ttf', 15)
    text1 = font.render('Отбить слева', False, 'black')
    text2 = font.render('Отбить в центре', False, 'black')
    text3 = font.render('Отбить справа', False, 'black')
    text4 = font.render('Для изменения клавиши - нажмите на кнопку, а затем на клавишу на клавиатуре', False, 'black')
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    running = True
    btn1 = Button(150, 50, screen, flag_swap)
    btn2 = Button(150, 50, screen, flag_swap)
    btn3 = Button(150, 50, screen, flag_swap)
    back_btn = Button(150, 50, screen, show_menu)
    fon = pygame.transform.scale(pygame.image.load('data/sample.jpg'), SIZE)
    screen.blit(fon, (0, 0))
    screen.blit(text1, (30, 155))
    screen.blit(text2, (220, 155))
    screen.blit(text3, (420, 155))
    screen.blit(text4, (10, 300))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if flag_l:
                    swap_keys(1, event.key)
                    flag_swap(1)
                elif flag_r:
                    swap_keys(3, event.key)
                    flag_swap(3)
                elif flag_t:
                    swap_keys(2, event.key)
                    flag_swap(2)
        btn1.draw(30, 100, str(LEFT), number=31)
        btn2.draw(220, 100, str(TOP), number=32)
        btn3.draw(410, 100, str(RIGHT), number=33)
        back_btn.draw(10, 540, 'BACK', number=101, action=a)
        pygame.display.flip()
        pole_igrok.swap(LEFT, TOP, RIGHT)