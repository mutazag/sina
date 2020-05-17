import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(
    os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


def test_sample_graph():
    from helpers.samples import SampleGraph
    sample_graph = SampleGraph()
    sample_graph.Get_Networkx_Graph()
    print(sample_graph.G.nodes)
    sample_graph.Draw_Networkx_Graph()
    pass


if __name__ == '__main__':
    test_sample_graph()
