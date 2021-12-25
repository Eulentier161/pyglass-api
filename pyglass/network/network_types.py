class NcRepresentative:
    def __init__(self, nc_representative: dict) -> None:
        self.address: str = nc_representative["address"]
        self.weight: int = nc_representative["weight"]

    def __repr__(self) -> str:
        return str(self.__dict__)


class NakamotoCoefficient:
    def __init__(self, request: dict) -> None:
        self.delta: int = request["delta"]
        self.nakamoto_coefficient: int = request["nakamotoCoefficient"]
        self.nc_representatives: list[NcRepresentative] = [
            NcRepresentative(nc_representative)
            for nc_representative in request["ncRepresentatives"]
        ]
        self.nc_reps_weight: int = request["ncRepsWeight"]

    def __repr__(self) -> str:
        return str(self.__dict__)


class Peer:
    def __init__(self, request: dict) -> None:
        self.count: int = request["count"]
        self.version: str = request["version"]

    def __repr__(self) -> str:
        return str(self.__dict__)


class Quorum:
    def __init__(self, request: dict) -> None:
        self.no_rep_percent: float = request["noRepPercent"]
        self.no_rep_weight: int = request["noRepWeight"]
        self.non_burned_weight: int = request["nonBurnedWeight"]
        self.offline_percent: float = request["offlinePercent"]
        self.offline_weight: int = request["offlineWeight"]
        self.online_percent: float = request["onlinePercent"]
        self.online_weight: int = request["onlineWeight"]
        self.online_weight_minimum: int = request["onlineWeightMinimum"]
        self.online_weight_quorum_percent: int = request["onlineWeightQuorumPercent"]
        self.peers_stake_weight: int = request["peersStakeWeight"]
        self.quorum_delta: int = request["quorumDelta"]

    def __repr__(self) -> str:
        return str(self.__dict__)
