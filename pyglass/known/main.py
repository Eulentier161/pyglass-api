from requests import get, post

from .known_types import Account

known_url = "https://api.spyglass.pw/banano/v1/known/"


def get_accounts(
    include_owner: bool = False, include_type: bool = False, type_filter: str = None
) -> list[Account]:
    data = {
        "includeOwner": include_owner,
        "includeType": include_type,
        "typeFilter": type_filter,
    }
    request = post(f"{known_url}accounts", json=data)
    return [Account(account) for account in request.json()]


def get_vanities() -> list[str]:
    request = get(f"{known_url}vanities")
    return request.json()
