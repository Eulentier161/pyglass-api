class NcRepresentative:
    def __init__(self, nc_representative: dict) -> None:
        self.address: str = nc_representative["address"]
        self.weight: int = nc_representative["weight"]


class NakamotoCoefficient:
    def __init__(self, request: dict) -> None:
        self.delta: int = request["delta"]
        self.nakamoto_coefficient: int = request["nakamotoCoefficient"]
        self.nc_representatives: list[NcRepresentative] = [
            NcRepresentative(nc_representative)
            for nc_representative in request["ncRepresentatives"]
        ]
        self.nc_reps_weight: int = request["ncRepsWeight"]


class Peer:
    def __init__(self, request: dict) -> None:
        self.count: int = request["count"]
        self.version: str = request["version"]


class Quorum:
    def __init__(self, request: dict) -> None:
        self.no_rep_percent: float = request["noRepPercent"]
        self.no_rep_weight: int = request["noRepWeight"]
        self.non_burned_weight: int = request["nonBurnedWeight"]
        self.offline_percent: float = request["offlinePercent"]
        self.offline_weight: int = request["offlineWeight"]
        self.online_percent: float = request["onlinePercent"]
        self.online_weight: int = request["onlineWeight"]
        self.onlineWeightMinimum: int = request["onlineWeightMinimum"]
        self.onlineWeightQuorumPercent: int = request["onlineWeightQuorumPercent"]
        self.peersStakeWeight: int = request["peersStakeWeight"]
        self.quorumDelta: int = request["quorumDelta"]
