import numpy as np

class Validator():
    @staticmethod
    def is_gate_unitary(gate: np.array) -> bool:
        return np.allclose(np.eye(gate.shape[0]), np.matrix(gate).getH() * gate)