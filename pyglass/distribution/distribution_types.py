from typing import Optional, Union
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class BurnAccount:
    address: str
    pending: int


@dataclass(frozen=True, order=True)
class Burn:
    total_amount: int
    burn_accounts: list[BurnAccount]


@dataclass(frozen=True, order=True)
class Buckets:
    number0_0001: int
    number0_001: int
    number0_01: int
    number0_1: int
    number1: int
    number10: int
    number100: int
    number100_000: int
    number100_000_000: int
    number10_000: int
    number10_000_000: int
    number1_000: int
    number1_000_000: int
    total_accounts: int


@dataclass(frozen=True, order=True)
class DeveloperWallet:
    address: str
    balance: int


@dataclass(frozen=True, order=True)
class DeveloperFunds:
    total_balance: int
    wallets: list[DeveloperWallet]


@dataclass(frozen=True, order=True)
class RichListItem:
    address: str
    amount: Union[int, float]
    representative: Optional[str]


@dataclass(frozen=True, order=True)
class Supply:
    burned_amount: int
    circulating_amount: int
    circulating_percent: Union[int, float]
    dev_fund_amount: int
    dev_fund_percent: Union[int, float]
    total_amount: int
