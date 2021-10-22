from numpy import ndarray

from kantele import gate, qubit
from .operator import CXgate, Hgate, Operator, Xgate, Ygate


class Circuit:
    """
    Create new circut
    """

    def __init__(self, qubits_count: int = 1):
        self.qubits = [qubit.zero] * qubits_count
        self.operators = []

    def get_qubits(self):
        return self.qubits

    def set_qubit(self, qubit_index, qubit: ndarray):
        """
        Set qubit state.

        Args:
            qubit_index: The qubit which value should be changed.
            qubit: Value to set.
        """

        self.qubits[qubit_index] = qubit

    def x(self, target_qubit: int):
        """
        Apply NOT gate on qubit.

        Args:
            target_qubit: The qubit to apply the gate to.
        """
        self.operators.append(Xgate(target_qubit))

    def cx(self, control_qubit: int, target_qubit: int, ):
        """
        Apply CNOT gate on qubit.

        Args:
            target_qubit: The qubit to apply the gate to.
            control_qubit: The qubit used as control.
        """
        self.operators.append(CXgate(control_qubit, target_qubit))

    def h(self, target_qubit: int):
        """
        Apply HADAMARD gate on qubit.

        Args:
            target_qubit: The qubit to apply the gate to.
        """
        self.operators.append(Hgate(target_qubit))

    def y(self, target_qubit: int):
        """
        Apply Y gate on qubit.

        Args:
            target_qubit: The qubit to apply the gate to.
        """
        self.operators.append(Ygate(target_qubit))

    def apply_operator(self, target_qubit: int, operator: Operator):
        """
        Apply custom operatoron qubit.

        Args:
            target_qubit: The qubit to apply the gate to.
            operator: user-defined object of Operator class.

        """
        self.operators.append(operator)
