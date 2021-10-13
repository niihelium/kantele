from numpy.testing import assert_array_equal, assert_array_almost_equal

from kantele import Simulator, Circuit, qubit

import pytest
from test_util import prepare_circuit

sv_00 = [1, 0, 0, 0]
sv_01 = [0, 1, 0, 0]
sv_10 = [0, 0, 1, 0]
sv_11 = [0, 0, 0, 1]

testdata_statevector = [
    (prepare_circuit([0, 0]), sv_00),
    (prepare_circuit([0, 1]), sv_01),
    (prepare_circuit([1, 0]), sv_10),
    (prepare_circuit([1, 1]), sv_11),
]


@pytest.mark.parametrize("circuit, expected", testdata_statevector)
def test_two_qubit_statevector(circuit, expected):
    simulator = Simulator(Simulator.NUMPY)
    result = simulator.calculate(circuit)
    assert_array_equal(result, expected)


testdata_x = [
    (prepare_circuit([0, 0]), 0, sv_10),
    (prepare_circuit([0, 0]), 1, sv_01),
    (prepare_circuit([0, 1]), 0, sv_11),
    (prepare_circuit([0, 1]), 1, sv_00),
    (prepare_circuit([1, 0]), 0, sv_00),
    (prepare_circuit([1, 0]), 1, sv_11),
    (prepare_circuit([1, 1]), 0, sv_01),
    (prepare_circuit([1, 1]), 1, sv_10),
]


@pytest.mark.parametrize("circuit, qubit, expected", testdata_x)
def test_two_qubit_x(circuit, qubit, expected):
    circuit.x(qubit)
    simulator = Simulator(Simulator.NUMPY)
    result = simulator.calculate(circuit)
    assert_array_equal(result, expected)
