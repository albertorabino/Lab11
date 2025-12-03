from dataclasses import dataclass

@dataclass
class Connessione:
    id_rifugio1: int
    id_rifugio2: int

    def __str__(self):
        return f'{({self.id_rifugio1}, {self.id_rifugio2})}'

    def __hash__(self):
        return hash(( self.id_rifugio1, self.id_rifugio2))