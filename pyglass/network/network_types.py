from dataclasses import dataclass
from typing import Union


@dataclass(frozen=True, order=True)
class NcRepresentative:
    address: str
    weight: int


@dataclass(frozen=True, order=True)
class NakamotoCoefficient:
    delta: int
    nakamoto_coefficient: int
    nc_representatives: list[NcRepresentative]
    nc_reps_weight: int


@dataclass(frozen=True, order=True)
class Peer:
    count: int
    version: str


@dataclass(frozen=True, order=True)
class Quorum:
    no_rep_percent: Union[int, float]
    no_rep_weight: int
    non_burned_weight: int
    offline_percent: Union[int, float]
    offline_weight: int
    online_percent: Union[int, float]
    online_weight: int
    online_weight_minimum: int
    online_weight_quorum_percent: int
    peers_stake_weight: int
    quorum_delta: int
