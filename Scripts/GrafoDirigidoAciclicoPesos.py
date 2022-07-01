import GrafoDirigidoAciclico as GDA
import itertools as it
from typing import List
import copy

class GDA_con_pesos():
    
    ''' Un GDAP es un GDA con una matriz asociada. La matriz determina las 
    aristas y los vértices del GDA asociado. '''
    def __init__(self, M):
        self.G = GDA.Grafo_dirigido_aciclico(len(M))
        self.M = M
        for i in range(0,len(self.M)):
            for j in range(i):
                if( self.M[i][j] > 0 ):
                    self.G.crea_arista(i,j)
    
    ''' Devuelve el GDAP clausura transitiva de this. Es decir, el grafo 
    asociado es el grafo clausura transitiva y la matriz es completada por 
    transitividad '''
    def clausura_transitiva(self):
        T = copy.deepcopy(self)
        T.G = T.G.clausura_transitiva()
        T.__completa_pesos()
        return T
    
    ''' Completa la matriz del GDAP por transitividad + máximo '''
    def __completa_pesos(self):
        for i in range(len(self.M)):
            for j in self.G.adj[i]:
                if(self.M[i][j]==0):
                    p=[]
                    self.busca_pesos(i,j,p)
                    if(len(p)>0):
                        m = max([v[0] for v in p])
                        self.M[i][j]=m 
    
    ''' Devuelve el GDAP filtrado por r '''
    def filtracion(self,r):
        F=copy.deepcopy(self.M)
        for i in range(len(self.M)):
            for j in range(i):
                if(self.M[i][j]<r):
                    F[i][j]=0
        return GDA_con_pesos(F)
 
    ''' Devuelve un lista con el complejo simplicial asociado al GDAP. 
    V.LOCAL '''
    def get_simplex_local(self, t : float)->List[List[int]]:
        simplices=self.__calcula_simplices(t)
        
        simplices.extend([[i] for i in range(len(self.M))])
        
        '''Hemos calculado símplices "maximales", nos faltan sus subsímplices'''
        for s in simplices:
            for L in range(2,len(s)+1):
                for sub in it.combinations(s,L):
                    if(list(sub) not in simplices):
                       simplices.append(list(sub))
        return simplices
    
    ''' Devuelve un lista con el complejo simplicial asociado al GDAP. 
    V.GLOBAL '''
    def get_simplex_global(self, t : float)->List[List[int]]:
        simplices=self.__calcula_simplices_global(t)
        
        ''' En este caso hay que añadir los vértices '''
        simplices.extend([[i] for i in range(len(self.M))])
        
        ''' Ahora añadimos los subsímplices de los calculados '''
        for s in simplices:
            for L in range(3,len(s)+1):
                for sub in it.combinations(s,L):
                    if(list(sub) not in simplices):
                       simplices.append(list(sub))
        
        ''' Limpiamos aquellos símplices con aristas irreales '''
        tr=[s for s in simplices if len(s)>2]
        for e in tr:
            if(any([list(sub) not in simplices for sub in 
                it.combinations(e,len(e)-1)])):
                simplices.remove(e)

        return simplices

    ''' Almacena en p una lista de tuplas donde el primer argumento es el 
    posible peso entre origen(o) y destino(d); y el segundo argumento es el 
    camino que produce dicho peso. '''
    def busca_pesos(self, o, d, p=[], q=1, c=[]):
        ''' BÚSQUEDA EN PROFUNDIDAD '''
        if(o==d):
            c.append(o)
            p.append((q.__round__(4),c))
            q=1
            c=[]
        else:   
            for j in range(d,o):
                if(self.M[o][j]!=0):
                    ''' NOTA: Podríamos optimizarlo para que si q<t pase al 
                    siguente vértice. SÓLO VÁLIDO PARA V.LOCAL'''
                    self.busca_pesos(j,d,p,q*self.M[o][j],c+[o])

    ''' Devuelve una lista de los símplices maximales de cada vértice si al 
    menos uno de ellos pasa el filtro t. Recorre la lista de vértices 
    adyacentes a uno dado y en caso de que no haya adyacencia directa, calcula 
    los caminos indirectos y los añade. Si la adyacencia directa pasa el 
    filtro, la añade.'''
    def __calcula_simplices_global(self,t)->List[List[int]]:
        simp=[]
        ''' Necesario para recorrer los adyacentes. OPTIMIZACIÓN '''
        P=self.filtracion(t)
        T=P.clausura_transitiva()
        for i in range(len(self.M)):
            for j in T.G.adj[i]:
                if(self.M[i][j]==0):
                    p=[]
                    self.busca_pesos(i,j,p)
                    if(len(p)>0):
                        m=max([v[0] for v in p])
                        if(m>=t):
                            l = [k[1] for k in p]
                            simp.extend(l)
                            simp.append([i,j])
                elif (self.M[i][j]>=t):
                    simp.append([i,j])
        return simp

    ''' Devuelve una lista de los símplices maximales de cada vértice que pasan
    el filtro t. Lo que hace es recorrer la lista de vértices adyacentes y en 
    caso de que no haya adyacencia directa, calcula los caminos indirectos.'''
    def __calcula_simplices(self,t)->List[List[int]]:
        simp=[]
        ''' Necesario para recorrer los adyacentes. OPTIMIZACIÓN '''
        P=self.filtracion(t)
        T=P.clausura_transitiva()
        for i in range(len(self.M)):
            for j in T.G.adj[i]:
                if(self.M[i][j]==0):
                    p=[]
                    self.busca_pesos(i,j,p)
                    if(len(p)>0):
                        l = [k[1] for k in p if k[0]>=t]
                        simp.extend(l)
                elif (self.M[i][j]>=t):
                    simp.append([i,j])
        return simp

    ''' GDAP to String '''
    def __str__(self):
        return self.G.to_string() + '\n' + str(self.M)
