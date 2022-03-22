class GraphOriente:
    def __init__(self):
        self.liste_sommets = []
        self.liste_arcs = []

    def ajouter_sommets(self, A):
        self.liste_sommets.append(A)

    def ajouter_arcs(self,A,B):
        self.liste_arcs.append((A,B))

    def supprimer_arc(self,A,B):
        for i in range(len(self.liste_arcs)):
            if self.liste_arcs[i]==(A,B):
                del self.liste_arcs[i]
                break

    def liste_sommets_issus(self,A):
        liste=[]
        for i in range(len(self.liste_arcs)):
            if self.liste_arcs[i][0]== A:
                liste.append(self.liste_arcs[i][1])
        return liste    

#tests
if __name__ == '__main__':
    G = GraphOriente()
    G.ajouter_sommets('A')
    G.ajouter_sommets('B')  
    G.ajouter_sommets('C')  
    G.ajouter_sommets('D')
    G.ajouter_arcs('A','B')
    G.ajouter_arcs('A','C')  
    G.ajouter_arcs('B','D')  
    G.ajouter_arcs('C','D') 
    print(G.liste_sommets)
    print(G.liste_arcs)       
    G.supprimer_arc('A','B')
    print(G.liste_arcs)
    print(G.liste_sommets_issus('B'))
