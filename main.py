import pygame
import random
from btn import Button
from end_screen import end_screen
from pole_igrok import Board_player
from start import start_screen
from saving import saving
from Ball import Ball, Border, Barrier, Animated_enemy, load_image, Table, Particle

SIZE = WIDTH, HEIGHT = 800, 600
START = start_x, start_y = 360, 165
BOARD = BOARD_WIDTH, BOARD_HEIGHT = 130, 215
CELL_SIZE = 5
STANDART_SCORE = 100

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('PyPong')


levels = {
          1: [1, 0, 0, 0, 38, 'Music/Lazy Walk - Cheel.mp3', 50, '1.png', 'skin_for_table2.jpg'],
          2: [2, 0, 0, 1, 30, 'Music/Sunset Dream - Cheel.mp3', 45, '1.png', 'skin_for_table2.jpg'],
          3: [3, 0, 1, 0, 30, 'Music/Sunday Rain - Cheel.mp3', 40, '2.png', 'skin_for_table2.jpg'],
          4: [4, 1, 0, 0, 30, 'Music/MydNyte - Noir Et Blanc Vie.mp3', 35, '3.png', 'skin_for_table2.jpg'],
          5: [5, 1, 1, 0, 30, 'Music/Knowpe - Noir Et Blanc Vie.mp3', 30, '5.png', 'skin_for_table2.jpg'],
          6: [6, 0, 1, 1, 30, 'Music/Empire Seasons - Dan Henig.mp3', 25, '5.png', 'skin_for_table2.jpg'],
          7: [7, 1, 1, 1, 30, 'Music/Blue Dream - Cheel.mp3', 20, '5.png', 'skin_for_table2.jpg']
           }


def show_menu(flag_misic):
    if not flag_misic:
        pygame.mixer.music.load('Music/mainmenu.mp3')
        pygame.mixer.music.play(-1)
        flag_misic = True
    fon = pygame.transform.scale(pygame.image.load('data/sample.jpg'), (SIZE))
    show = True
    font = pygame.font.Font('data/font.ttf', 20)
    text = font.render('Выбор уровня', False, 'black')
    clear_btn = Button(270, 30, screen, game)
    frst_btn = Button(104, 30, screen, game, levels, msc=flag_misic)
    scnd_btn = Button(104, 30, screen, game, levels, msc=flag_misic)
    th_btn = Button(104, 30, screen, game, levels, msc=flag_misic)
    four_btn = Button(104, 30, screen, game, levels, msc=flag_misic)
    fiv_btn = Button(104, 30, screen, game, levels, msc=flag_misic)
    sx_btn = Button(104, 30, screen, game, levels, msc=flag_misic)
    sv_btn = Button(104, 30, screen, game, levels,msc=flag_misic)
    ex_btn = Button(70, 70, screen, show_menu)
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(fon, (0, 0))
        screen.blit(text, (10, 10))
        if saving() == 1:
            frst_btn.draw(100, 100, '1 Уровень', number=1)
        if saving() == 2:
            frst_btn.draw(100, 100, '1 Уровень', number=1)
            scnd_btn.draw(100, 150, '2 Уровень', number=2)
        if saving() == 3:
            frst_btn.draw(100, 100, '1 Уровень', number=1)
            scnd_btn.draw(100, 150, '2 Уровень', number=2)
            th_btn.draw(100, 200, '3 Уровень', number=3)
        if saving() == 4:
            frst_btn.draw(100, 100, '1 Уровень', number=1)
            scnd_btn.draw(100, 150, '2 Уровень', number=2)
            th_btn.draw(100, 200, '3 Уровень', number=3)
            four_btn.draw(250, 100, '4 Уровень', number=4)
        if saving() == 5:
            frst_btn.draw(100, 100, '1 Уровень', number=1)
            scnd_btn.draw(100, 150, '2 Уровень', number=2)
            th_btn.draw(100, 200, '3 Уровень', number=3)
            four_btn.draw(250, 100, '4 Уровень', number=4)
            fiv_btn.draw(250, 150, '5 Уровень', number=5)
        if saving() == 6:
            frst_btn.draw(100, 100, '1 Уровень', number=1)
            scnd_btn.draw(100, 150, '2 Уровень', number=2)
            th_btn.draw(100, 200, '3 Уровень', number=3)
            four_btn.draw(250, 100, '4 Уровень', number=4)
            fiv_btn.draw(250, 150, '5 Уровень', number=5)
            sx_btn.draw(250, 200, '6 Уровень', number=6)
        if saving() == 7:
            frst_btn.draw(100, 100, '1 Уровень', number=1)
            scnd_btn.draw(100, 150, '2 Уровень', number=2)
            th_btn.draw(100, 200, '3 Уровень', number=3)
            four_btn.draw(250, 100, '4 Уровень', number=4)
            fiv_btn.draw(250, 150, '5 Уровень', number=5)
            sx_btn.draw(250, 200, '6 Уровень', number=6)
            sv_btn.draw(250, 250, '7 Уровень', number=7)
        clear_btn.draw(500, 550, 'Очистить таблицу лидеров', number=69)
        ex_btn.draw(10, 500, 'BACK', number=99, action=start_screen)
        pygame.display.flip()


def game(id, shadow, wind, double, fps, track_name, ball_speed, opponent_jpg, table_jpg, music):
    player = Board_player(3, 1)
    hit = pygame.mixer.Sound("music/pingpong_hit.wav")
    enemy_jpg = load_image(opponent_jpg, 120, 60)
    all_sprites = pygame.sprite.Group()
    ball_sprites = pygame.sprite.Group()
    border = pygame.sprite.Group()
    barrier = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    table_sprite = pygame.sprite.Group()
    particle_sprites = pygame.sprite.Group()

    Table(start_x, start_y, table_jpg, all_sprites, table_sprite)
    Ball(all_sprites, ball_sprites, wind, shadow)
    Border(start_x, start_y, start_x + BOARD_WIDTH, all_sprites, border)
    Barrier(start_x, start_y + BOARD_HEIGHT // 2, start_x + BOARD_HEIGHT,
            all_sprites, barrier)
    Animated_enemy(enemy_jpg, 3, 1, start_x + BOARD_WIDTH // 2, start_y,
                   all_sprites, enemy_sprites)

    button_pressed = pygame.USEREVENT + 1
    move_ball = pygame.USEREVENT + 2
    opponent_hit = pygame.USEREVENT + 3
    particle_appear = pygame.USEREVENT + 4
    opponent_flag = False
    particle_flag = False
    player.set_view(player.left, player.top, player.cell_size)
    score = 0
    running = True
    flag = False
    pause_flag = False
    pygame.time.set_timer(move_ball, 50)
    player.mainpos = True
    pygame.mixer.music.load(track_name)
    pygame.mixer.music.play(0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                break
            if event.type == particle_appear:
                particle_flag = False
                for elem in particle_sprites:
                    elem.kill()
            if event.type == move_ball and not pause_flag:
                for elem in ball_sprites:
                    ans = elem.update(border, barrier)
                    if ans:
                        coords = elem.get_coords()
                        opponent_flag = True
                        pygame.time.set_timer(opponent_hit, 200)
                        if ans == 1:
                            enemy_sprites.update(coords[1], start_y - 40, 0)
                        else:
                            enemy_sprites.update(coords[1], start_y - 40, 2)
                    else:
                        if not opponent_flag:
                            enemy_sprites.update(start_x + BOARD_WIDTH // 2,
                                                 start_y - 40, 1)
                pygame.time.set_timer(move_ball, ball_speed)
            if event.type == opponent_hit:
                opponent_flag = False
            if event.type == button_pressed and not pause_flag:
                for i in range(3):
                    player.board[0][i] = 0
                pygame.time.set_timer(button_pressed, 0)
                flag = False
                player.mainpos = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if pause_flag:
                        pause_flag = False
                        pygame.mixer.music.unpause()
                    else:
                        pause_flag = True
                        pygame.mixer.music.pause()
                if event.key == 109:
                    pygame.mixer.music.stop()
                    music = False
                    show_menu(music)
                    return
                if not flag:
                    key_pressed = player.get_click(event.key)
                    if key_pressed:
                        pygame.time.set_timer(button_pressed, 200)
                        flag = True
                        player.mainpos = False
        screen.fill([255, 255, 255])
        fone = pygame.transform.scale(pygame.image.load('data/back.jpg'), SIZE)
        screen.blit(fone, (0, 0))
        if pause_flag:
            text = 'Игра на паузе, нажмите "ESC" для подолжения или M(англ) для выхода на меню уровней.'
            font_type = pygame.font.Font('data/font.ttf', 13)
            text = font_type.render(text, True, (255, 255, 255))
            screen.blit(text, (10, 100))
        if player.get_coords():
            for elem in ball_sprites:
                coords = elem.get_coords()
                if player.get_coords()[0] < coords[0] < (
                        player.get_coords()[0] + player.cell_size) and \
                        player.get_coords()[1] < coords[1] < (
                        player.get_coords()[1] + player.cell_size):
                    if coords[1] - start_x < 10:
                        elem.rect = elem.rect.move(5, 0)
                    if start_x + BOARD_WIDTH - coords[1] < 10:
                        elem.rect = elem.rect.move(-5, 0)
                    pygame.time.set_timer(particle_appear, 350)
                    if elem.wind_flag:
                        elem.wind_flag = False
                        elem.p_coord += elem.wind_move
                        elem.wind_move = 0
                    if elem.vy > 0:
                        hit.play()
                        board_height = start_y + BOARD_HEIGHT
                        if board_height - CELL_SIZE * 5 < coords[
                            0] < board_height - CELL_SIZE * 4 or board_height - CELL_SIZE * 1 < \
                                coords[0] < board_height - CELL_SIZE * 0:
                            score += STANDART_SCORE // 2
                            for i in range(50):
                                Particle(random.randint(0, WIDTH),
                                         random.randint(0, HEIGHT), all_sprites,
                                         particle_sprites)
                                particle_flag = True
                        elif board_height - CELL_SIZE * 4 < coords[
                            0] < board_height - CELL_SIZE * 3 or board_height - CELL_SIZE * 2 < \
                                coords[0] < board_height - CELL_SIZE * 1:
                            score += STANDART_SCORE * 3 // 4
                            for i in range(100):
                                Particle(random.randint(0, WIDTH),
                                         random.randint(0, HEIGHT), all_sprites,
                                         particle_sprites)
                                particle_flag = True
                        else:
                            for i in range(200):
                                Particle(random.randint(0, WIDTH),
                                         random.randint(0, HEIGHT), all_sprites,
                                         particle_sprites)
                                particle_flag = True
                            score += STANDART_SCORE
                        elem.vy = -4
                        elem.a_coord = random.randint(0, 2)
                    if double:
                        Ball(all_sprites, ball_sprites, wind, shadow)
                        double = False
        if not pygame.mixer.music.get_busy() and not pause_flag:
            coords = []
            for elem in ball_sprites:
                coords.append((elem.get_coords()))
            if len(coords) == 1:
                for elem in ball_sprites:
                    vy = coords[0][0] // 10
                    for i in range(10):
                        elem.vy = - vy
                        elem.rect = elem.rect.move(elem.vx, elem.vy)
                        enemy_sprites.draw(screen)
                        table_sprite.draw(screen)
                        barrier.draw(screen)
                        ball_sprites.draw(screen)
                        pygame.display.flip()
                        clock.tick(fps)

            else:
                if coords[0][0] > coords[1][0]:
                    flag_elem = False
                    for elem in ball_sprites:
                        if flag_elem:
                            vy = coords[1][0] // 10
                            for i in range(10):
                                elem.vy = - vy
                                elem.rect = elem.rect.move(elem.vx, elem.vy)
                                enemy_sprites.draw(screen)
                                table_sprite.draw(screen)
                                barrier.draw(screen)
                                ball_sprites.draw(screen)
                                pygame.display.flip()
                                clock.tick(fps)
                        else:
                            flag_elem = True
                else:
                    flag_elem = True
                    for elem in ball_sprites:
                        if flag_elem:
                            vy = coords[1][0] // 10
                            for i in range(10):
                                elem.vy = - vy
                                elem.rect = elem.rect.move(elem.vx, elem.vy)
                                enemy_sprites.draw(screen)
                                table_sprite.draw(screen)
                                barrier.draw(screen)
                                ball_sprites.draw(screen)
                                pygame.display.flip()
                                clock.tick(fps)
                        else:
                            flag_elem = False
            pygame.mixer.music.stop()
            end_screen(str(score), id, 1)
        pygame.draw.rect(screen, (255, 255, 255), (360, 165, 130, 215), 1)
        for elem in ball_sprites:
            coords = elem.get_coords()
            if coords[0] > start_y + BOARD_HEIGHT:
                pygame.mixer.music.stop()
                end_screen(str(score), id)
        if particle_flag:
            particle_sprites.draw(screen)
        enemy_sprites.draw(screen)
        table_sprite.draw(screen)
        barrier.draw(screen)
        ball_sprites.draw(screen)
        player.render(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


if __name__ == '__main__':
    start_screen(show_menu)
