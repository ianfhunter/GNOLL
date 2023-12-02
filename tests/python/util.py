import importlib.util as iu
import os
import subprocess
from enum import Enum

import numpy as np
from gnoll import gnoll_roll


class Mock(Enum):
    NO_MOCK = 0
    RETURN_CONSTANT = 1
    RETURN_INCREMENTING = 2
    RETURN_DECREMENTING = 3
    RETURN_CONSTANT_TWICE_ELSE_CONSTANT_ONE = 4


def error_handled_by_gnoll(e):
    test = e.__class__.__name__ == "GNOLLException"
    if not test:
        print(e)
        raise AssertionError

def roll(s,
         mock_mode=Mock.NO_MOCK,
         mock_const=3,
         verbose=False,
         squeeze=True,
         builtins=False):
    
    if mock_mode is None:
        mock_mode = Mock.NO_MOCK
        
    first_run = False

    dt_return = gnoll_roll(
        s,
        mock=mock_mode.value,
        mock_const=mock_const,
        verbose=verbose,
        breakdown=True,
        builtins=builtins,
    )
    exit_code = dt_return[0]
    result = dt_return[1]
    dice_breakdown = dt_return[2] if len(dt_return) > 2 else []

    if squeeze:
        result = np.squeeze(np.array(result)).tolist()

    if exit_code:
        raise ValueError

    return result, dice_breakdown
