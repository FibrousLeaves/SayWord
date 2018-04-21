import pygame

pygame.init()
screen = pygame.display.set_mode((780, 500))
done = False

def title():
    font = pygame.font.SysFont("tahoma", 30)
    text = font.render("Volume Settings", True, (255, 150, 0))
    screen.blit(text,
            (390 - text.get_width() // 2, 50 - text.get_height() // 2))

def firstRectangles():
    font = pygame.font.SysFont("tahoma", 50)
    text = font.render("SFX", True, (255, 255, 255))
    screen.blit(text,
            (200 - text.get_width() // 2, 180 - text.get_height() // 2))

def secondRectangles():
    font = pygame.font.SysFont("tahoma", 50)
    text = font.render("Volume", True, (255, 255, 255))
    screen.blit(text,
            (200 - text.get_width() // 2, 280 - text.get_height() // 2))
def main():
    while not done:
    is_red = True
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True
            if is_red:
                color = (255, 255, 255)
            else:
                color = (255, 0, 0)
            color2 = (130, 130, 130)
            if event.type == pygame.K_DOWN and event.key == pygame.K_SPACE:
                is_red = not is_red
            widthA = 350
            widthB = 300
            widthC = 300
            pygame.draw.rect(screen, color, pygame.Rect(350, 150, widthA, 70))
            pygame.draw.rect(screen, color2, pygame.Rect(350, 150, widthB, 70))
            pygame.draw.rect(screen, color, pygame.Rect(350, 250, widthA, 70))
            pygame.draw.rect(screen, color2, pygame.Rect(350, 250, widthC, 70))
            title()
            firstRectangles()
            secondRectangles()
            for event in pygame.event.get():
                    select = 0
                    if event.type == pygame.K_s:
                        select = select + 1
                        if select % 2 != 0:
                            if event.key == pygame.K_a:
                                if widthC > 0:
                                    widthC = widthC - 30
                                    color2 = (200, 229, 235)
                                    pygame.draw.rect(screen, color2, pygame.Rect(350, 150, widthC, 70))

                            if event.key == pygame.K_d:
                                if widthC > 0:
                                    widthC = widthC + 30
                                    color2 = (200, 229, 235)
                                    pygame.draw.rect(screen, color2, pygame.Rect(350, 150, widthC, 70))
                        else:
                            select = select + 1
                            if event.key == pygame.K_a:
                                if widthC > 0:
                                    widthC = widthB - 30
                                    color2 = (200, 229, 235)
                                    pygame.draw.rect(screen, color2, pygame.Rect(350, 150, widthB, 70))

                            if event.key == pygame.K_d:
                                if widthC > 0:
                                    widthC = widthB + 30
                                    color2 = (200, 229, 235)
                                    pygame.draw.rect(screen, color2, pygame.Rect(350, 150, widthB, 70))
                    else:
                        select = select + 1
                        if event.key == pygame.K_a:
                            if widthC > 0:
                                widthC = widthC - 30
                                pygame.draw.rect(screen, color2, pygame.Rect(350, 150, widthC, 70))

                        if event.key == pygame.K_d:
                            if widthC > 0:
                                widthC = widthC + 30
                                pygame.draw.rect(screen, color2, pygame.Rect(350, 150, widthC, 70))

            s_image = pygame.image.load("socialmedia.png")
            screen.blit(s_image, (-1, 442))
            pygame.display.flip()
main()
