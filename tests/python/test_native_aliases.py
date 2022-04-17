#!/usr/bin/env python3

from unittest import mock
import pytest
import csv
import os
import sys
from util imp

# TODO: better tests for percentage dice - not fool proof

def test_percentile_dice():
    result = roll("d%")
    assert(result > 0)
    assert(result < 100)

def test_percentile_dice():
    result = roll("d%%2")
    assert(result >= 0)
    assert(result < 2)
