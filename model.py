    class Model:
    def __init__(self):
        self._data = []
        
    def add_data(self, data):
        self._data.append(data)
        
    def get_data(self):
        return self._data
