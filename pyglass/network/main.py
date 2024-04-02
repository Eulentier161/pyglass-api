from typing import Union

from requests import get

from pyglass.exceptions import SpyglassException
from pyglass.network import network_types


class Network:
    def __init__(self, base_url: str) -> None:
        self._network_url = f"{base_url}/v1/network/"

    def get_ledger_size(self) -> Union[int, float]:
        """https://spyglass-api.web.app/network/ledger-size"""
        response = get(f"{self._network_url}ledger-size")
        if not response.ok:
            raise SpyglassException(response.json())

        ledger_size = response.json()["ledgerSizeMB"]
        return ledger_size

    def get_nakamoto_coefficient(self) -> network_types.NakamotoCoefficient:
        """https://spyglass-api.web.app/network/nakamoto-coefficient"""
        response = get(f"{self._network_url}nakamoto-coefficient")
        if not response.ok:
            raise SpyglassException(response.json())

        nakamoto_coefficient = response.json()
        return network_types.NakamotoCoefficient(
            delta=nakamoto_coefficient["delta"],
            nakamoto_coefficient=nakamoto_coefficient["nakamotoCoefficient"],
            nc_representatives=[
                network_types.NcRepresentative(rep["address"], rep["weight"])
                for rep in nakamoto_coefficient["ncRepresentatives"]
            ],
            nc_reps_weight=nakamoto_coefficient["ncRepsWeight"],
        )

    def get_peer_versions(self) -> list[network_types.Peer]:
        """https://spyglass-api.web.app/network/peer-versions"""
        response = get(f"{self._network_url}peers")
        if not response.ok:
            raise SpyglassException(response.json())

        peers = response.json()
        return [network_types.Peer(peer["count"], peer["version"]) for peer in peers]

    def get_quorum(self) -> network_types.Quorum:
        """https://spyglass-api.web.app/network/quorum"""
        response = get(f"{self._network_url}quorum")
        if not response.ok:
            raise SpyglassException(response.json())

        quorum = response.json()
        return network_types.Quorum(
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
