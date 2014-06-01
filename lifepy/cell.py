'''
A single cell in the life game. Holds references to neighbors and runs
logic to determine if it should live or die.
'''
__author__ = 'cody.owens@gmail.com'
from random import randint

class Cell(object):
    # True when the cell is currently alive.
    # It should be set by executing evaluate, and then update.
    alive = False

    # A random color is assigned to this cell every time update is called.
    # This isn't used internally, it's here for convenience for the renderer.
    color = (0, 0, 0)

    # Neighbors will be in a list, starting with the top left (northwest)
    # neighbor, and moving clockwise from there.
    neighbors = []

    # Result of the previous evaluate.
    _evaluate_result = False

    def __init__(self, neighbors):
        self.neighbors = neighbors

    def evaluate(self):
        '''
        Evaluate if the cell should live or die. Because all cells should evaluate
        at the same time, the results will not be applied immediately. Instead, the
        result will be stored until the update method is executed.
        '''
        live = 0
        dead = 0
        for cell in self.neighbors:
            if cell is None or cell.alive == False:
                dead += 1
                continue
            live += 1

        # Cells 'reproduce' when a dead cell is next to exactly 3 live ones.
        isAlive = self._evaluate_result
        if not isAlive and live == 3:
            self._evaluate_result = True
        elif not isAlive:
            self._evaluate_result = False # Dead cells without 3 neighbors stay dead.
        elif isAlive:
            if live == 2 or live == 3: # Stay alive with 2 or 3 live neighbors.
                self._evaluate_result = True
            else:
                self._evaluate_result = False

        return self._evaluate_result

    def update(self):
        self.alive = self._evaluate_result
        self.color = self.get_random_color()

    def get_random_color(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


