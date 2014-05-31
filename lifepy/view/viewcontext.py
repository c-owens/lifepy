__author__ = 'cody.owens@gmail.com'

class ViewContext(object):
    def __init__(self, surface, width, height, x, y):
        self.surface = surface
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.offset = (x, y)
