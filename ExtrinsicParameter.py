import numpy as np

class ExtrinsicParameter():
    def __init__(self, ):
        self.hasR = False
        self.hasQ = False
        self.hast = False
    
    def initByMatrix(self, Matrix34):
        self.initByRandt(Matrix34[0:2, 0:2], Matrix34[0:2, 3])

    def initByQandt(self, Qx, Qy, Qz, Qw, t):
        self.Q = np.asarray([Qx, Qy, Qz, Qw])
        self.hasQ = True
        self.t = t
        self.hast = True

    def initByRandt(self, R, t):
        self.R = R
        self.hasR = True
        self.t = t
        self.hast = True

    def getR(self):
        if not self.hasR:
            self.calcRfromQ()
        return self.R
    
    def gett(self):
        if self.hast:
            return self.t
        else:
            print("t ga nai")
            return np.asarray([[0], [0], [0]])

    def getQ(self):
        if not self.hasQ:
            self.calcQfromR
        return self.Q
            
    def calcRfromQ(self):
        if self.hasQ:
            x = self.Q[0]
            y = self.Q[1]
            z = self.Q[2]
            w = self.Q[3]

            self.R = np.asarray([[1-2*y*y-2*z*z, 2*x*y+2*w*z, 2*x*z-2*w*y], \
            [2*x*y-2*w*z, 1-2*x*x-2*z*z, 2*y*z+2*w*x], \
            [2*x*z+2*w*y, 2*y*z-2*w*x, 1-2*x*x-2*y*y]]);
            self.hasR = True
        else:
            print("Q ga nai")
    
    def calcQfromR(self):
        if self.hasR:
            print("miteigi gomene")
        else:
            print("R ga nai")