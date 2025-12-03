def test_pgcd():
    from my_arithmetic_bhuchon.pgcd import pgcd

    assert pgcd(48, 18) == 6
    assert pgcd(101, 10) == 1
    assert pgcd(-48, 18) == 6
    assert pgcd(0, 5) == 5
    assert pgcd(5, 0) == 5
    assert pgcd(0, 0) == 0
    assert pgcd(270, 192) == 6
    assert pgcd(54, 24) == 6