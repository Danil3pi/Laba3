import pygame
from pygame.draw import *

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000
MAIN_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


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
    draw_face((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 300)
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


def draw_mount():
    pass


def draw_eyes():
    pass


def draw_eyebrows():
    pass

main()
pygame.quit()