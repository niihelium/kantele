import numpy as np

from .operator import Operator

def prepare_matrix(operator: Operator, qubits_count: int) -> np.array:
    before = np.eye(2**operator.target_qubit)
    gate = operator.gate
    after = np.eye(2**(qubits_count - operator.target_qubit -
                       int(operator.gate.shape[0]**0.5)))
    return np.kron(np.kron(before, gate), after)

def prepare_controlled_matrix(operator: Operator, qubits_count: int) -> np.array:
    before = np.eye(2**operator.target_qubit)
    gate = operator.gate
    after = np.eye(2**(qubits_count - operator.target_qubit -
                       int(operator.gate.shape[0]**0.5)))
    return np.kron(np.kron(before, gate), after)
