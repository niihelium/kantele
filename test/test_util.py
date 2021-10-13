from kantele import Circuit, qubit


def prepare_circuit_1() -> Circuit:
    circuit = Circuit()
    circuit.set_qubit(0, qubit.one)
    return circuit