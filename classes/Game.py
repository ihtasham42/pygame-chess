from classes.Board import Board
import constants
import pygame


class Game():
    def __init__(self):
        self.board = Board(self)

        self.init_pygame()
        self.run_game_loop()

    def init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode(constants.SCREEN_SIZE)

    def run_game_loop(self):
        self.running = True
        clock = pygame.time.Clock()

        while True:
            clock.tick(constants.FPS)
            self.handle_inputs()
            if not self.running:
                break
            self.update()
            self.draw()

        pygame.quit()

    def handle_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.screen.fill(constants.BLACK)
        self.board.draw()
        pygame.display.update()
