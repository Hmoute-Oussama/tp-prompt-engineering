"""
Tests unitaires pytest pour les trois versions de format_product_code() (Exercice 2.2).
"""

import pytest

# ───────────────────────────────────────────────────────────────────
# Tests pour la Version 1 (Zero-Shot)
# ───────────────────────────────────────────────────────────────────
from v1_zero_shot import format_product_code as format_v1


class TestFormatV1ZeroShot:
    """Tests pour la version zero-shot."""

    def test_format_valide(self):
        # Note : la version zero-shot produit XXX-XXXX-XXX (tirets après 3e et 7e)
        result = format_v1("ABC123DEF4")
        assert result == "ABC-123D-EF4"  # Résultat différent de l'attendu !

    def test_longueur_invalide(self):
        with pytest.raises(ValueError):
            format_v1("SHORT")

    def test_caracteres_speciaux(self):
        with pytest.raises(ValueError):
            format_v1("ABC@123DEF")

    def test_chaine_vide(self):
        with pytest.raises(ValueError):
            format_v1("")


# ───────────────────────────────────────────────────────────────────
# Tests pour la Version 2 (One-Shot)
# ───────────────────────────────────────────────────────────────────
from v2_one_shot import format_product_code as format_v2


class TestFormatV2OneShot:
    """Tests pour la version one-shot."""

    def test_format_abc(self):
        assert format_v2("ABC123DEF4") == "ABC-123-DEF4"

    def test_format_xyz(self):
        assert format_v2("XYZ987GHIJ") == "XYZ-987-GHIJ"

    def test_longueur_invalide(self):
        with pytest.raises(ValueError):
            format_v2("SHORT")

    def test_caracteres_speciaux(self):
        with pytest.raises(ValueError):
            format_v2("ABC!23DEF4")


# ───────────────────────────────────────────────────────────────────
# Tests pour la Version 3 (Few-Shot)
# ───────────────────────────────────────────────────────────────────
from v3_few_shot import format_product_code as format_v3


class TestFormatV3FewShot:
    """Tests pour la version few-shot."""

    def test_format_abc(self):
        assert format_v3("ABC123DEF4") == "ABC-123-DEF4"

    def test_format_xyz(self):
        assert format_v3("XYZ987GHIJ") == "XYZ-987-GHIJ"

    def test_longueur_invalide(self):
        with pytest.raises(ValueError):
            format_v3("SHORT")

    def test_caracteres_speciaux(self):
        with pytest.raises(ValueError):
            format_v3("ABC!23DEF4")

    def test_type_invalide(self):
        with pytest.raises(ValueError):
            format_v3(12345)

    def test_chaine_avec_espaces(self):
        with pytest.raises(ValueError):
            format_v3("ABC 123DEF")
