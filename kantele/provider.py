from kantele.simulator import Simulator, NumpySimulator


NUMPY = "numpy"

def request_simulator_backend(type) -> Simulator:
    if (type == NUMPY):
        return NumpySimulator()