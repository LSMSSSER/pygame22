import pygame


def end_screen(score, id, flagst=False):
    flag_misic = False
    from main import SIZE, show_menu
    from btn import Button
    from update_score import update
    flag_of_input = False
    if not flag_misic:
        pygame.mixer.music.load('Music/mainmenu.mp3')
        pygame.mixer.music.play(-1)
        flag_misic = True
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    running = True
    btn = Button(60, 60, screen, show_menu, msc=flag_misic)
    fon = pygame.transform.scale(pygame.image.load('data/backgroumd_end.png'), SIZE)
    screen.blit(fon, (0, 0))
    clock = pygame.time.Clock()
    rect = pygame.Rect(300, 10, 100, 20)
    font = pygame.font.Font('data/font.ttf', 20)
    color = 'red'
    flag = False
    text_input = ''
    description = 'Нажмите на поле ввода, введите свое имя и нажмите enter для сохраннеия результата'
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if rect.collidepoint(pos) and not flag_of_input:
                    flag = not flag
                if flag:
                    color = 'black'
                else:
                    color = 'red'
            if event.type == pygame.KEYDOWN:
                if flag and not flag_of_input:
                    if event.key == pygame.K_RETURN:
                        update(id, score, text_input)
                        text_input = ''
                        flag_of_input = True
                    elif event.key == pygame.K_BACKSPACE:
                        text_input = text_input[:-1]
                    else:
                        text_input += event.unicode
        screen.blit(fon, (0, 0))
        btn.draw(10, 530, 'BACK', number=43)
        screen.blit(font.render(score, True, 'black'), (220, 500))
        screen.blit(pygame.font.Font('data/font.ttf', 13).render(description, True, 'black'), (10, 100))
        if flagst:
            screen.blit(pygame.font.Font('data/font.ttf', 100).render('YOU', True, 'black'), (270, 200))
            screen.blit(pygame.font.Font('data/font.ttf', 100).render('WIN', True, 'black'), (300, 300))
        else:
            screen.blit(
                pygame.font.Font('data/font.ttf', 100).render('GAME', True,
                                                              'black'),
                (270, 200))
            screen.blit(
                pygame.font.Font('data/font.ttf', 100).render('OVER', True,
                                                              'black'),
                (270, 300))
        txt = font.render(text_input, True, color)
        if txt.get_width() + 5> rect.width:
            rect.width = txt.get_width() + 5
        screen.blit(txt, (rect.x + 5, rect.y))
        pygame.draw.rect(screen, color, rect, 2)
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    end_screen('100', id, 1)
    pygame.quit()

