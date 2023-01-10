import pytest


@pytest.mark.skip("only to be tested manually")
def test_pip_package():
    from gnoll import roll

    err_code, result, _ = roll("1d4")
    assert err_code == 0
    assert result in [1, 2, 3, 4]
