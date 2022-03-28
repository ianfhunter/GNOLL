#!/usr/bin/env python3

from unittest import mock
import pytest
import csv
import os
import sys
from util import roll

def test_dropping():
    # Test each type of notation
    ## Keep Highest
    result = roll("2d20kh", mock_random=(8,11))
    assert(result == 11)
    result = roll("2d20dl", mock_random=(8,11))
    assert(result == 11)
    result = roll("2d20h", mock_random=(8,11))
    assert(result == 11)

    ## Keep Lowest
    result = roll("2d20kl", mock_random=(8,11))
    assert(result == 8)
    result = roll("2d20dh", mock_random=(8,11))
    assert(result == 8)
    result = roll("2d20l", mock_random=(8,11))
    assert(result == 8)

    # Keep >1
    result = roll("3d20kh2", mock_random=(8,11,19))
    assert(result == 30)

    result = roll("3d20kl2", mock_random=(8,11,19))
    assert(result == 19)
