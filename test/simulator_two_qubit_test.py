from numpy.testing import assert_array_equal, assert_array_almost_equal

from kantele import Simulator, Circuit

import pytest
from test_util import prepare_circuit_1, prepare_circuit_00, prepare_circuit_01, prepare_circuit_10, prepare_circuit_11

sv_00 = [1, 0, 0, 0]
sv_01 = [0, 1, 0, 0]
sv_10 = [0, 0, 1, 0]
sv_11 = [0, 0, 0, 1]

testdata_statevector = [
    (prepare_circuit_00(), sv_00),
    (prepare_circuit_01(), sv_01),
    (prepare_circuit_10(), sv_10),
    (prepare_circuit_11(), sv_11),
]
@pytest.mark.parametrize("circuit, expected", testdata_statevector)
def test_two_qubit_statevector(circuit, expected):
    simulator = Simulator(Simulator.NUMPY)
    result = simulator.calculate(circuit)
    assert_array_equal(result, expected)