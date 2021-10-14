from kantele import Circuit, provider
from kantele.provider import request_simulator_backend

circuit = Circuit(3)
circuit.h(2)
simulator = request_simulator_backend(provider.NUMPY)
result = simulator.calculate(circuit)
print(result)
