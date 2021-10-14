from kantele import Circuit, provider
from kantele.provider import request_simulator_backend

circuit = Circuit(2)
circuit.h(0)
circuit.cx(0, 1)
simulator = request_simulator_backend(provider.NUMPY)
result = simulator.calculate(circuit)
print(result)
