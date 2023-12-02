import gnoll.__main__

m = lambda *x: list(gnoll.__main__.main_with_args(x))


def test_cli():
    print(m("1d4"))
    [[r]] = m("1d4")
    assert isinstance(r, int)

    [[(die1, die2), a, r]] = m("2d4", "--breakdown")
    assert all((isinstance(x, int) for x in [die1, die2, r]))
    assert a == "-->"

    executions = m("4d6kh3", "+", "1", "--breakdown", "--times", "6",
                   "--no-builtins")
    assert len(executions) == 6
    for (die1, die2, die3, die4), a, r in executions:
        assert all((isinstance(x, int) for x in [die1, die2, die3, die4, r]))
        assert a == "-->"
