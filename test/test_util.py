from typing import List
from kantele import Circuit, qubit


def prepare_circuit(qubits: list) -> Circuit:
    circuit = Circuit(len(qubits))
    for position, qubit in enumerate(qubits):
        circuit.set_qubit(position, qubit)
    return circuit


def prepare_circuit(qubits: List[int]) -> Circuit:
    circuit = Circuit(len(qubits))
    for position, qubit in enumerate(qubits):
        circuit.set_qubit(position, [0, 1] if qubit else [1, 0])
    return circuit
