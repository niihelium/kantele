import numpy as np
from kantele import Simulator, Circuit, qubit

circuit = Circuit(3)
circuit.y(1)
circuit.h(1)
circuit.h(2)
simulator = Simulator(Simulator.NUMPY)
result = simulator.calculate(circuit)
print(result)
