from enum import Enum
from _pytest.compat import is_generator

import numpy as np

from .validator import Validator

class Operator:
    class Type(Enum):
        x = 'x',
        cx = 'cx',
        y = 'y',
        h = 'h'

    def __init__(self, type: Type, target_qubit: int, gate: np.array, control_qubit: int = None):
        self.type = type
        self.target_qubit = target_qubit
        if (not Validator.is_gate_unitary(gate)): 
            raise ValueError("Custom operator should be unitary")
        self.gate = gate


