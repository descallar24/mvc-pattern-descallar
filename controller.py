from model import Model
from view import View

class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        
    def add_data(self, data):
        self._model.add_data(data)
        
    def update_view(self):
        data = self._model.get_data()
        self._view.show_data(data)
