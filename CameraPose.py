import numpy as np

class CameraPose():
    def __init__(self, intrinsicParameter, extrinsicParameter):
        self.inP = intrinsicParameter
        self.exP = extrinsicParameter

