from typing import Any, Iterable, Optional


def addresses_to_list(addresses: str) -> Iterable[str]:
    return [address.strip() for address in addresses.split(",")]


def messages_to_dict(
    plain: Optional[str] = None, html: Optional[str] = None
) -> dict[str, Any]:
    return {"plain": plain, "html": html}
