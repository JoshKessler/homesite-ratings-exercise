import math
import statistics

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

COVERAGE_EQ_SLOPE, COVERAGE_EQ_INTERCEPT = None, None


def get_age_factor(age):
    """Returns multiplier based on home age"""
    for k, v in sorted(HOME_AGE_FACTOR.items()):
        if age <= k:
            return v


def _interpolate_coverage_equation():
    """Estimates line of best fit for dwelling coverage factor using sum
    of square differences and sets global variables for slope and
    y intercept."""
    x_avg = statistics.mean(DWELLING_COVERAGE_FACTOR.keys())
    y_avg = statistics.mean(DWELLING_COVERAGE_FACTOR.values())
    x_dif = [x - x_avg for x in DWELLING_COVERAGE_FACTOR.keys()]
    y_dif = [y - y_avg for y in DWELLING_COVERAGE_FACTOR.values()]
    x_y_product = [x*y for x, y in zip(x_dif, y_dif)]
    square_dif = [(x - x_avg)**2 for x in DWELLING_COVERAGE_FACTOR.keys()]
    x_y_sum = sum(x_y_product)
    square_sum = sum(square_dif)
    slope = x_y_sum / square_sum
    intercept = y_avg - (slope * x_avg)
    global COVERAGE_EQ_SLOPE, COVERAGE_EQ_INTERCEPT
    COVERAGE_EQ_SLOPE, COVERAGE_EQ_INTERCEPT = slope, intercept


def calculate_coverage_factor(dwelling_cvg_amt):
    """Returns coverage factor for a given coverage amount, using either
    an exact match in the table or by interpolating it."""
    exact_match = DWELLING_COVERAGE_FACTOR.get(dwelling_cvg_amt)
    if exact_match:
        return exact_match
    else:
        if COVERAGE_EQ_INTERCEPT is None:
            _interpolate_coverage_equation()
        return (COVERAGE_EQ_SLOPE * dwelling_cvg_amt) + COVERAGE_EQ_INTERCEPT


def calculate_raw_premium(base, dwelling_cvg_factor, age_factor, roof_factor,
                          units_factor):
    """Returns premium based on all possible factors except discount."""
    return base * dwelling_cvg_factor * age_factor * roof_factor * units_factor


def apply_discount(base_premium):
    """Returns premium with discount applied"""
    return base_premium * (1 - DISCOUNT_RATE)
