from dataclasses import dataclass
from typing import Optional, Union


@dataclass(frozen=True, order=True)
class Alias:
    address: str
    alias: str


@dataclass(frozen=True, order=True)
class ConfirmationInfo:
    count: Optional[int]
    time_span: Optional[int]
    average: Optional[int]
    percentile50: Optional[int]
    percentile75: Optional[int]
    percentile90: Optional[int]
    percentile95: Optional[int]
    percentile99: Optional[int]


@dataclass(frozen=True, order=True)
class MonitoredRepresentative:
    address: str
    cemented_blocks: Optional[int]
    confirmation_info: Optional[ConfirmationInfo]
    current_block: Optional[int]
    ip: Optional[str]
    location: Optional[str]
    name: Optional[str]
    node_uptime_startup: Optional[int]
    online: Optional[bool]
    peers: Optional[int]
    representative: Optional[str]
    system_load: Optional[Union[int, float]]
    total_mem: Optional[int]
    used_mem: Optional[int]
    version: Optional[str]
    weight: Optional[Union[int, float]]


@dataclass(frozen=True, order=True)
class Outage:
    offline_unix_timestamp: Optional[int]
    offline_date: Optional[str]
    online_unix_timestamp: Optional[int]
    online_date: Optional[str]
    duration_minutes: Optional[int]


@dataclass(frozen=True, order=True)
class UptimePercentages:
    day: Union[int, float]
    week: Union[int, float]
    month: Union[int, float]
    semi_annual: Union[int, float]
    year: Union[int, float]


@dataclass(frozen=True, order=True)
class UptimeStats:
    last_outage: Optional[Outage]
    ping_stats: Optional[list[dict[str, int]]]
    tracking_start_date: str
    tracking_start_unix_timestamp: int
    uptime_percentages: UptimePercentages


@dataclass(frozen=True, order=True)
class NodeMonitorStats:
    cemented_blocks: Optional[int]
    confirmation_info: Optional[ConfirmationInfo]
    current_block: Optional[int]
    ip: Optional[str]
    location: Optional[str]
    name: Optional[str]
    node_uptime_startup: Optional[int]
    peers: Optional[int]
    representative: Optional[str]
    system_load: Optional[Union[int, float]]
    total_mem: Optional[int]
    unchecked_blocks: Optional[int]
    used_mem: Optional[int]
    version: Optional[str]
    weight: Optional[Union[int, float]]


@dataclass(frozen=True, order=True)
class Representative:
    address: str
    alias: Optional[str]
    delegators_count: Optional[str]
    node_monitor_stats: Optional[NodeMonitorStats]
    online: bool
    uptime_stats: Optional[UptimeStats]
    weight: int


@dataclass(frozen=True, order=True)
class MonitorStats:
    has_above_avg_cemented_blocks: bool
    has_below_avg_unchecked_blocks: bool
    has_min_memory_requirement: bool
    name: str


@dataclass(frozen=True, order=True)
class Score:
    address: str
    alias: Optional[str]
    monitor_stats: Optional[MonitorStats]
    online: bool
    principal: bool
    score: int
    uptime_percentages: Optional[UptimePercentages]
    weight: int
    weight_percentage: Union[int, float]


@dataclass(frozen=True, order=True)
class Uptime:
    address: str
    last_outage: Optional[Outage]
    online: bool
    ping_stats: Optional[list[dict[str, int]]]
    tracking_start_date: str
    tracking_start_unix_timestamp: int
    uptime_percentages: UptimePercentages
