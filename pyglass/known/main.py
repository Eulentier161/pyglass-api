from requests import get, post

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
    request = post(f"{KNOWN_URL}accounts", json=data)
    return [Account(account) for account in request.json()]


def get_vanities() -> list[str]:
    """https://spyglass-api.web.app/known/vanities"""
    request = get(f"{KNOWN_URL}vanities")
    return request.json()
