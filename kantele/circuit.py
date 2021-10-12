from numpy import ndarray

from kantele import gate, qubit
from .operator import Operator


class Circuit:

    def __init__(self, qubit_count: int = 1):
        self.qubits = [qubit.zero] * qubit_count
        self.operators = []

    def qubits(self):
        return self.qubit_count

    def set_qubit(self, qubit_index, qubit):
        self.qubits[qubit_index] = qubit

    def set_qubit(self, qubit_index, qubit: ndarray):
        self.qubits[qubit_index] = qubit

    def x(self, target_qubit: int):
        self.operators.append(
            Operator(Operator.Type.x, target_qubit, gate=gate.x)
        )

    def cx(self, control_qubit: int, target_qubit: int):
        self.operators.append(
            Operator(Operator.Type.cx,
                     control_qubit=control_qubit,
                     target_qubit=target_qubit,
                     gate=gate.cx)
        )

    def h(self, target_qubit: int):
        self.operators.append(
            Operator(Operator.Type.h, target_qubit, gate=gate.h)
        )

    def y(self, target_qubit: int):
        self.operators.append(
            Operator(Operator.Type.y, target_qubit, gate=gate.y)
        )
