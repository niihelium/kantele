from enum import Enum

import numpy as np

class Operator:
    class Type(Enum):
        x = 'x',
        cx = 'cx',
        y = 'y',
        h = 'h'

    def __init__(self, type: Type, target_qubit: int, gate: np.array, control_qubit: int = None):
        self.type = type
        self.target_qubit = target_qubit