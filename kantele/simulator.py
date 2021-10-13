import numpy as np

from .circuit import Circuit
from .gate import x, h, y
from .operator import Operator


class Simulator:
    NUMPY = "numpy"

    def __init__(self, backend=NUMPY):
        self.position = 0
        self.circuit: Circuit = Circuit()

    def _next_operator(self) -> Operator:
        """
        Return next operator from operators list and advance position.
        """
        operator = self.circuit.operators[self.position]
        self.position += 1
        return operator

    
    def _qubits_product(self, values) -> np.array:
        """
        Return Kronecker multiplication of variable length qubits list.

        Args:
            values: List of qubits.
        """
        result = values[0]
        for item in values[1:]:
            result = np.kron(item, result)
            
        result = np.reshape(result, -1)

        return result

    def calculate(self, circuit: Circuit) -> np.array:
        """
        Perform statevector calculation for given circuit

        Args:
            circuit: Constructed circuit.
        """
        self.circuit = circuit

        if (len(circuit.operators) == 0):
            return self.return_statevector(circuit.qubits)

        values = circuit.qubits
        gate = []

        while (self.position < len(circuit.operators)):
            operator = self._next_operator()
            gate = operator.gate

            target_qubit = operator.target_qubit

            values[target_qubit] = np.dot(gate, values[target_qubit])
        

        return self._return_statevector(values)

    def _return_statevector(self, qubits):
        if (len(qubits) == 1):
            return qubits[0]
        else:
            return self.qubits_product(qubits)

        
