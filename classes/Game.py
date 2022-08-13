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
        

        while True:
            self.draw()
            self.handle_inputs()
            if not self.running:
                break

        pygame.quit()

    def handle_inputs(self):
        clock = pygame.time.Clock()
        input_loop_running = True

        while input_loop_running:
            clock.tick(constants.FPS)
            input_loop_running = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.board.handle_click(event.pos)
                else:
                    input_loop_running = True

    def draw(self):
        self.screen.fill(constants.BLACK)
        self.board.draw()
        pygame.display.update()
