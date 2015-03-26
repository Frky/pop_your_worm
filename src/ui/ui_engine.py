
from src.engine import Engine

class UIEngine(Engine):
    """
        Engine responsible for the display of 
        control panel and for the fetching of
        user inputs

    """

    def __init__(self, simu_launch):
        self.simu_launch = simu_launch


    def start(self):
        # Test purpose
        self.simu_launch(100, 10)
