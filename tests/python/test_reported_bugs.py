#!/usr/bin/env python3

import pytest


def test_issue_444():
    """
    issue reported that the built-in/mock combination produces a segmentation fault
    WARN: this is testing the pip library not the local one
    """
    from gnoll import roll as gnollroll

    with pytest.raises(Exception) as exc_info:
        gnollroll("1d6", builtins=True, mock=1)

    assert exc_info.type is None, f"Exception {exc_info.value} was raised unexpectedly"
