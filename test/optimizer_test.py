import numpy as np

from kantele import Circuit, Optimizer, circuit, optimizer
from kantele.operator import Operator

from numpy.testing import assert_array_equal


def test_optimirser_trivial():

    e_circuit = Circuit()
    e_circuit.set_qubit(0, [1, 0])

    circuit = Circuit()
    circuit.set_qubit(0, [1, 0])
    circuit.x(0)
    circuit.x(0)

    optimizer = Optimizer()
    o_circuit = optimizer.optimize(circuit)
    print(circuit)
    assert_array_equal(e_circuit.operators, o_circuit.operators)
