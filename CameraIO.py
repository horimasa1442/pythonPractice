from Params import *
import numpy as np

def readFromCameraV2(path):
    with open(path) as f:
        flag = True

        while flag:
            line = f.readline().rstrip('\r\n')

            if (not line) or (line[0] == '#'):
                continue

            cameraNum = int(line)
            flag = False