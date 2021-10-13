from numpy.testing import assert_array_equal
import numpy as np

from kantele import Simulator, Circuit, qubit
from kantele.operator import Operator

z_gate = np.array([[1, 0],
                   [0, -1]])


def prepare_circuit_1() -> Circuit:
    circuit = Circuit()
    circuit.set_qubit(0, qubit.one)
    return circuit


def test_single_qubit_x_0():
    circuit = Circuit()
    circuit.apply_operator(0, Operator(None, 0, z_gate))
    simulator = Simulator(Simulator.NUMPY)
    result = simulator.calculate(circuit)
    assert_array_equal(result,  [1, 0])


def test_single_qubit_x_1():
    circuit = prepare_circuit_1()
    circuit.apply_operator(0, Operator(None, 0, z_gate))
    simulator = Simulator(Simulator.NUMPY)
    result = simulator.calculate(circuit)
    assert_array_equal(result,  [0, -1])
