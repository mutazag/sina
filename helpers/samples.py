# graph samples

import networkx as nx
import matplotlib.pyplot as plt


class SampleGraph():
    def __init__(self):
        self.data = []
        self.nodes = 'ABC'
        self.edges = [
            ('A', 'B'), ('A', 'C')]
        self.pos = {
            'A': (1, 1.5),
            'B': (2, 1),
            'C': (2, 2)
        }
        self.labels = {c: f'${c}$' for i, c in enumerate(self.nodes)}
        self.G = None

    def Get_Networkx_Graph(self):
        if self.G is None:
            self.G = nx.Graph()
            self.G.add_nodes_from(self.nodes)
            self.G.add_edges_from(self.edges)
        return(self.G)

    def Draw_Networkx_Graph(self):
        nx.draw_networkx_nodes(self.G, self.pos, node_color='grey', node_size=500, alpha=0.8)
        nx.draw_networkx_labels(self.G, self.pos, labels=self.labels, font_size=16)
        nx.draw_networkx_edges(self.G, self.pos, width=1.5, alpha=0.5, edge_color='g')
        plt.show()
        return


class graph1(SampleGraph):

    def __init__(self):
        SampleGraph.__init__(self)
        self.data = []
        self.nodes = 'ABCDEFGHIJ'
        self.edges = [
            ('A', 'B'), ('A', 'E'),
            ('B', 'F'),
            ('C', 'G'),
            ('D', 'E'), ('D', 'H'),
            ('E', 'H'),
            ('F', 'G'), ('F', 'J'), ('F', 'I'),
            ('G', 'J'),
            ('H', 'I'),
            # ('I')
            # ('J')
        ]

        self.pos = {
            'A': (2, 3),
            'B': (3, 3),
            'C': (4, 3),
            'D': (1, 2),
            'E': (2, 2),
            'F': (3, 2),
            'G': (4, 2),
            'H': (1.5, 1),
            'I': (2.5, 1),
            'J': (3.5, 1)
        }
        self.labels = {c: f'${c}$' for i, c in enumerate(self.nodes)}

    def Draw_Networkx_Graph(self):
        # node_color (color string, or array of floats) – Node color. Can be a single color format string (default=’r’),
        # or a sequence of colors with the same length as nodelist. If numeric values are specified they will be mapped
        # to colors using the cmap and vmin,vmax parameters. See matplotlib.scatter for more details.

        # can add nodelist to work with subset of nodes
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=list('ABCD'), node_color='red', node_size=500, alpha=0.8)
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=list('EFGH'), node_color='blue', node_size=500, alpha=0.8)
        nx.draw_networkx_nodes(self.G, self.pos, nodelist=list('IJ'), node_color='grey', node_size=500, alpha=0.8)

        # add labels to nodes
        nx.draw_networkx_labels(self.G, self.pos, labels=self.labels, font_size=16)

        # add edges
        nx.draw_networkx_edges(self.G, self.pos, width=1.5, alpha=0.5, edge_color='g')
        return


if __name__ == '__main__':
    print('sample graph')
