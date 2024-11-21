# SPDX-FileCopyrightText: 2024-present U.N. Owen <void@some.where>
#
# SPDX-License-Identifier: MIT


def gcd(a, b):
    """
    Compute the greatest common divisor of two integers.

    Parameters
    ----------
    a : int
        First integer.
    b : int
        Second integer.

    Returns
    -------
    int
        The greatest common divisor of `a` and `b`.
    """
    while b:
        a, b = b, a % b
    return a
