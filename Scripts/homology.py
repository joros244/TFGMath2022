import itertools
import numpy as np
import copy

def comb(seq):
    res=[]
    for L in range(1,len(seq)+1):
        for sub in itertools.combinations(seq,L):
            res.append(list(sub))
    return res

def get_simplex(matriz,puntos,t):
    rel = 1.0
    n = len(matriz)
    result = []
    origen = puntos[0]
    for destino in puntos:
        rel = rel*matriz[origen][destino]
        origen = destino
    if rel >= t:
        for e in comb(puntos):
            result.append(e)
        ult = puntos[-1]
        for i in range (n):
            if matriz[ult][i] > 0 and i != ult:
                puntos2 = copy.deepcopy(puntos)
                puntos2.append(i)
                k = get_simplex(matriz,puntos2,t)
                for e in k:
                    for ee in comb(e):
                        result.append(ee)
    return list(map(list,set(map(tuple,result))))


prueba=np.array([[1,0,0,0,0,0,0,0,0,0,0],
                [0.3,1,0,0,0,0,0,0,0,0,0],
                [0.1,0,1,0,0,0,0,0,0,0,0],
                [0.6,0,0,1,0,0,0,0,0,0,0],
                [0,0.2,0,0,1,0,0,0,0,0,0],
                [0,0.8,0.2,0,0,1,0,0,0,0,0],
                [0,0,0.8,0.7,0,0,1,0,0,0,0],
                [0,0,0,0.3,0,0,0,1,0,0,0],
                [0,0,0,0,1,0.2,0,0,1,0,0],
                [0,0,0,0,0,0.8,0.7,0,0,1,0],
                [0,0,0,0,0,0,0.3,1,0,0,1]])
k0=[]
k1=[]
k2=[]
simp_tot=[]
for punto in range(0,len(prueba)):
    simp=get_simplex(prueba,[punto],0.2)
    simp_tot.extend(simp)
#k0.sort(reverse=True)
#k1.sort(reverse=True)
#k2.sort(reverse=True)
#print(k0)            
#print(k1)            
#print(k2)            
#print([e for e in simp_tot if len(e)>2])
#print(simp_tot.count([0]))

