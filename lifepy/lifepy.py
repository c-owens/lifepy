__author__ = 'cody.owens@gmail.com'
import logging

import pygame

import colors
from view.gameport import GamePort
from gamecontext import GameContext
from view.viewcontext import ViewContext


class App:
    _framerate = 60
    def __init__(self):
        self._running = True
        self._display_surface = None
        self.size = self.width, self.height = 720,720

    def init_logger(self):
        logger = logging.Logger( "lifepy" )
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger

    def init_viewports(self):
        return {
          "gameport" : GamePort(ViewContext(self.context.displaySurface, 720, 720, 0, 0), self.context)
        }


    def on_init(self):
        pygame.init()
        self._running = True

        clock = pygame.time.Clock()
        displaySurface = pygame.display.set_mode( self.size, pygame.HWSURFACE | pygame.DOUBLEBUF )
        cells = []
        logger = self.init_logger()

        self.context = GameContext(logger, displaySurface, cells, clock, 0)
        self.viewports = self.init_viewports()
        self.context.displaySurface.fill(colors.black)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self._milliseconds = self.context.clock.tick(self._framerate)

    def on_render(self):
        for port in self.viewports:
            self.viewports[port].on_render(self._milliseconds)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()