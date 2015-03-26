
from src.engine import Engine

class SimuEngine(Engine):
    """
        Engine responsible for the computation
        of the simulation

    """


    def __init__(self, graphic_engine):
        # Number of bytes encoding a machine IP address
        # (from that we deduce the total number of machines)
        self.L = 3
        # Number of machines reachable on the network
        # (by default, all possible IP address)
        self.n = 255**self.L
        # Number of machines vulnerable to attack
        self.k = 255**self.L
        # Time from the beginning of the simulation
        self.t = 0
        # Network of machines (all possible IP addr)
        self.network = [self.NORMAL] * (255**self.L)
        # Graphic Engine to display the simulation
        self.graphic = graphic_engine
        

    def generate_network(self):
        # Setting 255**L - n machines as unreachable
        nb = 0
        while nb < (255**self.L - self.n):
            ip = randint(0, 255**self.L)
            if self.network[ip] == cls.NORMAL:
                self.network[ip] = UNREACHABLE
                nb += 1
        # Setting n - k machines as invulnerable
        nb = 0
        while nb < (self.n - self.k):
            ip = randint(0, 255**self.L)
            if self.network[ip] == NORMAL:
                self.network[ip] = INVULNERABLE
                nb += 1


    def launch(self, n, k):
        self.n = n
        self.k = k
        # Generating the network
        self.generate_network()
        # Creation of the view window
        self.graphic.launch(self.network)
