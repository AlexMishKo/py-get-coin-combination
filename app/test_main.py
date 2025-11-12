from app.main import get_coin_combination


def test_single_coin_combinations() -> None:
    test_cases = [
        (1, [1, 0, 0, 0]),
        (5, [0, 1, 0, 0]),
        (10, [0, 0, 1, 0]),
        (25, [0, 0, 0, 1])
    ]
    for cents, expected in test_cases:
        assert get_coin_combination(cents) == expected


def test_small_amounts() -> None:
    test_cases = [
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (23, [3, 1, 2, 0])
    ]
    for cents, expected in test_cases:
        assert get_coin_combination(cents) == expected


def test_larger_amounts() -> None:
    test_cases = [
        (50, [0, 0, 0, 2]),
        (87, [2, 0, 1, 3]),
        (99, [4, 0, 2, 3])
    ]
    for cents, expected in test_cases:
        assert get_coin_combination(cents) == expected


def test_zero_cents() -> None:
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_minimum_number_of_coins() -> None:
    test_cases = [
        (30, [0, 1, 1, 1]),
        (41, [1, 1, 1, 1]),
        (99, [4, 0, 2, 3])
    ]
    for cents, expected in test_cases:
        assert get_coin_combination(cents) == expected
