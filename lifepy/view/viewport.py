'''
Defines a rectangular region to be devoted to a specific "view". This class
should not be used directly, only inherited from.
'''
__author__ = 'cody.owens@gmail.com'

class ViewPort(object):
    def __init__(self, viewContext):
        self.context = viewContext

    def on_render(self, deltaTime):
        raise NotImplementedError()