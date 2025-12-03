from dataclasses import dataclass

@dataclass
class Rifugio:
    id: int
    nome: str

    def __str__(self):
        return f'{self.id} ({self.nome})'
    def __hash__(self):
        return hash((self.id, self.nome))