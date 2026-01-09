from models.farm import Farm


def advance_days(n: int, farm: Farm):
    if n<=0:
        raise ValueError("No se puede dias negativos")

    for _ in range(n):
        farm.day+=1