import numpy as np

from .circuit import Circuit
from .gate import x, h, y
from .operator import Operator
from kantele import circuit


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
            result = np.kron(result, item)

        return result

    def calculate(self, circuit: Circuit) -> np.array:
        """
        Perform statevector calculation for given circuit

        Args:
            circuit: Constructed circuit.
        """
        self.circuit = circuit
        self.statevector = self._qubits_product(self.circuit.qubits)

        if (len(circuit.operators) == 0):
            return self.statevector

        while (self.position < len(circuit.operators)):
            operator = self._next_operator()
            matrix = self._prepare_matrix(operator, len(self.circuit.qubits))

            self.statevector = np.matmul(matrix, self.statevector)

        return self.statevector

    def _prepare_matrix(self, operator: Operator, qubits_count: int) -> np.array:
        before = np.eye(2**operator.target_qubit)
        gate = operator.gate
        after = np.eye(2**(qubits_count - operator.target_qubit - int(operator.gate.shape[0]**0.5)) )
        return np.kron(np.kron(before, gate), after)

    def _return_statevector(self, qubits):
        if (len(qubits) == 1):
            return qubits[0]
        else:
            return self._qubits_product(qubits)
