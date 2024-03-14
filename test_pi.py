from pi import calculate_pi_gauss_legendre, truncate_decimal, calculate_pi
from decimal import Decimal, getcontext
import math


def test_calculate_pi_gauss_legendre():
    digits = 3
    pi_approximation = calculate_pi_gauss_legendre(digits)
    getcontext().prec = digits + 1
    assert isinstance(pi_approximation, Decimal)
    assert pi_approximation == Decimal(
        "3.1416"
    )  # the last digit should be wrong


def test_truncate_decimal():
    digits = 3
    truncated = truncate_decimal(Decimal("1.1111"), digits)
    assert len(f"{truncated}") == digits + 2  # for the decimal point and "1"


def test_calculate_pi():
    digits = 3
    pi_approximation = calculate_pi(digits)
    assert (
        len(f"{pi_approximation}") == digits + 2
    )  # for the decimal point and "3"
    assert pi_approximation == Decimal("3.141")
    digits = 39
    pi_approximation = calculate_pi(digits)
    assert (
        len(f"{pi_approximation}") == digits + 2
    )  # for the decimal point and "3"
    assert pi_approximation == Decimal(
        "3.141592653589793238462643383279502884197"
    )
    digits = 100
    pi_approximation = calculate_pi(digits)
    assert (
        len(f"{pi_approximation}") == digits + 2
    )  # for the decimal point and "3"
    assert pi_approximation == Decimal(
        "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    )

    # check against standard library
    digits = 15
    pi_approximation = calculate_pi(digits)
    assert f"{pi_approximation}" == f"{math.pi}"
