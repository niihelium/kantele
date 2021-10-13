import numpy as np

from kantele.validator import Validator

def test_is_gate_unitary():
    result = Validator.is_gate_unitary(np.zeros(2))
    assert result == False