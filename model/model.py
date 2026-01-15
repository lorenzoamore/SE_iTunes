import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()
        self.nodi = []
        self.id_map = {}
        self.comp_conn = []
        self.best_path = []
        self.best_score = 0

    def build_graph(self,d):
        self.G.clear()
        self.nodi = DAO.get_all_albums(d)
        self.G.add_nodes_from(self.nodi)
        for n in self.nodi:
            self.id_map[n.id] = n
        connessioni = DAO.get_connessioni(d)
        for c in connessioni:
            a1 = self.id_map[c.id1]
            a2 = self.id_map[c.id2]
            self.G.add_edge(a1, a2)

    def connected_comp(self,a):
        self.comp_conn = list(nx.node_connected_component(self.G,a))
        return self.comp_conn

    def problema_ricorsivo(self,selezione,durata_max):

        comp_connessa = list(nx.node_connected_component(self.G,selezione))
        self._ricorsione(comp_connessa,durata_max,[selezione], selezione.durata)

    def _ricorsione(self,comp_connessa,durata_max,path,score):
        if len(path) > len(self.best_path):
            self.best_path = path.copy()
            self.best_score = score
        for a in comp_connessa:
            if a in path:
                continue
            else:
                if (score + a.durata) <= durata_max:
                    self._ricorsione(comp_connessa,
                                     durata_max,
                                     path + [a],
                                     score + a.durata)
