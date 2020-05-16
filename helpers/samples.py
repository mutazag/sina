import networkx as nx


class graph1(): 

    def __init__(self):
        self.data = []
        self.nodes = 'ABCDEFGHIJ'
        self.edges = [ 
            ('A','B'), ('A', 'E'),
            ('B','F'), 
            ('C','G'), 
            ('D','E'), ('D','H'),
            ('E','H'), 
            ('F','G'), ('F','J'), ('F','I'),
            ('G','J'),
            ('H','I'),
            #('I')
            #('J')
            ]
        self.pos = {
            'A': (2,3), 
            'B': (3,3),
            'C': (4,3),
            'D': (1,2), 
            'E': (2,2),
            'F': (3,2), 
            'G': (4,2), 
            'H': (1.5,1),
            'I': (2.5,1),
            'J': (3.5,1)
        }
        self.labels = {c:f'${c}$' for i,c in enumerate(self.nodes)}

    def Get_Networkx_Graph(self):
        G = nx.Graph()
        G.add_nodes_from(self.nodes)
        G.add_edges_from(self.edges)
        return(G)



if __name__ == '__main__':
    print('sample graph')