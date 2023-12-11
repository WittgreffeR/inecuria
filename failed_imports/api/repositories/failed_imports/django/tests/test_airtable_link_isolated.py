import pytest

from ..serialisers import data_type_lookup

pytestmark = pytest.mark.isolated


def test_lookup_data_type_standard_vague() -> None:
    """
    Given the Standard data type and NO record id
    It returns the correct airtable url
    """
    result = data_type_lookup("Standard")

    assert (
        result
        == "https://airtable.com/appjDXUPkfYwb65DU/tblB1lc7nQmfDvsF4/viwZNNC7cRPUoJPxq"
    )


def test_lookup_data_type_standard_specific() -> None:
    """
    Given the Standard data type and a record id
    It returns the correct airtable url
    """
    result = data_type_lookup("Standard", "reckdEPRweQMVVfzW")

    assert (
        result
        == "https://airtable.com/appjDXUPkfYwb65DU/tblB1lc7nQmfDvsF4/viwZNNC7cRPUoJPxq/reckdEPRweQMVVfzW"
    )


def test_lookup_data_type_provision_vague() -> None:
    """
    Given a Provision data type and NO record id
    It returns the correct airtable url
    """
    result = data_type_lookup("Provision")

    assert (
        result
        == "https://airtable.com/appjDXUPkfYwb65DU/tbl7KmA5iAq28i1a1/viwHwGauUCVGxveMQ"
    )


def test_lookup_data_type_provision_specific() -> None:
    """
    Given a Provision data type and a record id
    It returns the correct airtable url
    """
    result = data_type_lookup("Provision", "recFMKw8IFDqCFCzC")

    assert (
        result
        == "https://airtable.com/appjDXUPkfYwb65DU/tbl7KmA5iAq28i1a1/viwHwGauUCVGxveMQ/recFMKw8IFDqCFCzC"
    )


def test_lookup_data_type_invalid() -> None:
    """
    Given an invalid/unrecognised data type
    It returns None
    """
    result = data_type_lookup("Bogus")

    assert result is None
