from decimal import Decimal, getcontext


def calculate_pi_gauss_legendre(digits: int):
    """
    This implements the Gauss-Legendre algorithm to calculate the
    value of Pi. Because it is memory intensive, practitioners typically
    do not implement this algorithm for actually calculating Pi.

    https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm
    """
    getcontext().prec = digits + 2

    a = Decimal(1)  # a_0
    b = Decimal(1) / Decimal(2).sqrt()  # b_0
    t = Decimal(1) / Decimal(4)  # t_0
    p = Decimal(1)  # p_0

    for _ in range(digits):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2

    return (a + b) ** 2 / (4 * t)


def truncate_decimal(value: Decimal, places: int):
    """Truncates a Decimal value to a specified number of decimal places."""
    value_str = f"{value}"
    dot_position = value_str.find(".")
    return Decimal(
        value_str[: dot_position + places + 1]
        if dot_position != -1
        else value_str
    )


def calculate_pi(digits: int):
    """Returns the correct value of Pi up to the given digits."""
    return truncate_decimal(calculate_pi_gauss_legendre(digits), digits)
