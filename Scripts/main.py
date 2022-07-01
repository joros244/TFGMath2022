# ARCHIVO MAIN.PY
# AUTOR: JOSÉ MANUEL ROS RODRIGO
# EMAIL: joros@unirioja.es
# FECHA: 01/07/2022

from os import write
import numpy as np 
import GrafoDirigidoAciclicoPesos as GDAP
import dionysus as d
import gudhi as g
import matplotlib.pyplot as plt
import homology

def muestra_complejo(s,t):
    k0=[l for l in s if len(l)==1]
    k1=[l for l in s if len(l)==2]
    k2=[l for l in s if len(l)==3]
    kn=[l for l in s if len(l)>3]
    k0.sort(reverse=True)
    k1.sort(reverse=True)
    k2.sort(reverse=True)
    kn.sort(reverse=True)
    z=""
    z += "Complejo simplicial de la filtración a "+str(t)+":"+'\n'
    
    z += "0-símplices:"+'\n'  
    elems=""
    for a in k0:
        elems += "{"+str(a)[1:-1]+"},"
    z+="{"+elems[:-1]+"}"+'\n'
    
    z+="1-símplices:"+'\n' 
    elems2=""
    for a in k1:
        elems2 += "{"+str(a)[1:-1]+"},"
    z+="{"+elems2[:-1]+"}"+'\n'
    
    z+="2-símplices:"+'\n'
    elems3=""
    for a in k2:
        elems3 += "{"+str(a)[1:-1]+"},"
    z+="{"+elems3[:-1]+"}"+'\n'
    
    z+="n-símplices:"+'\n'
    elems4=""
    for a in kn:
        elems4 += "{"+str(a)[1:-1]+"},"
    z+="{"+elems4[:-1]+"}"+'\n'
    
    return z

'''Matriz de ejemplo'''

prueba=np.array([[1,0,0,0,0,0,0,0,0,0,0,0],
                 [0,1,0,0,0,0,0,0,0,0,0,0],
                 [0.57,0,1,0,0,0,0,0,0,0,0,0],
                 [0.43,0.59,0,1,0,0,0,0,0,0,0,0],
                 [0,0.41,0,0,1,0,0,0,0,0,0,0],
                 [0,0,0.4,0,0,1,0,0,0,0,0,0],
                 [0,0,0.6,0.58,0,0,1,0,0,0,0,0],
                 [0,0,0,0.42,0.56,0,0,1,0,0,0,0],
                 [0,0,0,0,0.44,0,0,0,1,0,0,0],
                 [0,0,0,0,0,1,0.5,0,0,1,0,0],
                 [0,0,0,0,0,0,0.5,0.55,0,0,1,0],
                 [0,0,0,0,0,0,0,0.45,1,0,0,1]])


'''Construcción del grafo asociado a la matriz con la estructura GDAP'''

H=GDAP.GDA_con_pesos(prueba)

r=[1.0,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.0]

###############################################################################
# CÁLCULO DE LOS DIAGRAMAS                                                    #
#fil = d.Filtration()
#
#for i,t in enumerate(r):
#    for e in H.get_simplex_global(t):
#        fil.add(d.Simplex(e,i))
#  
#fil.sort()
#
#m = d.homology_persistence(fil)
#dgms = d.init_diagrams(m,fil)
#
#
#h0=[]
#h1=[]
#h2=[]
#
#for i, dgm in enumerate(dgms):
#    for p in dgm:
#        birth = p.birth
#        death= p.death
#        if i==0:
#            h0.append([i,[birth,death]])
#        elif i==1:
#            h1.append([i,[birth,death]])
#        elif i==2:
#            h2.append([i,[birth,death]])
#l= h0 + h1 + h2
#l.sort(reverse=True)
#
#
#ax1= plt.axes()
#ax1.use_sticky_edges = False
#ax1.set_aspect('auto')
#g.plot_persistence_diagram(l, legend=True, axes=ax1)
#plt.title('Diagrama de persistencia',fontdict={'fontsize':16,'fontweight':'bold','color': 'black','verticalalignment':'baseline','horizontalalignment':'center'})
#plt.xlabel('Nacimiento',fontdict={'fontsize':16,'fontweight':'bold','color': 'black','horizontalalignment':'center'})
#plt.ylabel('Muerte',fontdict={'fontsize':16,'fontweight':'bold','color': 'black','horizontalalignment':'center'})
#plt.show()
#plt.savefig('Barras_local')

###############################################################################
# GENRALIZACIÓN DE LOS ARCHIVOS CON LAS LISTAS DE SÍMPLICES                   #

with open('simpEjHOMGLOBAL.txt', 'w') as f:
    f.write("########################################################################"+'\n')
    f.write("Listado de símplices asociado al ejemplo de distribución homogénea del capítulo 3. Versión global."+'\n')
    f.write("Autor: José Manuel Ros Rodrigo."+'\n')
    f.write("Email: joros@unirioja.es."+'\n')
    f.write("########################################################################"+'\n')
    for t in r:
        f.write('\n')
        f.write(str(muestra_complejo(H.get_simplex_global(t),t)))

###############################################################################
# VISUALIZACIÓN POR PANTALLA DE LOS SÍMPLICES                                 #

#for t in r:
#    print("VERSIÓN GLOBAL")
#    print(muestra_complejo(H.get_simplex_global(t),t))
#    print("VERSIÓN DEL AUTOR")
#    print(muestra_complejo(simp_tot,t))

#print("DIFERENCIA SIMÉTRICA ENTRE GLOBAL Y LOCAL (G ^ L)")
#T=[tuple(j) for j in H.get_simplex_global(t)]
#R=[tuple(j) for j in H.get_simplex_local(t)]
#U=set(T)^set(R)
#if (len(U)==0):
#    print("{}"+'\n')
#else:    
#    print(str(set(T) ^ set(R))+'\n')

#print("DIFERENCIA SIMÉTRICA ENTRE AUTOR Y LOCAL (A ^ L)")
#T=[tuple(j) for j in simp_tot]
#R=[tuple(j) for j in H.get_simplex_local(t)]
#U=set(T)^set(R)
#if (len(U)==0):
#    print("{}"+'\n')
#else:    
#    print(str(set(T) ^ set(R))+'\n')
