from typing import Optional


class Account:
    def __init__(self, request: dict) -> None:
        self.address: str = request["address"]
        self.alias: str = request["alias"]
        self.owner: Optional[str] = request.get("owner", None)
        self.type: Optional[str] = request.get("type", None)

    def __repr__(self) -> str:
        return str(self.__dict__)
