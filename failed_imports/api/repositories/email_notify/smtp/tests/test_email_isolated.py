import pytest

from ..serialisers import addresses_to_list

pytestmark = pytest.mark.isolated


def test_addresses_to_list_no_whitespace() -> None:
    """
    Given a set of comma-separated email addresses with no whitespace between them
    It returns a list of the addresses
    """
    addresses = "testemail@tdi-sustainability.com,thomas.esting@tdi-sustainability.com,t.est@tdi-sustainability.com"
    expected_result = [
        "testemail@tdi-sustainability.com",
        "thomas.esting@tdi-sustainability.com",
        "t.est@tdi-sustainability.com",
    ]

    assert addresses_to_list(addresses) == expected_result


def test_addresses_to_list_whitespace() -> None:
    """
    Given a set of comma-separated email addresses with whitespace
    It returns a list of the addresses with no trailing whitespace
    """
    addresses = "testemail@tdi-sustainability.com, thomas.esting@tdi-sustainability.com, t.est@tdi-sustainability.com"
    expected_result = [
        "testemail@tdi-sustainability.com",
        "thomas.esting@tdi-sustainability.com",
        "t.est@tdi-sustainability.com",
    ]

    assert addresses_to_list(addresses) == expected_result
