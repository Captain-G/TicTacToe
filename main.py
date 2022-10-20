import pygame

pygame.init()

screen = pygame.display.set_mode((500, 450))

pygame.display.set_caption("TicTacToe")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

cross_img = pygame.image.load("x.png")
nought_img = pygame.image.load("o.png")

counter = 1
this = 0



def cross(x, y):
    screen.blit(cross_img, (x, y))


def nought(x, y):
    screen.blit(nought_img, (x, y))


def draw(count, x, y):
    count += 1
    if count % 2 != 0:
        screen.blit(nought_img, (x, y))
    else:
        screen.blit(cross_img, (x, y))


running = True
while running:

    screen.fill((155, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.line(screen, (0, 0, 0), (165, 0), (165, 450), width=3)
    pygame.draw.line(screen, (0, 0, 0), (330, 0), (330, 450), width=3)

    pygame.draw.line(screen, (0, 0, 0), (0, 150), (500, 150), width=3)
    pygame.draw.line(screen, (0, 0, 0), (0, 300), (500, 300), width=3)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    left, middle, right = pygame.mouse.get_pressed()

    position = 0
    if mouse_x < 165 and mouse_y < 150:
        position = 1
    elif mouse_x < 330 and mouse_y < 150:
        position = 2
    elif mouse_x < 495 and mouse_y < 150:
        position = 3
    elif mouse_x < 165 and mouse_y < 300:
        position = 4
    elif mouse_x < 330 and mouse_y < 300:
        position = 5
    elif mouse_x < 495 and mouse_y < 300:
        position = 6
    elif mouse_x < 165 and mouse_y > 300:
        position = 7
    elif mouse_x < 330 and mouse_y > 300:
        position = 8
    elif mouse_x > 330 and mouse_y > 300:
        position = 9
    else:
        position = 0

    is_clicked = left

    if position == 1 and is_clicked:
        this = 1
    elif position == 2 and is_clicked:
        this = 2
        draw(counter, 183.5, 11)
    elif position == 3 and is_clicked:
        this = 3
        draw(counter, 348.5, 11)
    if position == 4 and is_clicked:
        this = 4
        screen.blit(nought_img, (18.5, 161))
    if position == 5 and is_clicked:
        this = 5
        screen.blit(nought_img, (183.5, 161))
    if position == 6 and is_clicked:
        this = 6
        screen.blit(nought_img, (348.5, 161))
    if position == 7 and is_clicked:
        this = 7
        screen.blit(nought_img, (18.5, 311))
    if position == 8 and is_clicked:
        this = 8
        screen.blit(nought_img, (183.5, 311))
    if position == 9 and is_clicked:
        this = 9
        screen.blit(nought_img, (348.5, 311))

    if this == 1:
        draw(counter, 18.5, 11)
    if this == 2:
        draw(counter, 183.5, 11)

    pygame.display.update()
