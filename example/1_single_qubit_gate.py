import numpy as np
from kantele import Simulator, Circuit, qubit

circuit = Circuit()
circuit.y(0)
simulator = Simulator(Simulator.NUMPY)
result = simulator.calculate(circuit)
print(result)
