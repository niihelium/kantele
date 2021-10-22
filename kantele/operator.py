from enum import Enum
from _pytest.compat import is_generator

import numpy as np

from kantele import gate

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


class Xgate(Operator):
    def __init__(self, target_qubit: int):
        super().__init__(Operator.Type.x, target_qubit, gate.x, None)


class Hgate(Operator):
    def __init__(self, target_qubit: int):
        super().__init__(Operator.Type.h, target_qubit, gate.h, None)


class Ygate(Operator):
    def __init__(self, target_qubit: int):
        super().__init__(Operator.Type.y, target_qubit, gate.y, None)


class CXgate(Operator):
    def __init__(self, control_qubit, target_qubit):
        super().__init__(Operator.Type.cx, target_qubit, gate.cx, control_qubit)
