from dataclasses import dataclass
from typing import Optional, Union


@dataclass(frozen=True, order=True)
class ConfirmedTX:
    address: Optional[str]
    amount: Optional[Union[int, float]]
    amount_raw: Optional[str]
    date: str
    hash: str
    height: int
    new_representative: Optional[str]
    timestamp: int
    type: str


@dataclass(frozen=True, order=True)
class Delegator:
    address: str
    weight: int


@dataclass(frozen=True, order=True)
class Delegators:
    count: int
    delegators: list[Delegator]
    empty_count: int
    weight_sum: int


@dataclass(frozen=True, order=True)
class Insights:
    block_count: int
    first_in_tx_hash: str
    first_in_tx_unix_timestamp: int
    first_out_tx_hash: Optional[str]
    first_out_tx_unix_timestamp: Optional[int]
    height_balances: Optional[list[Union[int, float]]]
    last_in_tx_hash: str
    last_in_tx_unix_timestamp: int
    last_out_tx_hash: Optional[str]
    last_out_tx_unix_timestamp: Optional[int]
    max_amount_received: Union[int, float]
    max_amount_received_hash: str
    max_amount_sent: Union[int, float]
    max_amount_sent_hash: Optional[str]
    max_balance: Union[int, float]
    max_balance_hash: str
    most_common_recipient_address: Optional[str]
    most_common_recipient_tx_count: int
    most_common_sender_address: str
    most_common_sender_tx_count: int
    total_amount_received: Union[int, float]
    total_amount_sent: Union[int, float]
    total_tx_change: int
    total_tx_received: int
    total_tx_sent: int


@dataclass(frozen=True, order=True)
class Overview:
    address: str
    balance: Optional[Union[int, float]]
    balance_raw: Optional[str]
    block_count: int
    delegators_count: int
    opened: bool
    principal: bool
    receivable: Union[int, float]
    receivable_raw: str
    representative: Optional[str]
    weight: Optional[int]


@dataclass(frozen=True, order=True)
class ReceivableTX:
    address: str
    amount: Union[int, float]
    amount_raw: str
    hash: str
    timestamp: int
