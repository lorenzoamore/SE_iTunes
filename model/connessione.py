from dataclasses import dataclass

@dataclass
class Connessione:
    id1: int
    id2: int

    def __str__(self):
        return f"{self.id1}  {self.id2}"

    def __repr__(self):
        return self.id1

    def __hash__(self):
        return hash(self.id1)
    def __eq__(self, other):
        return self.id1 == other.id1 and self.id2 == other.id2