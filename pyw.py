
"""
    Main file

    Creates instance of each of the three engines needed
    to run the simulation

"""

from src.ui.ui_engine import UIEngine
from src.simu.simu_engine import SimuEngine
from src.graphic.graphic_engine import GraphicEngine

class Simulation(object):

    def __init__(self):
        ui = UIEngine()
        simu = SimuEngine()
        graphic = GraphicEngine()

    def start(self):
        self.ui.start()

simulation = Simulation()
