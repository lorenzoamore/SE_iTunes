from dataclasses import dataclass

@dataclass
class Album:
    id: int
    title: str
    artist_id: int
    durata: float  # in minuti

    def __str__(self):
        return f"id: {self.id} titolo: {self.title} artist: {self.artist_id} durata: {self.durata}"

    def __repr__(self):
        return self.title

    def __hash__(self):
        return hash(self.id)


