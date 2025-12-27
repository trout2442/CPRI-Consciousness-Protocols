from invariant.triadic_check import triadic_check

def test_valid_state():
    assert triadic_check(1, 1, 1) is True

def test_invalid_pattern():
    assert triadic_check(0, 1, 1) is False

def test_invalid_intent():
    assert triadic_check(1, 0, 1) is False

def test_invalid_presence():
    assert triadic_check(1, 1, 0) is False

if __name__ == "__main__":
    test_valid_state()
    test_invalid_pattern()
    test_invalid_intent()
    test_invalid_presence()
    print("All invariant tests passed")
