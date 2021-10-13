import numpy as np

class Validator():
    @staticmethod
    def is_gate_unitary(gate: np.array) -> bool:
        return False