from kantele import provider
from kantele.provider import request_simulator_backend

import pytest
from test_util import prepare_circuit
from numpy.testing import assert_array_equal


sv_000 = [1, 0, 0, 0, 0,0,0,0]
sv_01 = [0, 1, 0, 0]
sv_10 = [0, 0, 1, 0]
sv_11 = [0, 0, 0, 1]

testdata_statevector = [
    (prepare_circuit([0, 0, 0]), sv_000)
    # (prepare_circuit([0, 0, 1]), sv_01),
    # (prepare_circuit([0, 1, 0]), sv_10),
    # (prepare_circuit([0, 1, 1]), sv_11),
]


@pytest.mark.parametrize("circuit, expected", testdata_statevector)
def test_three_qubit_statevector(circuit, expected):
    simulator = request_simulator_backend(provider.NUMPY)
    result = simulator.calculate(circuit)
    assert_array_equal(result, expected)
