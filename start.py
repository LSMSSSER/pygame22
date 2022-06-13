import set_window
SIZE = WIDTH, HEIGHT = 800, 600
flag_misic = False


def start_screen(act):
    global flag_misic
    import pygame
    screen = pygame.display.set_mode(SIZE)
    clc = pygame.mixer.Sound('Music/btn_sound.wav')
    fon = pygame.transform.scale(pygame.image.load('data/START.jpg'), (SIZE))
    if not flag_misic:
        pygame.mixer.music.load('Music/mainmenu.mp3')
        pygame.mixer.music.play(-1)
        flag_misic = True
    screen.blit(fon, (0, 0))
    flag = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 230 < mouse[0] < 560 and 200 < mouse[1] < 350 and flag:
            f = pygame.transform.scale(pygame.image.load('data/START2.jpg'), SIZE)
            screen.blit(f, (0, 0))
            flag = False
            if click[0] == 1:
                clc.play()
                act(flag_misic)
        elif 70 <= mouse[0] <= 222 and 230 <= mouse[1] <= 315 and flag:
            f = pygame.transform.scale(pygame.image.load('data/START_pressed.jpg'), SIZE)
            screen.blit(f, (0, 0))
            if click[0] == 1:
                clc.play()
                set_window.set_screen(start_screen)
        elif 567 <= mouse[0] <= 715 and 238 <= mouse[1] <= 315:
            f = pygame.transform.scale(pygame.image.load('data/START3.jpg'), SIZE)
            screen.blit(f, (0, 0))
            if click[0] == 1:
                pygame.quit()
                exit()
        else:
            f = pygame.transform.scale(pygame.image.load('data/START.jpg'), SIZE)
            screen.blit(f, (0, 0))
        flag = True
        pygame.display.flip()