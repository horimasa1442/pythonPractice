import numpy as np

class CameraPose():
    def __init__(self, intrinsicParameter, extrinsicParameter):
        self.inP = intrinsicParameter
        self.exP = extrinsicParameter

    def getProjectionMatrix(self):
        return self.inP.getA().dot(np.concatenate([self.exP.getR(), self.exP.gett()], axis = 1))

class IntrinsicParameter():
    def __init__(self, fx, fy, cx, cy):
        self.A = np.asarray([[fx, 0, cx],[0, fy, cy],[0, 0, 1]])
    
    def getA(self):
        return self.A

class ExtrinsicParameter():
    def __init__(self, ):
        self.hasR = False
        self.hasQ = False
        self.hast = False
        self.R = np.asarray([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
        self.t = np.asarray([[0],[0],[0]])
        self.Q = np.asarray([1, 0, 0, 0])
    
    def initByMatrix(self, Matrix34):
        self.initByRandt(Matrix34[0:2, 0:2], Matrix34[0:2, 3])

    def initByQandt(self, Qw, Qx, Qy, Qz, t):
        self.Q = np.asarray([Qw, Qx, Qy, Qz])
        self.hasQ = True
        self.t = t
        self.hast = True

    def initByRandt(self, R, t):
        self.R = R
        self.hasR = True
        self.t = t
        self.hast = True

    def initByCamera3D(self, Qw, Qx, Qy, Qz, c):
        self.Q = np.asarray([Qw, Qx, Qy, Qz])
        self.hasQ = True
        self.t = - np.linalg.inv(self.getR()).dot(c)
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

    def getC(self):
        if not self.hast:
            return np.asarray([[0], [0], [0]])
        else:
            return - np.linalg.inv(self.getR()).dot(self.gett())
            
    def calcRfromQ(self):
        if self.hasQ:
            x = self.Q[1]
            y = self.Q[2]
            z = self.Q[3]
            w = self.Q[0]

            self.R = np.asarray([[1-2*y*y-2*z*z, 2*x*y+2*w*z, 2*x*z-2*w*y], \
            [2*x*y-2*w*z, 1-2*x*x-2*z*z, 2*y*z+2*w*x], \
            [2*x*z+2*w*y, 2*y*z-2*w*x, 1-2*x*x-2*y*y]])
            self.R = np.linalg.inv(self.R)
            self.hasR = True
        else:
            print("Q ga nai")
    
    def calcQfromR(self):
        if self.hasR:
            print("miteigi gomene")
        else:
            print("R ga nai")