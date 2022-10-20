import pytest


@pytest.mark.skip("only to be tested manually")
def test_pip_package():
    from gnoll.parser import roll

    err_code, result = roll("1d4")
    assert err_code == 0
    assert result in [1, 2, 3, 4]
