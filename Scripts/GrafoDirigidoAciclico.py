import copy

class Grafo_dirigido_aciclico:
    # Constructor de la estructura grafo dirigido.
    def __init__(self, V):
        # Número de vértices del grafo
        self.V = V
        # Número de aristas del grafo. Por defecto 0
        self.A = 0
        # Lista que contiene una lista por cada vértice del grafo.
        self.adj= []
        # Cada sublista de adj es una lista de los vértices adyacentes del i-ésimo vértice.
        # Por defecto vacía.
        for i in range(0,V):
            self.adj.append([])
    
    # Constructor copia
    def copia(self, G):
         
         self = copy.deepcopy(G)

         return self
    
    # Función que comprueba si el vértice dado pertenece al grafo
    def es_vertice(self, v):

         return v >= 0 and v <= self.V
            
     # Función que añade una arista desde o (origen) hasta d (destino)
    def crea_arista(self,o,d):
        
        # La condición de o > d asegura que no vamos a tener ciclos

        if( self.es_vertice(o) and self.es_vertice(d) and o > d ):

            self.adj[o].append(d)
            self.adj[o].sort(reverse=True)
            self.A += 1
    
    # Función que devuelve una lista con los vértices adyacentes de v
    def adyacentes(self, v):

        if( self.es_vertice(v) ):

            return self.adj[v]
    
    # Función que devuelve una string con los vértices del grafo y sus adyacentes
    def to_string(self):
        
        res=[]

        for i in range(0,self.V):

            res.append([i,self.adj[i]])

        return str(res)

    # Función que devuelve el grafo clausura transitiva de self
    def clausura_transitiva(self):
        
        C = Grafo_dirigido_aciclico(self.V)
        
        for i in range(0, self.V):
            
            al = []
            self.alcanzables(i,al)
            
            for j in al:
                C.crea_arista(i,j)
        
        return C
    
    # Función que almacena en res los vértices alcanzables desde o. Búsqueda en profundidad
    def alcanzables(self, o, res=[]):
        
        res.append(o)

        for v in self.adj[o]:
            if(v not in res):
                self.alcanzables(v, res)
            


