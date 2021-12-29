from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True, order=True)
class BlockContents:
    account: str
    balance: str
    link: str
    link_as_account: str
    previous: str
    representative: str
    signature: str
    type: str
    work: str


@dataclass(frozen=True, order=True)
class Block:
    amount: Union[int, float]
    amount_raw: str
    balance: str
    block_account: str
    confirmed: bool
    contents: BlockContents
    height: int
    source_account: str
    subtype: str
    timestamp: int
