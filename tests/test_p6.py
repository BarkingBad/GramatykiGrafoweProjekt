from matplotlib.pyplot import draw
from data.Vertex import Vertex
from data.VertexLabel import VertexLabel
from productions.P1 import P1
from productions.P6 import P6
import pytest 
from util.GraphDrawer import draw_graph
from common import verticies_graph_fragment
    
def test1():
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -1, 30, VertexLabel(1)), Vertex(0, -1.5, 31, VertexLabel(1)), Vertex(1, -1.5, 32, VertexLabel(1)), Vertex(0.5, -2, 33, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(1, 30), (2, 30), (1, 31), (3, 31), (2, 32), (4,32), (3, 33), (4, 33)]))
    graph_fragment.edges.remove((1, 2))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((4, 2))
    graph_fragment.edges.remove((3, 4))
    P6(5)
    assert verticies_graph_fragment.get(10) != None

def test2():
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -1, 32, VertexLabel(1)), Vertex(0, -1.5, 31, VertexLabel(1)), Vertex(1, -1.5, 30, VertexLabel(1)), Vertex(0.5, -2, 33, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(1, 30), (2, 30), (1, 31), (3, 31), (2, 32), (4,32), (3, 33), (4, 33)]))
    graph_fragment.edges.remove((1, 2))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((4, 2))
    graph_fragment.edges.remove((3, 4))
    P6(5)
    assert verticies_graph_fragment.get(10) == None

def test3():
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -1, 30, VertexLabel(1)), Vertex(0, -1.6, 31, VertexLabel(1)), Vertex(1, -1.5, 32, VertexLabel(1)), Vertex(0.5, -2, 33, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(1, 30), (2, 30), (1, 31), (3, 31), (2, 32), (4,32), (3, 33), (4, 33)]))
    graph_fragment.edges.remove((1, 2))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((4, 2))
    graph_fragment.edges.remove((3, 4))
    P6(5)
    assert verticies_graph_fragment.get(10) == None

def test4():
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -1, 30, VertexLabel(1)), Vertex(0, -1.5, 31, VertexLabel(1)), Vertex(1, -1.5, 32, VertexLabel(1)), Vertex(0.5, -2, 33, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(1, 30), (2, 30), (1, 31), (3, 31), (2, 32), (4,32), (3, 33)]))
    graph_fragment.edges.remove((1, 2))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((4, 2))
    graph_fragment.edges.remove((3, 4))
    P6(5)
    assert verticies_graph_fragment.get(10) == None

def test5():
    P1(0)
    graph_fragment = verticies_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0.5, -1, 30, VertexLabel(1)), Vertex(0, -1.5, 31, VertexLabel(1)), Vertex(1, -1.5, 32, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(1, 30), (2, 30), (1, 31), (3, 31), (2, 32), (4,32)]))
    graph_fragment.edges.remove((1, 2))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((4, 2))
    P6(5)
    assert verticies_graph_fragment.get(10) == None
