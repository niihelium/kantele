from numpy.testing import assert_array_equal, assert_array_almost_equal

from kantele import Simulator, Circuit, qubit

def prepare_circuit_1() -> Circuit:
    circuit = Circuit()
    circuit.set_qubit(0, qubit.one)
    return circuit

def test_single_qubit_x_0():
    circuit = Circuit()
    circuit.x(0)
    simulator = Simulator(Simulator.NUMPY)
    result = simulator.calculate(circuit)
    assert_array_equal(result,  [0, 1])

def test_single_qubit_x_1():
    circuit = prepare_circuit_1()
    circuit.x(0)
    simulator = Simulator(Simulator.NUMPY)
    result = simulator.calculate(circuit)
    assert_array_equal(result,  [1, 0])

def test_single_qubit_y_0():
    circuit = Circuit()
    circuit.y(0)
    simulator = Simulator(Simulator.NUMPY)
    result = simulator.calculate(circuit)
    assert_array_equal(result,  [0, 1j])

def test_single_qubit_y_1():
    circuit = prepare_circuit_1()
    circuit.y(0)
    simulator = Simulator(Simulator.NUMPY)
    result = simulator.calculate(circuit)
    assert_array_equal(result,  [-1j, 0])

def test_single_qubit_h_0():
    circuit = Circuit()
    circuit.h(0)
    simulator = Simulator(Simulator.NUMPY)
    result = simulator.calculate(circuit)
    assert_array_almost_equal(result,  [0.70710678, 0.70710678])

def test_single_qubit_h_1():
    circuit = prepare_circuit_1()
    circuit.h(0)
    simulator = Simulator(Simulator.NUMPY)
    result = simulator.calculate(circuit)
    assert_array_almost_equal(result,  [0.70710678, -0.70710678])