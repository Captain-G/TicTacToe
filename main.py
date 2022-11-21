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
isBool = True

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


def draw(x, y):
    global is_even  # is_even is False
    global isBool
    if is_even:
        screen.blit(nought_img, (x, y))
        is_even = False
    elif not is_even:
        screen.blit(cross_img, (x, y))
        is_even = True


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
        draw(5, 11)
    if position_2:
        draw(183.5, 11)
    if position_3:
        draw(348.5, 11)
    if position_4:
        draw(18.5, 161)
    if position_5:
        draw(183.5, 161)
    if position_6:
        draw(348.5, 161)
    if position_7:
        draw(18.5, 311)
    if position_8:
        draw(183.5, 311)
    if position_9:
        draw(348.5, 311)

    # if position_1 and position_2 and position_3:
    #     print("Player wins")
    # elif position_4 and position_5 and position_6:
    #     print("Player wins")
    # elif position_7 and position_8 and position_9:
    #     print("Player wins")
    # elif position_1 and position_4 and position_7:
    #     print("Player wins")
    # elif position_2 and position_5 and position_8:
    #     print("Player wins")
    # elif position_3 and position_6 and position_9:
    #     print("Player wins")
    # elif position_7 and position_5 and position_3:
    #     print("Player wins")
    # elif position_1 and position_5 and position_9:
    #     print("Player wins")

    pygame.display.update()
