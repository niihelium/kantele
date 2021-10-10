import numpy as np
from kantele import Simulator, Circuit, qubit

circuit = Circuit(3)
circuit.h(1)
simulator = Simulator(Simulator.NUMPY)
result = simulator.calculate(circuit)
print(result)
