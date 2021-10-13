import numpy as np

class Validator():
    @staticmethod
    def is_gate_unitary(gate: np.array) -> bool:
        """
        Check where provided gate matrix is unitary.

        Args:
            gate: Gate matrix to check.
        """
        return np.allclose(np.eye(gate.shape[0]), np.matrix(gate).getH() * gate)