from typing import Any, Optional


class ConfirmedTX:
    def __init__(self, request: dict) -> None:
        self.address: Optional[str] = request.get("address", None)
        self.amount: Optional[float] = request.get("amount", None)
        self.amount_raw: Optional[str] = request.get("amountRaw", None)
        self.date: str = request["date"]
        self.hash: str = request["hash"]
        self.height: int = request["height"]
        self.new_representative: Optional[str] = request.get("newRepresentative", None)
        self.timestamp: int = request["timestamp"]
        self.type: str = request["type"]

    def __repr__(self) -> str:
        return str(self.__dict__)


class Delegator:
    def __init__(self, delegator: dict) -> None:
        self.address: str = delegator["address"]
        self.weight: int = delegator["weight"]

    def __repr__(self) -> str:
        return str(self.__dict__)


class Delegators:
    def __init__(self, request: dict) -> None:
        self.count: int = request["count"]
        self.delegators: list[Delegator] = [
            Delegator(delegator) for delegator in request["delegators"]
        ]
        self.empty_count = request["emptyCount"]
        self.weight_sum = request["weightSum"]

    def __repr__(self) -> str:
        return str(self.__dict__)


class Export:
    def __init__(self, request: dict) -> None:
        self.error: Optional[dict] = request.get("error", None)
        self.text: Optional[str] = request.get("text", None)

    def __repr__(self) -> str:
        return str(self.__dict__)


class Insights:
    def __init__(self, request: dict) -> None:
        self.block_count: int = request["number"]
        self.first_in_tx_hash: str = request["string"]
        self.first_in_tx_unix_timestamp: int = request["number"]
        self.first_out_tx_hash: str = request["string"]
        self.first_out_tx_unix_timestamp: int = request["number"]
        self.height_balances: Optional[Any] = request.get("heightBalances", None)
        self.last_in_tx_hash: str = request["string"]
        self.last_in_tx_unix_timestamp: int = request["number"]
        self.last_out_tx_hash: str = request["string"]
        self.last_out_tx_unix_timestamp: int = request["number"]
        self.max_amount_received: float = request["number"]
        self.max_amount_received_hash: str = request["string"]
        self.max_amount_sent: float = request["number"]
        self.max_amount_sent_hash: str = request["string"]
        self.max_balance: float = request["number"]
        self.max_balance_hash: str = request["string"]
        self.most_common_recipient_address: str = request["string"]
        self.most_common_recipient_tx_count: int = request["number"]
        self.most_common_sender_address: str = request["string"]
        self.most_common_sender_tx_count: int = request["number"]
        self.total_amount_received: float = request["number"]
        self.total_amount_sent: float = request["number"]
        self.total_tx_change: int = request["number"]
        self.total_tx_received: int = request["number"]
        self.total_tx_sent: int = request["number"]

    def __repr__(self) -> str:
        return str(self.__dict__)


class Overview:
    def __init__(self, request: dict) -> None:
        self.address: str = request["address"]
        self.balance: Optional[float] = request.get("balance", None)
        self.balance_raw: Optional[str] = request.get("balanceRaw", None)
        self.block_count: int = request["blockCount"]
        self.delegators_count: int = request["delegatorsCount"]
        self.opened: bool = request["opened"]
        self.principal: bool = request["principal"]
        self.receivable: float = request["receivable"]
        self.receivable_raw: str = request["receivableRaw"]
        self.representative: Optional[str] = request.get("representative", None)
        self.weight: Optional[int] = request.get("weight", None)

    def __repr__(self) -> str:
        return f"{self.__dict__}"


class ReceivableTX:
    def __init__(self, request: dict) -> None:
        self.address: str = request["address"]
        self.amount: float = request["amount"]
        self.amount_raw: str = request["amountRaw"]
        self.hash: str = request["hash"]
        self.timestamp: int = request["timestamp"]

    def __repr__(self) -> str:
        return str(self.__dict__)
