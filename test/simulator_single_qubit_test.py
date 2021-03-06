from kantele import Circuit, provider
from kantele.provider import request_simulator_backend

import pytest
from test_util import prepare_circuit
from numpy.testing import assert_array_equal, assert_array_almost_equal



testdata_x = [
    (Circuit(), [0, 1]),
    (prepare_circuit([1]), [1, 0]),
]


@pytest.mark.parametrize("circuit, expected", testdata_x)
def test_single_qubit_x(circuit, expected):
    circuit.x(0)
    simulator = request_simulator_backend(provider.NUMPY)
    result = simulator.calculate(circuit)
    assert_array_equal(result, expected)


testdata_y = [
    (Circuit(), [0, 1j]),
    (prepare_circuit([1]), [-1j, 0]),
]


@pytest.mark.parametrize("circuit, expected", testdata_y)
def test_single_qubit_y(circuit, expected):
    circuit.y(0)
    simulator = request_simulator_backend(provider.NUMPY)
    result = simulator.calculate(circuit)
    assert_array_equal(result,  expected)


testdata_h = [
    (Circuit(), [0.70710678, 0.70710678]),
    (prepare_circuit([1]), [0.70710678, -0.70710678]),
]


@pytest.mark.parametrize("circuit, expected", testdata_h)
def test_single_qubit_h(circuit, expected):
    circuit.h(0)
    simulator = request_simulator_backend(provider.NUMPY)
    result = simulator.calculate(circuit)
    assert_array_almost_equal(result, expected)
