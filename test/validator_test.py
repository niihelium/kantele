import numpy as np

import pytest

from kantele.validator import Validator
from kantele.gate import x, y, h

testdata = [
    (x, True),
    (y, True),
    (h, True),
    (np.array([[1, 2],[3, 4]]), False)
]

@pytest.mark.parametrize("gate, expected", testdata)
def test_is_gate_unitary(gate, expected):
    result = Validator.is_gate_unitary(gate)
    assert result == expected