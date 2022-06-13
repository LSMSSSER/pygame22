def win_screen():
    from main import SIZE
    import pygame
    from btn import Button
    from main import show_menu

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    FPS = 50
    btn = Button(100, 100, screen, show_menu)
    fon = pygame.transform.scale(pygame.image.load('win.jpg'), SIZE)
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        btn.draw(100, 100, 'Уровни', number=11)
        pygame.display.flip()
        clock.tick(FPS)