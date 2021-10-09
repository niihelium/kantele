from enum import Enum

class Operator:
    class Type(Enum):
        x = 'x',
        y = 'y',
        h = 'h'

    def __init__(self, type: Type, target_qubit: int):
        self.type = type
        self.target_qubit = target_qubit
