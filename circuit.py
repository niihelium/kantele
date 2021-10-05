from typing import Type
from enum import Enum
import qubit


class Circuit:

    def __init__(self, qubit_count=1):
        self.qubit = qubit.zero
        self.operators = []

    def qubits(self):
        return self.qubit_count

    def set_qubit(self, qubit):
        self.qubit = qubit

    def x(self, target_qubit: int):
        self.operators.append(
            Operator(Operator.Type.x, target_qubit)
        )


class Operator:
    class Type(Enum):
        x = 'x'

    def __init__(self, type: Type, target_qubit: int):
        self.type = type
        self.target_qubit = target_qubit
