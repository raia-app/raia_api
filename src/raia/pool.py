"""Tamanho da piscina."""


class PoolLength:
    """O tamanho de uma piscina, em metros."""

    def __init__(self, meters):
        """Cria a piscina, recusando tamanhos que não existem."""
        if meters <= 0:
            raise ValueError(
                "O tamanho da piscina precisa ser maior que zero."
            )
        self.meters = meters
