from unittest import result

from lib2to3.btm_utils import reduce_tree

import networkx as nx
from database.dao import DAO
from model.rifugio import Rifugio


class Model:
    def __init__(self):
        self.G = nx.Graph()

    def build_graph(self, year: int) -> None:
        """Costruisce il grafo dei rifugi fino all'anno specificato."""

        self.G.clear()

        rifugi_selezionati = DAO.rifugi_fino_a(year)
        for rifugio in rifugi_selezionati:
            self.G.add_node(rifugio.id,nome=rifugio.nome)

        connessioni = DAO.connessioni(year)
        for conn in connessioni:
            self.G.add_edge(conn.id_rifugio1,conn.id_rifugio2)

    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """
        # TODO
        from model.rifugio import Rifugio
        result = []
        for node_id in self.G.nodes():
            name = self.G.nodes[node_id]['nome']
            result.append(Rifugio(node_id, name))
        return result


    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """
        # TODO
        return self.G.degree(node.id)

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        # TODO
        return nx.number_connected_components(self.G)

    def get_reachable(self, start):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.

        ESEMPIO
        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        b = self.get_reachable_recursive(start)

        return a
        """

        # devo sapere l'id di partenza, poi mi cerco le connessioni e restituisco la lista di connessioni
        # TODO
        a = self.get_reachable_bfs(start)
        b = self.get_reachable_recursive(start)
        return b



    def get_reachable_bfs(self, start):
        from model.rifugio import Rifugio
        result = []

        node_id = start.id

        bfs_tree = nx.bfs_tree(self.G, node_id)

        for nodo in bfs_tree.nodes():
            if nodo != node_id:
                nome = self.G.nodes[nodo]["nome"]
                result.append(Rifugio(nodo, nome))

        return result

    def get_reachable_recursive(self, start):
        from model.rifugio import Rifugio

        node_id = start.id
        visited = set()

        def dfs(u):
            visited.add(u)
            for v in self.G.neighbors(u):
                if v not in visited:
                    dfs(v)

        dfs(node_id)

        result = []
        for nodo in visited:
            if nodo != node_id:
                nome = self.G.nodes[nodo]["nome"]
                result.append(Rifugio(nodo, nome))

        return result
