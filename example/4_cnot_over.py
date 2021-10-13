import numpy as np
from kantele import Simulator, Circuit, qubit

circuit = Circuit(3)
circuit.x(0)
circuit.x(2)
simulator = Simulator(Simulator.NUMPY)
result = simulator.calculate(circuit)
print(result)
