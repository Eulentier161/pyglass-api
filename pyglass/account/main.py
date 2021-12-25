from typing import Union

from requests import get, post

from .account_types import (
    ConfirmedTX,
    Delegators,
    Export,
    Insights,
    Overview,
    ReceivableTX,
    Representative,
)

account_url = "https://api.spyglass.pw/banano/v1/account/"


def get_confirmed_transactions(
    address: str,
    include_change: bool = True,
    include_receive: bool = True,
    include_send: bool = True,
    offset: int = 0,
    size: int = 25,
) -> list[ConfirmedTX]:
    """
    `offset`: Results will be returned starting from this block height\n
    `size`: Max number of blocks to return; defaults to include 25 with a max of 500
    """
    data = {
        "address": address,
        "includeChange": include_change,
        "includeReceive": include_receive,
        "includeSend": include_send,
        "offset": offset,
        "size": size,
    }
    request = post(f"{account_url}confirmed-transactions", json=data)
    return [ConfirmedTX(tx) for tx in request.json()]


def get_delegators(
    address: str,
    offset: int = 0,
    size: int = 100,
    threshold: Union[int, float] = 0.001,
) -> Delegators:
    """
    `offset`: Skips the specified number of records in the result set. Used for pagination.\n
    `size`: Number of delegators to return. Defaults to show 100 delegators.\n
    `threshold`: Minimum required balance for a delegator to be included in the response. This not in raw. Defaults to 0.0001.
    """
    data = {"address": address, "offset": offset, "size": size, "threshold": threshold}
    request = post(f"{account_url}delegators", json=data)
    return Delegators(request.json())


def get_export(address: str) -> Export:
    data = {"address": address}
    request = post(f"{account_url}export", json=data)
    return Export(request.json())


def get_insights(address: str, include_height_balances: bool = False) -> Insights:
    data = {"address": address, "includeHeightBalances": include_height_balances}
    request = post(f"{account_url}insights", data)
    return Insights(request.json())


def get_overview(address: str) -> Overview:
    request = get(f"{account_url}overview/{address}")
    return Overview(request.json())


def get_representative(address: str) -> Representative:
    request = get(f"{account_url}representative/{address}")
    return Representative(request.json())


def get_receivable_transactions(
    address: str, offset: int = 0, size: int = 50
) -> list[ReceivableTX]:
    """
    `offset`: Skips the specified number of records in the result set. Used for pagination.\n
    `size`: Number of receivable transactions to return; Defaults to include 50 with a max of 500.
    """
    data = {"address": address, "offset": offset, "size": size}
    request = post(f"{account_url}receivable-transactions", json=data)
    return [ReceivableTX(transaction) for transaction in request.json()]
