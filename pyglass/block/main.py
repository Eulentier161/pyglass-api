from requests import get
from .block_types import Block

BLOCK_URL = "https://api.spyglass.pw/banano/v1/block/"


def get_block(block_hash: str) -> Block:
    """https://spyglass-api.web.app/account/block"""
    request = get(f"{BLOCK_URL}{block_hash}")
    return Block(request.json())
