from typing import Union
from requests import get

from .. import SpyglassException
from .network_types import NakamotoCoefficient, NcRepresentative, Peer, Quorum

NETWORK_URL = "https://api.spyglass.pw/banano/v1/network/"


def get_ledger_size() -> Union[int, float]:
    """https://spyglass-api.web.app/network/ledger-size"""
    response = get(f"{NETWORK_URL}ledger-size")
    if not response.ok:
        raise SpyglassException(response.json())

    ledger_size = response.json()["ledgerSizeMB"]
    return ledger_size


def get_nakamoto_coefficient() -> NakamotoCoefficient:
    """https://spyglass-api.web.app/network/nakamoto-coefficient"""
    response = get(f"{NETWORK_URL}nakamoto-coefficient")
    if not response.ok:
        raise SpyglassException(response.json())

    nakamoto_coefficient = response.json()
    return NakamotoCoefficient(
        delta=nakamoto_coefficient["delta"],
        nakamoto_coefficient=nakamoto_coefficient["nakamotoCoefficient"],
        nc_representatives=[
            NcRepresentative(rep["address"], rep["weight"])
            for rep in nakamoto_coefficient["ncRepresentatives"]
        ],
        nc_reps_weight=nakamoto_coefficient["ncRepsWeight"],
    )


def get_peer_versions() -> list[Peer]:
    """https://spyglass-api.web.app/network/peer-versions"""
    response = get(f"{NETWORK_URL}peers")
    if not response.ok:
        raise SpyglassException(response.json())

    peers = response.json()
    return [Peer(peer["count"], peer["version"]) for peer in peers]


def get_quorum() -> Quorum:
    """https://spyglass-api.web.app/network/quorum"""
    response = get(f"{NETWORK_URL}quorum")
    if not response.ok:
        raise SpyglassException(response.json())

    quorum = response.json()
    return Quorum(
        no_rep_percent=quorum["noRepPercent"],
        no_rep_weight=quorum["noRepWeight"],
        non_burned_weight=quorum["nonBurnedWeight"],
        offline_percent=quorum["offlinePercent"],
        offline_weight=quorum["offlineWeight"],
        online_percent=quorum["onlinePercent"],
        online_weight=quorum["onlineWeight"],
        online_weight_minimum=quorum["onlineWeightMinimum"],
        online_weight_quorum_percent=quorum["onlineWeightQuorumPercent"],
        peers_stake_weight=quorum["peersStakeWeight"],
        quorum_delta=quorum["quorumDelta"],
    )
