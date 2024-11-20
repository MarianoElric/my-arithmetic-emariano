from my_arithmetic_emariano import gcd


def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(101, 103) == 1
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0
