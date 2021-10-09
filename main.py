import numpy as np
from circuit import Circuit
import qubit
from simulator import Simulator

def main():
    circuit = Circuit()
    circuit.set_qubit(qubit.one)
    circuit.y(0)
    simulator = Simulator(Simulator.NUMPY)
    result = simulator.calculate(circuit)
    print(result)


if __name__ == "__main__":
    main()


