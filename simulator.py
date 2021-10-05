import numpy as np
from circuit import Circuit, Operator
from gate import x


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
        value = circuit.qubit
        operator = self.next_operator()
        gate = []
        if (operator.type == Operator.Type.x):
            gate = x

        return np.dot(value, gate)
