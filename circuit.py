from typing import Type
from enum import Enum

from numpy import ndarray
import qubit


class Circuit:


    def __init__(self, qubit_count=1):
        self.qubit: ndarray = qubit.zero
        self.operators = []

    def qubits(self):
        return self.qubit_count

    def set_qubit(self, qubit):
        self.qubit = qubit

    def set_qubit(self, qubit: ndarray):
        self.qubit = qubit

    def x(self, target_qubit: int):
        self.operators.append(
            Operator(Operator.Type.x, target_qubit)
        )

    def h(self, target_qubit: int):
        self.operators.append(
            Operator(Operator.Type.h, target_qubit)
        )


class Operator:
    class Type(Enum):
        x = 'x',
        h = 'h'

    def __init__(self, type: Type, target_qubit: int):
        self.type = type
        self.target_qubit = target_qubit
