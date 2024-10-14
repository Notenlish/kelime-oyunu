class Player:
    def __init__(self, name: str, score: int, time: float) -> None:
        self.name = name
        self.score = score
        self.time = time

    def draw(self): ...

    def __repr__(self) -> str:
        return f"<Player {self.name} {self.score} {self.time} />"


class PlayerManager:
    def __init__(self) -> None:
        self.players: list[Player] = []
        self.read_db()

    def read_db(self):
        with open("players.txt", "r") as f:
            lines = f.readlines()
            self.players = [Player(l.strip(), -1, -1) for l in lines]
