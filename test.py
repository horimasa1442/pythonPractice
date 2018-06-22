'''
from Params import *
import numpy as np


para = ExtrinsicParameter()

para.initByQandt(0.958221, 0.024887, 0.264127, -0.106916, np.asarray([[-4.17062], [1.35133], [3.75977]]))
print(para.gett())
print(para.getC())
print(para.getR())
print(para.getQ())

print(-np.linalg.inv(para.getR()).dot(para.gett()))

print("-----------------------------")

inP = IntrinsicParameter(1673.37, 1673.37, 600.5, 802.5)
print(inP.getA())

ppp = CameraPose(inP, para)

print(ppp.getProjectionMatrix())

'''

from CameraIO import *

readFromCameraV2("E:\data\dataset\yorkCOLMAP\camera_v2.txt")