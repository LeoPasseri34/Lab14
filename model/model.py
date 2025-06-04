import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodes = []
        self._graph = nx.DiGraph()
        self._idMap = {}

    def getAllStores(self):
        return DAO.getStores()

    def buildGraph(self, id):
        self._graph.clear()
        self._nodes = DAO.getNodes(id)
        for n in self._nodes:
            self._idMap[n.order_id] = n
        self._graph.add_nodes_from(self._nodes)
        return self._graph

    def addEdges(self):
        pass


    def getNumNodes(self):
        return self._graph.number_of_nodes()

    def getNumEdges(self):
        return self._graph.number_of_edges()

    def getNodes(self):
        return self._graph.nodes()
