import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._stores = []

    def fillDD(self):
        self._stores = self._model.getAllStores()
        for n in self._stores:
            self._view._ddStore.options.append(ft.dropdown.Option(n))
        self._view.update_page()

    def handleCreaGrafo(self, e):
        store = self._view._ddStore.value

        if store is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione! Selezionare lo store.", color='red'))
            self._view.update_page()

        else:
            grafo = self._model.buildGraph(store)
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato"))
            self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {self._model.getNumNodes()}"))
            self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {self._model.getNumEdges()}"))
            self._view.update_page()



    def handleCerca(self, e):
        pass

    def handleRicorsione(self, e):
        pass
