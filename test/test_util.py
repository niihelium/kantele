from kantele import Circuit, qubit


def prepare_circuit_1() -> Circuit:
    circuit = Circuit()
    circuit.set_qubit(0, qubit.one)
    return circuit

def prepare_circuit_00() -> Circuit:
    return Circuit(2)

def prepare_circuit_01() -> Circuit:
    circuit = Circuit(2)
    circuit.set_qubit(1, qubit.one)
    return circuit

def prepare_circuit_10() -> Circuit:
    circuit = Circuit(2)
    circuit.set_qubit(0, qubit.one)
    return circuit

def prepare_circuit_11() -> Circuit:
    circuit = Circuit(2)
    circuit.set_qubit(0, qubit.one)
    circuit.set_qubit(1, qubit.one)
    return circuit