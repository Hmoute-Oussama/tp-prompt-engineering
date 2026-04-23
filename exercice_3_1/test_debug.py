"""
Tests unitaires pytest pour la correction de calculate_average (Exercice 3.1).
"""

import pytest
from fixed_code import calculate_average

def test_average_mixed_types():
    assert calculate_average([1, 2, 'three', 4]) == pytest.approx(2.333333333)

def test_average_all_numbers():
    assert calculate_average([10, 20, 30]) == 20

def test_average_empty_list():
    assert calculate_average([]) == 0

def test_average_no_numbers():
    assert calculate_average(['a', 'b', 'c']) == 0

def test_average_floats():
    assert calculate_average([1.5, 2.5, 5]) == 3.0
