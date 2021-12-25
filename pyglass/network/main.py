from requests import get

from .network_types import NakamotoCoefficient, Peer, Quorum

NETWORK_URL = "https://api.spyglass.pw/banano/v1/network/"


def get_ledger_size() -> float:
    """https://spyglass-api.web.app/network/ledger-size"""
    request = get(f"{NETWORK_URL}ledger-size")
    return request.json()["ledgerSizeMB"]


def get_nakamoto_coefficient() -> NakamotoCoefficient:
    """https://spyglass-api.web.app/network/nakamoto-coefficient"""
    request = get(f"{NETWORK_URL}nakamoto-coefficient")
    return NakamotoCoefficient(request.json())


def get_peer_versions() -> list[Peer]:
    """https://spyglass-api.web.app/network/peer-versions"""
    request = get(f"{NETWORK_URL}peers")
    return [Peer(peer) for peer in request.json()]


def get_quorum() -> Quorum:
    """https://spyglass-api.web.app/network/quorum"""
    request = get(f"{NETWORK_URL}quorum")
    return Quorum(request.json())
