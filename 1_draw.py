import pygame
from pygame.draw import *

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
MAIN_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
MAIN_SCREEN.fill([255, 255, 255])

def main():
    loop()


def loop():
    FPS = 30
    tack = pygame.time.Clock ()

    draw_smile ()

    while True:
        tack.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        pygame.display.update()


def draw_smile():
    """
    Нужна система координат.
    :return:
    """
    draw_face((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 250)
    draw_mount()
    draw_eyes()
    draw_eyebrows()


def draw_face(face_position : tuple, face_radius : int) -> None:
    """
    Рисует лицо нашего человека.
    :param face_position: Позиция лица
    :param face_radius: Радиус лица
    :return: Ничего
    """
    circle(MAIN_SCREEN, (255, 255, 1), face_position, face_radius)
    circle(MAIN_SCREEN, 'black', face_position, face_radius, 3)


def draw_mount():
    """
    Рисует рот.
    :return:
    """
    rect(MAIN_SCREEN, (0, 0, 0), (100, 300, 300, 70))


def draw_eyes():
    # left eye
    circle(MAIN_SCREEN, 'red', (150, 150), 45)
    circle(MAIN_SCREEN, 'black', (150, 150), 15)

    # right eye
    circle(MAIN_SCREEN, 'red', (SCREEN_WIDTH - 175, 150), 30)
    circle(MAIN_SCREEN, 'black', (SCREEN_WIDTH - 175, 150), 10)


def draw_eyebrows():
    polygon(MAIN_SCREEN, 'black', [(12, 14), (140, 14), (150, 52)])

main()
pygame.quit()