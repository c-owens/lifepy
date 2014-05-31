'''
Context object for things shared throughout the module, for instance logging.
'''
__author__ = 'cody.owens@gmail.com'

class GameContext(object):
    def __init__(self, logger, displaySurface, cells, clock, deltaTime):
        self.logger = logger
        self.displaySurface = displaySurface
        self.cells = cells
        self.clock = clock
        self.deltaTime = deltaTime