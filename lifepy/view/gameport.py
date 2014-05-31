'''
Draws the main game view, which handles displaying all of the cells.
It must be initialized with a square display area.
'''
__author__ = 'cody.owens@gmail.com'
from view.viewport import ViewPort
from random import randint
import pygame
import colors

class GamePort(ViewPort):
    _ms_total = 0
    _sec_total = 0
    def __init__(self, viewContext, gameContext):
        ViewPort.__init__(self, viewContext)
        self.gameContext = gameContext
        self.cover = pygame.Surface((self.context.width, self.context.height))
        self.font = pygame.font.SysFont("Droid Sans Mono Slashed", 30)

    def on_render(self, deltaTime):
        self._ms_total += deltaTime
        self.context.surface.blit(self.cover, (0, 0))
        label = self.font.render(str(self._ms_total), 2, colors.black)
        self.context.surface.blit(label, (10, 10))
        label = self.font.render(str(self._sec_total), 2, colors.black)
        self.context.surface.blit(label, (self.context.width - 60, 10))
        if( self._ms_total > 1000 ):
            self._sec_total = int(self._sec_total + ( self._ms_total / 1000 ))
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            color = r, g, b
            self.context.surface.fill(color)
            self.cover.fill(color)
            self._ms_total = 0
            self.gameContext.logger.debug(str(color))
        #self.gameContext.logger.debug( deltaTime )
