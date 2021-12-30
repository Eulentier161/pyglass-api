from requests import get

from .. import SpyglassException
from .block_types import Block, BlockContents

BLOCK_URL = "https://api.spyglass.pw/banano/v1/block/"


def get_block(block_hash: str) -> Block:
    """https://spyglass-api.web.app/account/block"""
    response = get(f"{BLOCK_URL}{block_hash}")

    if not response.ok:
        raise SpyglassException(response.json())

    block = response.json()
    block_contents = block["contents"]
    return Block(
        amount=block["amount"],
        amount_raw=block["amountRaw"],
        balance=block["balance"],
        block_account=block["blockAccount"],
        confirmed=bool(block["confirmed"]),
        contents=BlockContents(
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
