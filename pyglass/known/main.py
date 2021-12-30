from requests import get, post

from .. import SpyglassException
from .known_types import Account

KNOWN_URL = "https://api.spyglass.pw/banano/v1/known/"


def get_accounts(
    include_owner: bool = False, include_type: bool = False, type_filter: str = None
) -> list[Account]:
    """https://spyglass-api.web.app/known/accounts"""
    data = {
        "includeOwner": include_owner,
        "includeType": include_type,
        "typeFilter": type_filter,
    }
    response = post(f"{KNOWN_URL}accounts", json=data)
    if not response.ok:
        raise SpyglassException(response.text)

    accounts: list[dict] = response.json()

    return [
        Account(
            address=account["address"],
            alias=account["alias"],
            owner=account.get("owner", None),
            type=account.get("type", None),
        )
        for account in accounts
    ]


def get_vanities() -> list[str]:
    """https://spyglass-api.web.app/known/vanities"""
    response = get(f"{KNOWN_URL}vanities")
    if not response.ok:
        raise SpyglassException(response.json())

    vanities: list[str] = response.json()
    return vanities
