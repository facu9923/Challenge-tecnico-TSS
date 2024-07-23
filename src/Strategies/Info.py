class Info:
    idStrategy = None
    size = None
    def __init__(self, atributo1, atributo2):
        self.idStrategy = atributo1
        self.size = atributo2
    
    def get_data(self):
        return {'idStrategy': self.idStrategy, 'size': self.size}