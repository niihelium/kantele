import numpy as np
from kantele import Simulator, Circuit, qubit

circuit = Circuit()
circuit.set_qubit(qubit.zero)
circuit.h(0)
simulator = Simulator(Simulator.NUMPY)
result = simulator.calculate(circuit)
print(result)
