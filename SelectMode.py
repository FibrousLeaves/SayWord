import pygame

pygame.init()
screen = pygame.display.set_mode((780, 500))
done = False
class SelectMode():
    def title():
        font = pygame.font.SysFont("tahoma", 30)
        text = font.render("Please select a Difficulty", True, (255, 150, 0))
        screen.blit(text,
                (390 - text.get_width() // 2, 50 - text.get_height() // 2))

    def firstRectangles():
        font = pygame.font.SysFont("tahoma", 42)
        text = font.render("Easy", True, (0, 0, 255))
        screen.blit(text,
                (190 - text.get_width() // 2, 180 - text.get_height() // 2))

    def secondRectangles():
        font = pygame.font.SysFont("tahoma", 42)
        text = font.render("Medium", True, (0, 255, 0))
        screen.blit(text,
                (190 - text.get_width() // 2, 280 - text.get_height() // 2))

    def thirdRectangles():
        font = pygame.font.SysFont("tahoma", 42)
        text = font.render("Hard", True, (255, 0, 0))
        screen.blit(text,
                (570 - text.get_width() // 2, 180 - text.get_height() // 2))

    def fourthRectangles():
        font = pygame.font.SysFont("tahoma", 42)
        text = font.render("Chaotic", True, (255, 0, 100))
        screen.blit(text,
                (570 - text.get_width() // 2, 280 - text.get_height() // 2))

    def modeMain():
        is_red = True
        while not done:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
                if is_red:
                    color = (255, 255, 255)
                else:
                    color = (255, 0, 0)
                color2 = (255, 255, 255)
                color3 = (255, 255, 255)
                color4 = (255, 255, 255)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_red = not is_red
                pygame.draw.rect(screen, color, pygame.Rect(25, 150, 350, 70))
                pygame.draw.rect(screen, color, pygame.Rect(25, 250, 350, 70))
                pygame.draw.rect(screen, color2, pygame.Rect(400, 150, 350, 70))
                pygame.draw.rect(screen, color2, pygame.Rect(400, 250, 350, 70))
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            done = True
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            done = True
                title()
                firstRectangles()
                secondRectangles()
                thirdRectangles()
                fourthRectangles()
                s_image = pygame.image.load("flames.png")
                d_image = pygame.image.load("angry.png")
                screen.blit(d_image, (422, 145))
                screen.blit(d_image, (652, 145))
                screen.blit(s_image, (392, 255))
                screen.blit(s_image, (632, 255))
                kkey_image = pygame.image.load("keyboardkey.png")
                screen.blit(kkey_image, (352, 145))
                pygame.display.flip()
    modeMain()
