"""
Tests unitaires pytest pour les trois versions de calculate() (Exercice 2.1).
"""

import pytest

# ───────────────────────────────────────────────────────────────────
# Tests pour la Version 2 (prompt spécifique)
# ───────────────────────────────────────────────────────────────────
from v2_prompt_specifique import calculate as calculate_v2


class TestCalculateV2:
    """Tests pour la version générée par le prompt spécifique."""

    def test_addition(self):
        assert calculate_v2(5, 3, '+') == 8

    def test_subtraction(self):
        assert calculate_v2(5, 3, '-') == 2

    def test_multiplication(self):
        assert calculate_v2(5, 3, '*') == 15

    def test_division_arrondie(self):
        assert calculate_v2(5, 3, '/') == 1.67

    def test_division_par_zero(self):
        with pytest.raises(ZeroDivisionError):
            calculate_v2(5, 0, '/')

    def test_operateur_invalide(self):
        with pytest.raises(ValueError):
            calculate_v2(5, 3, '%')


# ───────────────────────────────────────────────────────────────────
# Tests pour la Version 3 (prompt avec persona)
# ───────────────────────────────────────────────────────────────────
from v3_prompt_persona import calculate as calculate_v3


class TestCalculateV3:
    """Tests pour la version générée par le prompt avec persona."""

    def test_addition(self):
        assert calculate_v3(5, 3, '+') == 8

    def test_subtraction(self):
        assert calculate_v3(5, 3, '-') == 2

    def test_multiplication(self):
        assert calculate_v3(5, 3, '*') == 15

    def test_division_arrondie(self):
        assert calculate_v3(5, 3, '/') == 1.67

    def test_division_par_zero(self):
        with pytest.raises(ZeroDivisionError):
            calculate_v3(5, 0, '/')

    def test_operateur_invalide(self):
        with pytest.raises(ValueError):
            calculate_v3(5, 3, '%')

    def test_type_error_operande(self):
        with pytest.raises(TypeError):
            calculate_v3("5", 3, '+')

    def test_type_error_operateur(self):
        with pytest.raises(TypeError):
            calculate_v3(5, 3, 123)
