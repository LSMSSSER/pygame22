def save(main):
    import pygame
    SIZE = 800, 600
    from btn import Button
    import start

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    running = True
    font = pygame.font.Font('data/font.ttf', 17)
    text = font.render('Выбор сохранения', False, 'black')
    fon = pygame.transform.scale(pygame.image.load('data/sample.jpg'), SIZE)
    screen.blit(fon, (0, 0))
    screen.blit(text, (60, 50))
    btn_ex = Button(70, 70, screen, start.start_screen)
    btn1 = Button(40, 40, screen, main)
    btn2 = Button(40, 40, screen, main)
    btn3 = Button(40, 40, screen, main)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        btn1.draw(100, 100, '1', number=201)
        btn2.draw(100, 200, '2', number=202)
        btn3.draw(100, 300, '3', number=203)
        btn_ex.draw(10, 500, 'BACK', number=456, action=save)
        pygame.display.flip()
