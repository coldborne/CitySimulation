import pygame

from game_window import GameWindow


class Application:
    def __init__(self):
        pygame.init()
        self.__game_window = GameWindow(900, 600)

    def run(self):
        is_running = True

        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

            self.__game_window.draw()
            pygame.display.flip()
