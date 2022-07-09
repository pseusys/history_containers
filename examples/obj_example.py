from history_containers import HistoryObjectMixin


class Mirror(HistoryObjectMixin):
    transparent = False
    color = 'silver'
    reflects = ['humans', 'trolls', 'elves']
    skips = ['vampires', 'ghosts']
    material = {
        'surface': 'glass',
        'components': ['silver', 'sand'],
        'fragility': 9
    }

    def __init__(self, watch_self: bool = False):
        super(Mirror, self).__init__(watch_self)


if __name__ == '__main__':
    print("Let's create a simple object extending HistoryObjectMixin - it should keep track of his fields (dicts and lists) history, but not oh his own!")
    obj = Mirror()
    print(obj.print(), end='\n\n')

    print("Let's assume this is a bulletproof glass, its fragility should be less - change of nested dict value should be visible in history!")
    obj.material['fragility'] = 7
    print(obj.print(), end='\n\n')

    print("Let's make the mirror transparent, like in detective films - change of object value won't be visible in history (because of 'watch_self' parameter)!")
    obj.transparent = True
    print(obj.print(), end='\n\n')

    print("Let's make object self-changes-aware - from now on it should keep track of its own attribute changes!")
    obj.watch_self = True
    print("Just after that let's change the mirror color - old and new values should remain in history!")
    obj.color = 'black'
    print(obj.print(), end='\n\n')

    print("The way to track object fields deletion is also defined, however it can't be used without additional code since it's impossible to delete object field in Python!")
    # del obj.reflects  # Throws AttributeError('reflects') because of Python.
    # print(obj.print(), end='\n\n')
