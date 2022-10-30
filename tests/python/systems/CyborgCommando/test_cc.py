from util import roll


def test_cc_d10x():
    result = roll("d10xd10")
    assert result >= 1
    assert result <= 100
