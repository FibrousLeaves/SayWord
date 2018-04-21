import pygame
import random

pygame.init()
screen = pygame.display.set_mode((780, 500))
done = False

def title():
    font = pygame.font.SysFont("tahoma", 30)
    text = font.render("Which word is spelled incorrectly?", True, (255, 150, 0))
    screen.blit(text,
            (390 - text.get_width() // 2, 50 - text.get_height() // 2))

def firstRectangles(word):
    font = pygame.font.SysFont("tahoma", 42)
    text = font.render(word, True, (118, 238, 198))
    screen.blit(text,
            (190 - text.get_width() // 2, 180 - text.get_height() // 2))
    return word
def secondRectangles(word):
    font = pygame.font.SysFont("tahoma", 42)
    text = font.render(word, True, (118, 238, 198))
    screen.blit(text,
            (190 - text.get_width() // 2, 280 - text.get_height() // 2))
    return word

def thirdRectangles(word):
    font = pygame.font.SysFont("tahoma", 42)
    text = font.render(word, True, (118, 238, 198))
    screen.blit(text,
            (570 - text.get_width() // 2, 180 - text.get_height() // 2))
    return word

def fourthRectangles(word):
    font = pygame.font.SysFont("tahoma", 42)
    text = font.render(word, True, (118, 238, 198))
    screen.blit(text,
            (570 - text.get_width() // 2, 280 - text.get_height() // 2))
    return word

def editWord(word):
    newword = ""
    for y in range(len(word)):
        if y == (len(word)-5):
            newword = newword
        else:
            newword = newword+word[y]
    return newword

def GetList():
    open_file = open("CHAOTIC MODE.txt", "r")
    wordlist = []
    word = open_file.readline()
    word = word.strip("\n")
    wordlist.append(word)
    while word != "":
        word = open_file.readline()
        word = word.strip("\n")
        wordlist.append(word)
    open_file.close()
    return wordlist

def Main():
    color = (0, 0, 139)
    color2 = (0, 0, 139)
    color3 = (0, 0, 139)
    color4 = (0, 0, 139)
    pygame.draw.rect(screen, color, pygame.Rect(25, 150, 350, 70))
    pygame.draw.rect(screen, color, pygame.Rect(25, 250, 350, 70))
    pygame.draw.rect(screen, color2, pygame.Rect(400, 150, 350, 70))
    pygame.draw.rect(screen, color2, pygame.Rect(400, 250, 350, 70))
    title()
    wordlist = GetList()
    print (wordlist)
    num = random.randrange(0,len(wordlist))
    wordlist[0] = editWord(wordlist[0])
    firstRectangles(wordlist[0])
    print (wordlist[0])
    secondRectangles(wordlist[1])
    print (wordlist[1])
    thirdRectangles(wordlist[2])
    print (wordlist[2])
    fourthRectangles(wordlist[3])
    print (wordlist[3])
    while not done:
        pygame.display.flip()
Main()
