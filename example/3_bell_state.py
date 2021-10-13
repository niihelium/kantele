import numpy as np
from kantele import Simulator, Circuit, qubit

circuit = Circuit(2)
circuit.h(0)
circuit.cx(0, 1)
simulator = Simulator(Simulator.NUMPY)
result = simulator.calculate(circuit)
print(result)
