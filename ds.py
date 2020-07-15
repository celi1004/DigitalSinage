##
# -*- coding: utf-8 -*-

import os
import pygame
import sys
import time

#디렉토리 안 파일 목록 가져오기
PATH_DIR = '/Users/ParkJinYoung/Desktop/cs/images'

#state 변화 상수
CHANGE_TIME = 7000

#global variable
imgList = []
idxCurrImage = 0
idxNextImage = 0

#pygame 설정
pygame.init()
DISPLAYSURF = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
background = pygame.Surface((DISPLAYSURF.get_rect().width, DISPLAYSURF.get_rect().height))
clock = pygame.time.Clock()

class Display(object):
    def __init__(self, filename):
        img = pygame.image.load(PATH_DIR + '/' + filename).convert()
        self.image = pygame.transform.scale(img, DISPLAYSURF.get_size())


def loadImages():
    global imgList, idxCurrImage, idxNextImage

    filelist = os.listdir(PATH_DIR)
    for filename in filelist:
        imgList.append(Display(filename))

    if len(imgList) == 0:
        pygame.quit
        sys.exit()
    else:
        idxCurrImage = 0
        idxNextImage = 1


def main():

    global imgList, idxCurrImage, idxNextImage

    loadImages()

    length = len(imgList)

    DISPLAYSURF.fill((255,255,255))
    background.fill((0,0,0))

    while True:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        currImage = imgList[idxCurrImage].image
        nextImage = imgList[idxNextImage].image

        idxAlpha = 0

        while idxAlpha < 255:
            currImage.set_alpha(255 - idxAlpha)
            nextImage.set_alpha(idxAlpha)

            DISPLAYSURF.blit(background, background.get_rect())
            DISPLAYSURF.blit(currImage, (0,0))
            DISPLAYSURF.blit(nextImage, (0,0))

            pygame.time.delay(1)
            pygame.display.update()

            idxAlpha += 5

        idxCurrImage = (idxCurrImage + 1) % length
        idxNextImage = (idxNextImage + 1) % length
    
        pygame.time.delay(CHANGE_TIME)

if __name__ == "__main__":
    main()