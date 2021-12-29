from typing import Union

from pyglass import SpyglassException
from requests import get, post

from .account_types import (
    ConfirmedTX,
    Delegator,
    Delegators,
    Insights,
    Overview,
    ReceivableTX,
)

ACCOUNT_URL = "https://api.spyglass.pw/banano/v1/account/"


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
    `size`: Max number of blocks to return; defaults to include 25 with a max of 500\n
    https://spyglass-api.web.app/account/confirmed
    """
    data = {
        "address": address,
        "includeChange": include_change,
        "includeReceive": include_receive,
        "includeSend": include_send,
        "offset": offset,
        "size": size,
    }
    response = post(f"{ACCOUNT_URL}confirmed-transactions", json=data)

    if not response.ok:
        raise SpyglassException(response.json())

    confirmed_tx: list[dict] = response.json()
    return [
        ConfirmedTX(
            address=tx.get("address", None),
            amount=tx.get("amount", None),
            amount_raw=tx.get("amountRaw", None),
            date=tx["date"],
            hash=tx["hash"],
            height=tx["height"],
            new_representative=tx.get("newRepresentative", None),
            timestamp=tx["timestamp"],
            type=tx["type"],
        )
        for tx in confirmed_tx
    ]


def get_delegators(
    address: str,
    offset: int = 0,
    size: int = 100,
    threshold: Union[int, float] = 0.001,
) -> Delegators:
    """
    `offset`: Skips the specified number of records in the result set. Used for pagination.\n
    `size`: Number of delegators to return. Defaults to show 100 delegators.\n
    `threshold`: Minimum required balance for a delegator to be included in the response.
    This not in raw. Defaults to 0.0001.\n
    https://spyglass-api.web.app/account/delegators
    """
    data = {"address": address, "offset": offset, "size": size, "threshold": threshold}
    response = post(f"{ACCOUNT_URL}delegators", json=data)

    if not response.ok:
        raise SpyglassException(response.json())

    delegators = response.json()
    return Delegators(
        count=delegators["count"],
        empty_count=delegators["emptyCount"],
        weight_sum=delegators["weightSum"],
        delegators=[
            Delegator(delegator["address"], delegator["weight"])
            for delegator in delegators["delegators"]
        ],
    )


def get_export(address: str):
    """https://spyglass-api.web.app/account/export"""
    data = {"address": address}
    resppnse = post(f"{ACCOUNT_URL}export", json=data)

    if not resppnse.ok:
        raise SpyglassException(resppnse.json())

    return resppnse.json()


def get_insights(address: str, include_height_balances: bool = False) -> Insights:
    """https://spyglass-api.web.app/account/insights"""
    data = {"address": address, "includeHeightBalances": include_height_balances}
    response = post(f"{ACCOUNT_URL}insights", json=data)

    if not response.ok:
        raise SpyglassException(response.json())

    insights: dict = response.json()
    return Insights(
        block_count=insights["blockCount"],
        first_in_tx_hash=insights["firstInTxHash"],
        first_in_tx_unix_timestamp=insights["firstInTxUnixTimestamp"],
        first_out_tx_hash=insights.get("firstOutTxHash", None),
        first_out_tx_unix_timestamp=insights.get("firstOutTxUnixTimestamp", None),
        height_balances=insights.get("heightBalances", None),
        last_in_tx_hash=insights["lastInTxHash"],
        last_in_tx_unix_timestamp=insights["lastInTxUnixTimestamp"],
        last_out_tx_hash=insights.get("lastOutTxHash", None),
        last_out_tx_unix_timestamp=insights.get("lastOutTxUnixTimestamp", None),
        max_amount_received=insights["maxAmountReceived"],
        max_amount_received_hash=insights["maxAmountReceivedHash"],
        max_amount_sent=insights["maxAmountSent"],
        max_amount_sent_hash=insights.get("maxAmountSentHash", None),
        max_balance=insights["maxBalance"],
        max_balance_hash=insights["maxBalanceHash"],
        most_common_recipient_address=insights.get("mostCommonRecipientAddress", None),
        most_common_recipient_tx_count=insights["mostCommonRecipientTxCount"],
        most_common_sender_address=insights["mostCommonSenderAddress"],
        most_common_sender_tx_count=insights["mostCommonSenderTxCount"],
        total_amount_received=insights["totalAmountReceived"],
        total_amount_sent=insights["totalAmountSent"],
        total_tx_change=insights["totalTxChange"],
        total_tx_received=insights["totalTxReceived"],
        total_tx_sent=insights["totalTxSent"],
    )


def get_overview(address: str) -> Overview:
    """https://spyglass-api.web.app/account/overview"""
    response = get(f"{ACCOUNT_URL}overview/{address}")

    if not response.ok:
        raise SpyglassException(response.json())

    overview: dict = response.json()
    return Overview(
        address=overview["address"],
        balance=overview.get("balance", None),
        balance_raw=overview.get("balanceRaw", None),
        block_count=overview["blockCount"],
        delegators_count=overview["delegatorsCount"],
        opened=overview["opened"],
        principal=overview["principal"],
        receivable=overview["receivable"],
        receivable_raw=overview["receivableRaw"],
        representative=overview.get("representative", None),
        weight=overview.get("weight", None),
    )


def get_representative(address: str) -> str:
    """https://spyglass-api.web.app/account/representative"""
    response = get(f"{ACCOUNT_URL}representative/{address}")

    if not response.ok:
        raise SpyglassException(response.json())

    return response.json()["representative"]


def get_receivable_transactions(
    address: str, offset: int = 0, size: int = 50
) -> list[ReceivableTX]:
    """
    `offset`: Skips the specified number of records in the result set. Used for pagination.\n
    `size`: Number of receivable transactions to return; Defaults to include 50 with a max of 500.\n
    https://spyglass-api.web.app/account/receivable
    """
    data = {"address": address, "offset": offset, "size": size}
    response = post(f"{ACCOUNT_URL}receivable-transactions", json=data)
    if not response.ok:
        raise SpyglassException(response.json())

    return [
        ReceivableTX(
            address=transaction["address"],
            amount=transaction["amount"],
            amount_raw=transaction["amountRaw"],
            hash=transaction["hash"],
            timestamp=transaction["timestamp"],
        )
        for transaction in response.json()
    ]
