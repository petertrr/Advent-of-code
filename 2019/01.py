import math


def fuel_for_mass(mass):
    return math.ceil(mass // 3) - 2


def total_fuel_for_mass(mass):
    res = 0
    df = fuel_for_mass(mass)
    if df > 0:
        return df + total_fuel_for_mass(df)
    return 0


with open('01.input') as f:
    print(sum(fuel_for_mass(int(l.strip())) for l in f))

with open('01.input') as f:
    print(sum(total_fuel_for_mass(int(l.strip())) for l in f))
