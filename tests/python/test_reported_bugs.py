#!/usr/bin/env python3

import pytest
from util import roll


def test_issue_444():
    """
    issue reported that the built-in/mock combination produces a segmentation fault
    """
    with pytest.raises(Exception) as exc_info:
        roll('1d6', builtins = True, mock = 1)

    assert exc_info.type is None, f"Exception {exc_info.value} was raised unexpectedly"
    
