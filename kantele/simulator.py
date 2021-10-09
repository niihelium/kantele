import numpy as np

from .circuit import Circuit
from .gate import x, h, y
from .operator import Operator


class Simulator:
    NUMPY = "numpy"

    def __init__(self, backend=NUMPY):
        self.position = 0
        self.circuit: Circuit = Circuit()

    def next_operator(self) -> Operator:
        operator = self.circuit.operators[self.position]
        self.position += 1
        return operator

    def calculate(self, circuit: Circuit) -> np.array:
        self.circuit = circuit

        if (len(circuit.operators) == 0):
            return circuit.qubit

        value = circuit.qubit
        gate = []

        while (self.position < len(circuit.operators)):
            operator = self.next_operator()
            if (operator.type == Operator.Type.x):
                gate = x
            elif (operator.type == Operator.Type.y):
                gate = y
            elif (operator.type == Operator.Type.h):
                gate = h
            value = np.dot(value, gate)
        

        return value
