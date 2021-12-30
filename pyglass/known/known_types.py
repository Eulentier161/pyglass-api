from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Account:
    address: str
    alias: str
    owner: Optional[str]
    type: Optional[str]
