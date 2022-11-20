import pygame

pygame.init()

screen = pygame.display.set_mode((500, 450))

pygame.display.set_caption("TicTacToe")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

cross_img = pygame.image.load("x.png")
nought_img = pygame.image.load("o.png")

counter = 1
is_even = False

position_1 = False
position_2 = False
position_3 = False
position_4 = False
position_5 = False
position_6 = False
position_7 = False
position_8 = False
position_9 = False


def cross(x, y):
    screen.blit(cross_img, (x, y))


def nought(x, y):
    screen.blit(nought_img, (x, y))


def draw(isEven, x, y):
    if isEven:
        screen.blit(nought_img, (x, y))
    else:
        screen.blit(cross_img, (x, y))
    return isEven


running = True
while running:

    screen.fill((155, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP7:
                position_1 = True
            elif event.key == pygame.K_KP8:
                position_2 = True
            elif event.key == pygame.K_KP9:
                position_3 = True
            elif event.key == pygame.K_KP4:
                position_4 = True
            elif event.key == pygame.K_KP5:
                position_5 = True
            elif event.key == pygame.K_KP6:
                position_6 = True
            elif event.key == pygame.K_KP1:
                position_7 = True
            elif event.key == pygame.K_KP2:
                position_8 = True
            elif event.key == pygame.K_KP3:
                position_9 = True

    pygame.draw.line(screen, (0, 0, 0), (165, 0), (165, 450), width=3)
    pygame.draw.line(screen, (0, 0, 0), (330, 0), (330, 450), width=3)

    pygame.draw.line(screen, (0, 0, 0), (0, 150), (500, 150), width=3)
    pygame.draw.line(screen, (0, 0, 0), (0, 300), (500, 300), width=3)

    if position_1:
        draw(is_even, 5, 11)
        if is_even:
            is_even = False
        else:
            is_even = True
    if position_2:
        draw(is_even, 183.5, 11)
        if is_even:
            is_even = False
        else:
            is_even = True
    if position_3:
        draw(is_even, 348.5, 11)
        if is_even:
            is_even = False
        else:
            is_even = True
    if position_4:
        draw(counter, 18.5, 161)
        counter += 1
    if position_5:
        draw(counter, 183.5, 161)
        counter += 1
    if position_6:
        draw(counter, 348.5, 161)
        counter += 1
    if position_7:
        draw(counter, 18.5, 311)
        counter += 1
    if position_8:
        draw(counter, 183.5, 311)
        counter += 1
    if position_9:
        draw(counter, 348.5, 311)
        counter += 1

    pygame.display.update()
