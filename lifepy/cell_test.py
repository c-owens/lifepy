from unittest import TestCase
from cell import Cell
__author__ = 'cody.owens@gmail.com'

class TestCell(TestCase):
    _cell = None

    def init_test(self):
        neighbors = []
        neighbors.extend(self.create_neighbors())
        return Cell(neighbors)

    def create_neighbors(self):
        for num in range(8):
            yield Cell([])

    def test_cell_defaults(self):
        '''
        Test the default properties of a cell.
        '''
        cell = self.init_test()
        self.assertFalse(cell.alive, "Cell is not dead by default.")
        self.assertFalse(cell.neighbors is None)
        self.assertTrue(cell.color == (0, 0, 0))
        notNullCount = 0
        for neighbor in cell.neighbors:
            if neighbor is not None:
                notNullCount += 1
        self.assertGreater(notNullCount, 0, "All neighbors are null.")

    def test_evaluate(self):
        cell = self.init_test()

        # Set one neighbor alive, expect it to stay dead.
        cell.neighbors[0].alive = True
        self.assertFalse(cell.evaluate(), "Cell alive with one live neighbor.")

        # Set a second neighbor alive, expect it to stay dead.
        cell.neighbors[1].alive = True
        self.assertFalse(cell.evaluate(), "Cell alive with two live neighbors.")

        # Set a third neighbor alive, expect it to come alive.
        cell.neighbors[2].alive = True
        self.assertTrue(cell.evaluate(), "Cell dead with three live neighbors.")

        # It should stay alive as long as three neighbors are.
        self.assertTrue(cell.evaluate(), "Cell died with three live neighbors.")

        # It should also stay alive with two neighbors.
        cell.neighbors[0].alive = False
        self.assertTrue(cell.evaluate(), "Cell died with two live neighbors.")

        # It should die if there are too many live cells nearby.
        cell.neighbors[0].alive = True
        cell.neighbors[3].alive = True
        cell.neighbors[4].alive = True
        self.assertFalse(cell.evaluate())

        # It should also die when there are too few live cells nearby.
        cell._evaluate_result = True
        cell.neighbors[0].alive = False
        cell.neighbors[1].alive = False
        cell.neighbors[2].alive = False
        cell.neighbors[3].alive = False
        self.assertFalse(cell.evaluate())


    def test_update(self):
        '''
        After cell.update, cell.alive should match the result
        of cell.evaluate, and a new random color should be generated.
        '''
        cell = self.init_test()

        # This should bring it to life, evaluate but don't update.
        cell.neighbors[0].alive = True
        cell.neighbors[1].alive = True
        cell.neighbors[2].alive = True
        self.assertNotEqual(cell.evaluate(), cell.alive)
        originalColor = cell.color

        # Now update, and they should equal.
        cell.update()
        self.assertEqual(cell._evaluate_result, cell.alive)

        # And the colors should be different.
        self.assertNotEqual(originalColor, cell.color)
        originalColor = cell.color

        # And different once again.
        cell.update()
        self.assertNotEqual(originalColor, cell.color)

    def test_get_random_color(self):
        cell = self.init_test()
        previousColor = (0, 0, 0)
        for iter in range(1000):
            newColor = cell.get_random_color()
            self.assertNotEqual(previousColor, newColor)
            previousColor = newColor
