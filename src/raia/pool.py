"""Tamanho da piscina."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PoolLength:
    """O tamanho de uma piscina, em metros."""

    meters:int

    def __post_init__(self):
        """Recusa tamanhos de piscina que não existem."""
        if self.meters <= 0:
            raise ValueError(
                "O tamanho da piscina precisa ser maior que zero."
            )


    def count_lengths(self, distance_in_meters):
        """Devolve quantos comprimentos desta piscina cabem na distância."""
        return distance_in_meters / self.meters


    def fits(self, distance_in_meters):
        """Diz se a distância corresponde a um número inteiro."""
        return distance_in_meters % self.meters == 0
