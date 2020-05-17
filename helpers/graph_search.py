import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(
    os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


import samples
from queue import Queue
import networkx as nx
import matplotlib.pyplot as plt


class GraphSearch():

    def __init__(self, graph=None):

        if graph is None:
            self.graph = samples.graph1()
        else: 
            self.graph = graph

        self.G = self.graph.Get_Networkx_Graph()

    def plot_graph(self, i, n, d_keys, discovered_nodes, nodes_in_q):
        # print('\t', n)
        # print('\t', d_keys)
        # print('\t', discovered_nodes)
        print(f'\titeration: {i}')
        pos = self.graph.pos
        nx.draw_networkx_nodes(self.G, pos, node_color='grey', node_size=500, alpha=0.8)
        nx.draw_networkx_nodes(self.G, pos, nodelist=d_keys, node_color='blue', node_size=500, alpha=0.8)
        nx.draw_networkx_nodes(self.G, pos, nodelist=nodes_in_q, node_color='yellow', node_size=500, alpha=0.6)
        nx.draw_networkx_nodes(self.G, pos, nodelist=discovered_nodes, node_color='yellow', node_size=500, alpha=0.9)
        nx.draw_networkx_nodes(self.G, pos, nodelist=n, node_color='green', linewidth=1.0, node_size=500, alpha=1.0)

        # add labels to nodes
        nx.draw_networkx_labels(self.G, pos, labels=self.graph.labels, font_size=16)

        # print iteration number next to node
        offset = (-.2, -.2)
        iteration_pos = tuple(
            abs(label_pos + offset) if abs(label_pos + offset) > 1 else abs(label_pos - offset)
            for label_pos, offset in zip(pos[n], offset))
        # print(iteration_pos)

        nx.draw_networkx_labels(self.G, {n: iteration_pos}, labels={n: i}, font_size=16)

        # add edges
        nx.draw_networkx_edges(self.G, pos, width=1.5, alpha=0.5, edge_color='grey')
        # highlight edges for new nodes discovered
        edges_nbunch = [(n, n_discovered) for n_discovered in discovered_nodes]
        # print('\tedges_nbunch', edges_nbunch)
        nx.draw_networkx_edges(self.G, pos, edgelist=edges_nbunch, width=2, alpha=0.8, edge_color='green')
        plt.show()

    def process_node(self, i, n, d, Q):
        print(f'processing node {n}')
        nx.set_node_attributes(self.G, {n: {'iteration': i}})

        # get list of neighbors t onode
        neighbors = list(self.G.neighbors(n))
        # print(f'\tneighbors: {[nn for nn in neighbors]}')

        # get node distace value
        dn = d[n]
        # print(f'\tdistance: {dn}')
        discovered_nodes = []  # used for plotting purposes
        for j, nn in enumerate(neighbors):
            # if neighboring node not in distance list
            # add it to the list with distance = dn + 1
            # and put it in Q for processing
            if nn not in d:
                # print(f'\t\tnew node {nn} discovered at distance {dn + 1}')
                discovered_nodes.append(nn)
                Q.put(nn)
                d[nn] = dn + 1
        # print(Q.queue)
        # print(f'\t{d.keys()}')
        # plot step progress
        nodes_in_q = list(Q.queue)
        self.plot_graph(i, n, list(d.keys()), discovered_nodes, nodes_in_q)

    def simulate_bfs(self, node):
        # initialise empty distance list and Q
        d = {}
        Q = Queue()

        # add first node to the Q, and set its distance to 0
        Q.put(node)
        d[node] = 0

        # print(Q.queue)
        # print(d)

        # reset iteration counter - display only not used in logic
        i = 0

        while not Q.empty():
            # get node from queue
            # process node
            # advance iteration counter
            n = Q.get()
            self.process_node(i, n, d, Q)
            i += 1


if __name__ == '__main__':
    print('simluate bfs')
    gs = GraphSearch()
    gs.simulate_bfs('D')
