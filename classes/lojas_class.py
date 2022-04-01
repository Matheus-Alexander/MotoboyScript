from dataclasses import dataclass, field

@dataclass(init=True, frozen=True)
class Loja:
    id: int
    comission: float
