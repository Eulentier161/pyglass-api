from requests import get
from .block_types import Block

block_url = "https://api.spyglass.pw/banano/v1/block/"


def get_block(hash: str) -> Block:
    request = get(f"{block_url}{hash}")
    return Block(request.json())