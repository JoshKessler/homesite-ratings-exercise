import math

ROOF_TYPE_FACTOR = {
    "Asphalt Shingles": 1.00,
    "Tin": 1.70,
    "Wood": 2.00,
}

BASE_PREMIUM = 350

HOME_AGE_FACTOR = {10: 1.00, 35: 1.50, 100: 1.80, math.inf: 1.95}

NUM_UNITS_FACTOR = {
    1: 1.00,
    2: 0.80,
    3: 0.80,
    4: 0.80,
}

DWELLING_COVERAGE_FACTOR = {
    100_000: 0.971,
    150_000: 1.104,
    200_000: 1.314,
    250_000: 1.471,
    300_000: 1.579,
    350_000: 1.761,
}

DISCOUNT_RATE = 0.05


def get_age_factor(age):
    """Returns multiplier based on home age"""
    for k, v in sorted(HOME_AGE_FACTOR.items()):
        if age <= k:
            return v
