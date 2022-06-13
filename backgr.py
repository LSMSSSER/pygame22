def backgr(screen):
    import pygame
    from main import SIZE

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    running = True

    fone = pygame.transform.scale(pygame.image.load('data/back.jpg'), SIZE)
    screen.blit(fone, (0, 0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.flip()