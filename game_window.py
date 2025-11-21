import pygame


class GameWindow:
    def __init__(self, width: int | float, height: int | float) -> None:
        self.__bounds = (width, height)
        self.__screen = pygame.display.set_mode(self.__bounds)

        pygame.display.set_caption("Симуляция экономики города")
        self.__font = pygame.font.SysFont("arial", 14)

    def draw(self) -> None:
        pass
