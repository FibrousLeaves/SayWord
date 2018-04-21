import pygame
import random

pygame.init()
screen = pygame.display.set_mode((780, 500))
done = False

def title():
    font = pygame.font.SysFont("tahoma", 30)
    text = font.render("Which word is spelt correctly?", True, (255, 150, 0))
    screen.blit(text,
            (390 - text.get_width() // 2, 50 - text.get_height() // 2))

def firstRectangles(listofwords):
    font = pygame.font.SysFont("tahoma", 42)
    num = random.randrange(0,4)
    text = font.render(listofwords[num], True, (118, 238, 198))
    screen.blit(text,
            (190 - text.get_width() // 2, 180 - text.get_height() // 2))
    listofwords[num] = "-1"
    return listofwords

def secondRectangles(listofwords):
    font = pygame.font.SysFont("tahoma", 42)
    num = random.randrange(0,4)
    while listofwords[num] == "-1":
        num = random.randrange(0,4)
    text = font.render(listofwords[num], True, (118, 238, 198))
    screen.blit(text,
            (190 - text.get_width() // 2, 280 - text.get_height() // 2))
    listofwords[num] = "-1"
    return listofwords

def thirdRectangles(listofwords):
    font = pygame.font.SysFont("tahoma", 42)
    num = random.randrange(0,4)
    while listofwords[num] == "-1":
        num = random.randrange(0,4)
    text = font.render(listofwords[num], True, (118, 238, 198))
    screen.blit(text,
            (570 - text.get_width() // 2, 180 - text.get_height() // 2))
    listofwords[num] = "-1"
    return listofwords

def fourthRectangles(listofwords):
    font = pygame.font.SysFont("tahoma", 42)
    num = random.randrange(0,4)
    while listofwords[num] == "-1":
        num = random.randrange(0,4)
    text = font.render(listofwords[num], True, (118, 238, 198))
    screen.blit(text,
            (570 - text.get_width() // 2, 280 - text.get_height() // 2))
    listofwords[num] = "-1"
    return listofwords

def editWord(word):
    newword = ""
    newlist = []
    for x in range(4):
        if x == 0:
            for y in range(len(word)):
                newword = newword+word[y]
            newlist.append(newword)
        elif x == 1:
            for y in range(len(word)):
                if y == (len(word)-1):
                    newword = newword+word[y]+word[y]
                else:
                    newword = newword+word[y]
            newlist.append(newword)
        elif x == 2:
            for y in range(len(word)):
                if y == (len(word)-3):
                    newword = newword
                else:
                    newword = newword+word[y]
            newlist.append(newword)
        else:
            for y in range(len(word)):
                if y == (len(word)-5):
                    newword = newword
                else:
                    newword = newword+word[y]
            newlist.append(newword)
        newword = ""

    return newlist
def GetList():
    open_file = open("HARD MODE.txt", "r")
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
    num = random.randrange(0,len(wordlist))
    listofwords = editWord(wordlist[num])
    firstRectangles(listofwords)
    print (listofwords)
    secondRectangles(listofwords)
    print (listofwords)
    thirdRectangles(listofwords)
    print (listofwords)
    fourthRectangles(listofwords)
    print (listofwords)
    while not done:
        pygame.display.flip()
Main()
