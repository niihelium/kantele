import numpy as np

from kantele import Circuit, provider
from kantele.provider import request_simulator_backend
from kantele.operator import Operator

import pytest
from test_util import prepare_circuit
from numpy.testing import assert_array_equal


z_gate = np.array([[1, 0],
                   [0, -1]])


testdata_x = [
    (Circuit(), [1, 0]),
    (prepare_circuit([1]), [0, -1]),
]


@pytest.mark.parametrize("circuit, expected", testdata_x)
def test_custom_qubit(circuit, expected):
    circuit.apply_operator(0, Operator(None, 0, z_gate))
    simulator = request_simulator_backend(provider.NUMPY)
    result = simulator.calculate(circuit)
    assert_array_equal(result,  expected)
