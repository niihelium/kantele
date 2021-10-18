import numpy as np

from kantele import gate, matrix_builder
from kantele.operator import Operator

import pytest
from numpy.testing import assert_array_equal, assert_array_almost_equal


testdata = [
    (Operator(Operator.Type.x, 0, gate=gate.x), 1, np.array([[0, 1],
                                                             [1, 0]])),
    (Operator(Operator.Type.x, 0, gate=gate.x), 2, np.array([[0, 0, 1, 0],
                                                             [0, 0, 0, 1],
                                                             [1, 0, 0, 0],
                                                             [0, 1, 0, 0], ])),
    (Operator(Operator.Type.x, 1, gate=gate.x), 2, np.array([[0, 1, 0, 0],
                                                             [1, 0, 0, 0],
                                                             [0, 0, 0, 1],
                                                             [0, 0, 1, 0], ]))
]


@pytest.mark.parametrize("operator, qubits_count, expected", testdata)
def test_matrix_builder(operator, qubits_count, expected):
    result = matrix_builder.prepare_matrix(operator, qubits_count)
    assert_array_equal(result, expected)

testdata_controlled = [
    (Operator(Operator.Type.cx, 1, gate=gate.cx, control_qubit=0), 2, np.array([[1, 0, 0, 0],
                                                                                [0, 1, 0, 0],
                                                                                [0, 0, 0, 1],
                                                                                [0, 0, 1, 0], ])),
]

@pytest.mark.parametrize("operator, qubits_count, expected", testdata_controlled)
def test_matrix_builder(operator, qubits_count, expected):
    result = matrix_builder.prepare_controlled_matrix(operator, qubits_count)
    assert_array_equal(result, expected)