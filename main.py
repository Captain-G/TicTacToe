import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 450))

pygame.display.set_caption("TicTacToe")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

cross_img = pygame.image.load("x.png")
nought_img = pygame.image.load("o.png")

counter = 1
presses = 1
pos = 0
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

shape1 = "none"
shape2 = "none"
shape3 = "none"
shape4 = "none"
shape5 = "none"
shape6 = "none"
shape7 = "none"
shape8 = "none"
shape9 = "none"


def cross(x, y):
    screen.blit(cross_img, (x, y))


def nought(x, y):
    screen.blit(nought_img, (x, y))


def draw(pos, shape, x, y):
    global presses

    global shape1
    global shape2
    global shape3
    global shape4
    global shape5
    global shape6
    global shape7
    global shape8
    global shape9

    # position 1
    if pos == 1 and shape1 == "none":
        if presses % 2 == 0:
            screen.blit(nought_img, (x, y))
            shape1 = "o"
        else:
            screen.blit(cross_img, (x, y))
            shape1 = "x"
    elif pos == 1 and shape1 == "x":
        screen.blit(cross_img, (x, y))
    elif pos == 1 and shape1 == "o":
        screen.blit(nought_img, (x, y))

    # position 2
    if pos == 2 and shape2 == "none":
        if presses % 2 == 0:
            screen.blit(nought_img, (x, y))
            shape2 = "o"
        else:
            screen.blit(cross_img, (x, y))
            shape2 = "x"
    elif pos == 2 and shape2 == "x":
        screen.blit(cross_img, (x, y))
    elif pos == 2 and shape2 == "o":
        screen.blit(nought_img, (x, y))

    # position 3
    if pos == 3 and shape3 == "none":
        if presses % 2 == 0:
            screen.blit(nought_img, (x, y))
            shape3 = "o"
        else:
            screen.blit(cross_img, (x, y))
            shape3 = "x"
    elif pos == 3 and shape3 == "x":
        screen.blit(cross_img, (x, y))
    elif pos == 3 and shape3 == "o":
        screen.blit(nought_img, (x, y))

    # position 4
    if pos == 4 and shape4 == "none":
        if presses % 2 == 0:
            screen.blit(nought_img, (x, y))
            shape4 = "o"
        else:
            screen.blit(cross_img, (x, y))
            shape4 = "x"
    elif pos == 4 and shape4 == "x":
        screen.blit(cross_img, (x, y))
    elif pos == 4 and shape4 == "o":
        screen.blit(nought_img, (x, y))

    # position 5
    if pos == 5 and shape5 == "none":
        if presses % 2 == 0:
            screen.blit(nought_img, (x, y))
            shape5 = "o"
        else:
            screen.blit(cross_img, (x, y))
            shape5 = "x"
    elif pos == 5 and shape5 == "x":
        screen.blit(cross_img, (x, y))
    elif pos == 5 and shape5 == "o":
        screen.blit(nought_img, (x, y))

    # position 6
    if pos == 6 and shape6 == "none":
        if presses % 2 == 0:
            screen.blit(nought_img, (x, y))
            shape6 = "o"
        else:
            screen.blit(cross_img, (x, y))
            shape6 = "x"
    elif pos == 6 and shape6 == "x":
        screen.blit(cross_img, (x, y))
    elif pos == 6 and shape6 == "o":
        screen.blit(nought_img, (x, y))

    # position 7
    if pos == 7 and shape7 == "none":
        if presses % 2 == 0:
            screen.blit(nought_img, (x, y))
            shape7 = "o"
        else:
            screen.blit(cross_img, (x, y))
            shape7 = "x"
    elif pos == 7 and shape7 == "x":
        screen.blit(cross_img, (x, y))
    elif pos == 7 and shape7 == "o":
        screen.blit(nought_img, (x, y))

    # position 8
    if pos == 8 and shape8 == "none":
        if presses % 2 == 0:
            screen.blit(nought_img, (x, y))
            shape8 = "o"
        else:
            screen.blit(cross_img, (x, y))
            shape8 = "x"
    elif pos == 8 and shape8 == "x":
        screen.blit(cross_img, (x, y))
    elif pos == 8 and shape8 == "o":
        screen.blit(nought_img, (x, y))

    # position 9
    if pos == 9 and shape9 == "none":
        if presses % 2 == 0:
            screen.blit(nought_img, (x, y))
            shape9 = "o"
        else:
            screen.blit(cross_img, (x, y))
            shape9 = "x"
    elif pos == 9 and shape9 == "x":
        screen.blit(cross_img, (x, y))
    elif pos == 9 and shape9 == "o":
        screen.blit(nought_img, (x, y))


running = True
while running:

    screen.fill((178, 190, 181))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP7:
                position_1 = True
                presses += 1
            elif event.key == pygame.K_KP8:
                position_2 = True
                presses += 1
            elif event.key == pygame.K_KP9:
                position_3 = True
                presses += 1
            elif event.key == pygame.K_KP4:
                position_4 = True
                presses += 1
            elif event.key == pygame.K_KP5:
                position_5 = True
                presses += 1
            elif event.key == pygame.K_KP6:
                position_6 = True
                presses += 1
            elif event.key == pygame.K_KP1:
                position_7 = True
                presses += 1
            elif event.key == pygame.K_KP2:
                position_8 = True
                presses += 1
            elif event.key == pygame.K_KP3:
                position_9 = True
                presses += 1

    # vertical
    pygame.draw.line(screen, (0, 0, 0), (165, 0), (165, 450), width=3)
    pygame.draw.line(screen, (0, 0, 0), (330, 0), (330, 450), width=3)

    # horizontal
    pygame.draw.line(screen, (0, 0, 0), (0, 150), (500, 150), width=3)
    pygame.draw.line(screen, (0, 0, 0), (0, 300), (500, 300), width=3)

    if position_1:
        pos = 1
        draw(pos, shape1, 18.5, 11)
    if position_2:
        pos = 2
        draw(pos, shape2, 183.5, 11)
    if position_3:
        pos = 3
        draw(pos, shape3, 348.5, 11)
    if position_4:
        pos = 4
        draw(pos, shape4, 18.5, 161)
    if position_5:
        pos = 5
        draw(pos, shape5, 183.5, 161)
    if position_6:
        pos = 6
        draw(pos, shape6, 348.5, 161)
    if position_7:
        pos = 7
        draw(pos, shape7, 18.5, 311)
    if position_8:
        pos = 8
        draw(pos, shape8, 183.5, 311)
    if position_9:
        pos = 9
        draw(pos, shape9, 348.5, 311)

    # win instance
    if shape1 == shape2 == shape3 and shape1 != "none":
        pygame.draw.line(screen, (80, 200, 120), (0, 50), (500, 50), width=10)
        pygame.draw.line(screen, (80, 200, 120), (0, 100), (500, 100), width=10)
    elif shape4 == shape5 == shape6 and shape4 != "none":
        pygame.draw.line(screen, (80, 200, 120), (0, 200), (500, 200), width=10)
        pygame.draw.line(screen, (80, 200, 120), (0, 250), (500, 250), width=10)
    elif shape7 == shape8 == shape9 and shape7 != "none":
        pygame.draw.line(screen, (80, 200, 120), (0, 350), (500, 350), width=10)
        pygame.draw.line(screen, (80, 200, 120), (0, 400), (500, 400), width=10)

    elif shape1 == shape4 == shape7 and shape1 != "none":
        pygame.draw.line(screen, (80, 200, 120), (55, 0), (55, 450), width=10)
        pygame.draw.line(screen, (80, 200, 120), (110, 0), (110, 450), width=10)
    elif shape2 == shape5 == shape8 and shape2 != "none":
        pygame.draw.line(screen, (80, 200, 120), (220, 0), (220, 450), width=10)
        pygame.draw.line(screen, (80, 200, 120), (275, 0), (275, 450), width=10)
    elif shape3 == shape6 == shape9 and shape3 != "none":
        pygame.draw.line(screen, (80, 200, 120), (385, 0), (385, 450), width=10)
        pygame.draw.line(screen, (80, 200, 120), (440, 0), (440, 450), width=10)
    elif shape7 == shape5 == shape3 and shape7 != "none":
        pygame.draw.line(screen, (80, 200, 120), (485, 0), (0, 435), width=10)
        pygame.draw.line(screen, (80, 200, 120), (500, 15), (15, 450), width=10)
    elif shape1 == shape5 == shape9 and shape1 != "none":
        pygame.draw.line(screen, (80, 200, 120), (15, 0), (500, 435), width=10)
        pygame.draw.line(screen, (80, 200, 120), (0, 15), (485, 450), width=10)

    clock.tick(30)
    pygame.display.update()
