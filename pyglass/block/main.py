from requests import get

from pyglass.block import block_types
from pyglass.exceptions import SpyglassException


class Block:
    def __init__(self, base_url: str) -> None:
        self._block_url = f"{base_url}/v1/block/"

    def get_block(self, block_hash: str) -> block_types.Block:
        """https://spyglass-api.web.app/account/block"""
        response = get(f"{self._block_url}{block_hash}")

        if not response.ok:
            raise SpyglassException(response.json())

        block = response.json()
        block_contents = block["contents"]
        return block_types.Block(
            amount=block["amount"],
            amount_raw=block["amountRaw"],
            balance=block["balance"],
            block_account=block["blockAccount"],
            confirmed=bool(block["confirmed"]),
            contents=block_types.BlockContents(
                account=block_contents["account"],
                balance=block_contents["balance"],
                link=block_contents["link"],
                link_as_account=block_contents["linkAsAccount"],
                previous=block_contents["previous"],
                representative=block_contents["representative"],
                signature=block_contents["signature"],
                type=block_contents["type"],
                work=block_contents["work"],
            ),
            height=block["height"],
            source_account=block["sourceAccount"],
            subtype=block["subtype"],
            timestamp=block["timestamp"],
        )
