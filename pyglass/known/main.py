from requests import get, post

from pyglass.exceptions import SpyglassException
from pyglass.known import known_types


class Known:
    def __init__(self, base_url: str) -> None:
        self._known_url = f"{base_url}/v1/known/"

    def get_accounts(
        self, include_owner: bool = False, include_type: bool = False, type_filter: str = None
    ) -> list[known_types.Account]:
        """https://spyglass-api.web.app/known/accounts"""
        data = {
            "includeOwner": include_owner,
            "includeType": include_type,
            "typeFilter": type_filter,
        }
        response = post(f"{self._known_url}accounts", json=data)
        if not response.ok:
            raise SpyglassException(response.text)

        accounts: list[dict] = response.json()

        return [
            known_types.Account(
                address=account["address"],
                alias=account["alias"],
                owner=account.get("owner", None),
                type=account.get("type", None),
            )
            for account in accounts
        ]

    def get_vanities(self) -> list[str]:
        """https://spyglass-api.web.app/known/vanities"""
        response = get(f"{self._known_url}vanities")
        if not response.ok:
            raise SpyglassException(response.json())

        vanities: list[str] = response.json()
        return vanities
