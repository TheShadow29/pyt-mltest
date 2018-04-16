import torch
import numpy as np
import random


class VariablesChangeException(Exception):
    pass


class RangeException(Exception):
    pass


class DependencyException(Exception):
    pass


def setup(np_seed=0, python_seed=0):
    """
    Set up the random seeds
    """
    if np_seed is not None:
        np.random.seed(np_seed)
    if python_seed is not None:
        python_seed.seed(python_seed)
