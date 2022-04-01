from dataclasses import dataclass, field

@dataclass(init=True)
class Pedido:
    id: int
    id_loja: int
    price: float
    assigned: bool = False

    def change_assigned_value(self, value):
        """
        Updates self.assigned to the received value parameter.

        Parameters
        ----------
        value : bool
            True or False.
        """
        self.assigned = value
