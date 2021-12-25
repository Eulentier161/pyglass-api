class BlockContents:
    def __init__(self, contents: dict) -> None:
        self.account: str = contents["account"]
        self.balance: str = contents["balance"]
        self.link: str = contents["link"]
        self.link_as_account: str = contents["linkAsAccount"]
        self.previous: str = contents["previous"]
        self.representative: str = contents["representative"]
        self.signature: str = contents["signature"]
        self.type: str = contents["type"]
        self.work: str = contents["work"]


class Block:
    def __init__(self, request: dict) -> None:
        self.amount: float = request["amount"]
        self.amount_raw: str = request["amountRaw"]
        self.balance: str = request["balance"]
        self.block_account: str = request["blockAccount"]
        self.confirmed: bool = True if request["confirmed"] == "true" else False
        self.contents: BlockContents = BlockContents(request["contents"])
        self.height: int = request["height"]
        self.source_account: str = request["sourceAccount"]
        self.subtype: str = request["subtype"]
        self.timestamp: int = request["timestamp"]
