

class Engine(object):
    """
        Common ancestor of each engine 
        of the simulation

    """

    # Status of nodes
    NORMAL = 0
    INFECTED = 1
    PATCHED = 2
    INVULNERABLE = 3
    UNREACHABLE = 4

    def __init__(self):
        return super(Engine, self).__init__()

