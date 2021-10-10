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

    
    def qubits_product(self, values) -> np.array:
            result = values[0]
            for item in values[1:]:
                result = np.outer(item, result)
            result = np.reshape(result, -1)

            return result

    def calculate(self, circuit: Circuit) -> np.array:
        self.circuit = circuit

        if (len(circuit.operators) == 0):
            return self.return_statevector(circuit.qubits)

        values = circuit.qubits
        gate = []

        while (self.position < len(circuit.operators)):
            operator = self.next_operator()
            if (operator.type == Operator.Type.x):
                gate = x
            elif (operator.type == Operator.Type.y):
                gate = y
            elif (operator.type == Operator.Type.h):
                gate = h

            target_qubit = operator.target_qubit

            values[target_qubit] = np.dot(values[target_qubit], gate)
        

        return self.return_statevector(values)

    def return_statevector(self, qubits):
        if (len(qubits) == 1):
            return qubits[0]
        else:
            return self.qubits_product(qubits)

        
