import numpy as np

from kantele.optimizer import Optimizer

from .circuit import Circuit
from .gate import x, h, y
from .operator import Operator
from . import matrix_builder


class Simulator:
    def __init__(self):
        self.position = 0
        self.circuit: Circuit = Circuit()

    def _next_operator(self) -> Operator:
        """
        Return next operator from operators list and advance position.
        """
        operator = self.circuit.operators[self.position]
        self.position += 1
        return operator


class NumpySimulator(Simulator):
    def __init__(self):
        Simulator.__init__(self)

    def _qubits_product(self, values) -> np.array:
        """
        Return Kronecker multiplication of variable length qubits list.

        Args:
            values: List of qubits.
        """
        result = values[0]
        for item in values[1:]:
            result = np.kron(result, item)

        return result

    def calculate(self, circuit: Circuit) -> np.array:
        """
        Perform statevector calculation for given circuit

        Args:
            circuit: Constructed circuit.
        """
        self.optimizer = Optimizer()
        self.circuit = self.optimizer.optimize(circuit)
        self.statevector = self._qubits_product(self.circuit.qubits)

        if (len(circuit.operators) == 0):
            return self.statevector

        while (self.position < len(circuit.operators)):
            operator = self._next_operator()
            matrix = matrix_builder.prepare_matrix(operator, len(self.circuit.qubits))

            self.statevector = np.matmul(matrix, self.statevector)

        return self.statevector



    def _return_statevector(self, qubits):
        if (len(qubits) == 1):
            return qubits[0]
        else:
            return self._qubits_product(qubits)
