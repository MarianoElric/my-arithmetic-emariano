# SPDX-FileCopyrightText: 2024-present U.N. Owen <void@some.where>
#
# SPDX-License-Identifier: MIT


def gcd(a, b):
    """Calcule le plus grand commun diviseur de deux entiers a et b."""
    while b:
        a, b = b, a % b
    return a
