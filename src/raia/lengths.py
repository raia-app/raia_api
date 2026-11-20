"""Cálculos de comprimentos de piscina."""


def count_lengths(distance_in_meters, pool_length_in_meters):
    """Devolve quantos comprimentos da piscina cabem na distância."""
    return distance_in_meters / pool_length_in_meters

def distance_fits_pool(distance_in_meters, pool_length_in_meters):
    """Diz se a distância corresponde a um número inteiro de comprimentos."""
    return distance_in_meters % pool_length_in_meters == 0
