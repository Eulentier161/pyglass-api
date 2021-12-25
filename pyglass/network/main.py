from requests import get

from .network_types import NakamotoCoefficient, Peer, Quorum

network_url = "https://api.spyglass.pw/banano/v1/network/"


def get_ledger_size() -> float:
    request = get(f"{network_url}ledger-size")
    return request.json()["ledgerSizeMB"]


def get_nakamoto_coefficient() -> NakamotoCoefficient:
    request = get(f"{network_url}nakamoto-coefficient")
    return NakamotoCoefficient(request.json())


def get_peer_versions() -> list[Peer]:
    request = get(f"{network_url}peers")
    return [Peer(peer) for peer in request.json()]


def get_quorum() -> Quorum:
    request = get(f"{network_url}quorum")
    return Quorum(request.json())
