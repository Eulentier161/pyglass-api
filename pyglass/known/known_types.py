from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True, order=True)
class Account:
    address: str
    alias: str
    owner: Optional[str]
    type: Optional[str]
