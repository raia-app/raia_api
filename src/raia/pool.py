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


    def count_lengths(self, distance_in_meters):
        """Devolve quantos comprimentos desta piscina cabem na distância."""
        return distance_in_meters / self.meters


    def fits(self, distance_in_meters):
        """Diz se a distância corresponde a um número interiro de comprimentos."""
        return distance_in_meters % self.meters == 0
    