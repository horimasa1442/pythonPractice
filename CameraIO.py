from Params import *
import numpy as np
from HelperFunc import *

def readFromCameraV2(path):
    with open(path) as f:
        flag = True

        while flag:
            line = f.readline().rstrip('\r\n')

            if (not line) or (line[0] == '#'):
                continue

            cameraNum = int(line)
            flag = False

        print(cameraNum)

        line = f.readline().rstrip('\r\n')

        for i in range(cameraNum):
            fName = f.readline().rstrip('\r\n')
            line = f.readline().rstrip('\r\n')

            flength = str2floatList(f.readline.rstrip('\r\n'), ' ')
            pPoint = str2floatList(f.readline.rstrip('\r\n'), ' ')
            trans = np.asarray(str2floatList(f.readline.rstrip('\r\n'), ' '))
            