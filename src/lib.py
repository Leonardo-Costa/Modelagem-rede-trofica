# Bibliotecas
from scipy import optimize
import random
from matplotlib import pyplot as plt

def GetList():
    S = []
    D = []
    lst = []
    p = []

    S.append(2)
    for i in range(5): S.append(1)
    for i in range(6): D.append(0)
    for i in range(6): lst.append([])
    for i in range(24): p.append(round(random.unifor(0.01, 0.05), 3))

    aux = []
    aux.append(S)
    aux.append(D)
    aux.append(lst)
    aux.append(p)
    return aux


def Simulate(Tmax=10000, DT=0.01, k=1000, theta = 0.05, w=0, g=0):
   
    Lists = GetList()
    
    S   = Lists[0]
    D   = Lists[1]
    lst = Lists[2]
    p   = Lists[3]

    for i in range(6):
        lst[i].clear()

    for i in range(int(Tmax / DT)):

        D[0] = S[0] * (-p[0] * S[1] - p[1] * S[3] - p[2] * S[5] + p[3] - p[3] * (S[0] / k)) * DT
        D[1] = S[1] * (-p[4] * S[2] - p[5] * S[4] + p[6] * S[0] - p[7]) * DT
        D[2] = S[2] * (p[8] * S[1] + p[9] * S[3] - p[10]) * DT
        D[3] = S[3] * (p[11] * S[0] + p[12] * S[5] - p[13] * S[2] - p[14] * S[4] - p[15]) * DT
        D[4] = S[4] * (p[16] * S[1] + p[17] * S[3] + p[18] * S[5] - p[19]) * DT
        D[5] = S[5] * (p[20] * S[0] - p[21] * S[5] - p[22] * S[4] - p[23]) * DT

        for i in range(6): S[i] += D[i]
        for i in range(6): lst[i].append(S[i])
        for i in range(6):
            if S[i] < theta: break

optimize._dual_annealing(Simulate, args=(10000, 0.01, 1000, 0.05, 0, 0), )