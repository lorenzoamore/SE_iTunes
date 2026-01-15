import flet as ft
import networkx as nx

from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        durata = float(self._view.txt_durata.value)
        self._model.build_graph(durata)
        self._view.lista_visualizzazione_1.clean()
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Grafo creato: {len(self._model.nodi)} album, {len(self._model.G.edges())} archi"))
        for a in self._model.nodi:
            self._view.dd_album.options.append(ft.dropdown.Option(key = a.id, text = a.title))
        self._view.update()

    def get_selected_album(self, e):
        """ Handler per gestire la selezione dell'album dal dropdown """""
        # TODO
        s = int(self._view.dd_album.value)
        album = self._model.id_map[s]
        return album


    def handle_analisi_comp(self, e):
        """ Handler per gestire l'analisi della componente connessa """""
        # TODO
        selezione = self.get_selected_album(e)
        componente_conn = self._model.connected_comp(selezione)
        lunghezza = len(componente_conn)
        durata = sum(a.durata for a in componente_conn)
        self._view.lista_visualizzazione_2.clean()
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Componente connessa: {lunghezza}"))
        self._view.lista_visualizzazione_2.controls.append(ft.Text(f"Durata totale: {durata}"))
        self._view.update()

    def handle_get_set_album(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del set di album """""
        # TODO
        s = self.get_selected_album(e)
        d = None
        try:
            d = int(self._view.txt_durata_totale.value)
        except ValueError:
            self._view.show_alert("Inserire un valore numerico")

        self._model.problema_ricorsivo(s,d)
        self._view.lista_visualizzazione_3.clean()
        self._view.lista_visualizzazione_3.controls.append(ft.Text(f"Set trovato ({len(self._model.best_path)}, durata {self._model.best_score} minuti"))
        for a in self._model.best_path:
            self._view.lista_visualizzazione_3.controls.append(ft.Text(f"- {a.title} ({a.durata} minuti)"))
        self._view.update()