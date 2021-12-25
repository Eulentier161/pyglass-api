from typing import Optional


class Alias:
    def __init__(self, request: dict) -> None:
        self.address: str = request["address"]
        self.alias: str = request["alias"]

    def __repr__(self) -> str:
        return str(self.__dict__)


class ConfirmationInfo:
    def __init__(self, confirmation_info: dict) -> None:
        self.count: Optional[int] = confirmation_info.get("count", None)
        self.time_span: Optional[int] = confirmation_info.get("timeSpan", None)
        self.average: Optional[int] = confirmation_info.get("average", None)
        self.percentile50: Optional[int] = confirmation_info.get("percentile50", None)
        self.percentile75: Optional[int] = confirmation_info.get("percentile75", None)
        self.percentile90: Optional[int] = confirmation_info.get("percentile90", None)
        self.percentile95: Optional[int] = confirmation_info.get("percentile95", None)
        self.percentile99: Optional[int] = confirmation_info.get("percentile99", None)

    def __repr__(self) -> str:
        return str(self.__dict__)


class MonitoredRepresentative:
    def __init__(self, request: dict) -> None:
        self.address: str = request.get("address", None)
        self.cemented_blocks: Optional[int] = request.get("cementedBlocks", None)
        conf_info = request.get("confirmationInfo", None)
        self.confirmation_info: Optional[ConfirmationInfo] = (
            ConfirmationInfo(conf_info) if conf_info else None
        )
        self.current_block: Optional[int] = request.get("currentBlock", None)
        self.ip: Optional[str] = request.get("ip", None)
        self.location: Optional[str] = request.get("location", None)
        self.name: Optional[str] = request.get("name", None)
        self.node_uptime_startup: Optional[int] = request.get("nodeUptimeStartup", None)
        self.online: Optional[bool] = request.get("online", None)
        self.peers: Optional[int] = request.get("peers", None)
        self.representative: Optional[str] = request.get("representative", None)
        self.system_load: Optional[float] = request.get("systemLoad", None)
        self.total_mem: Optional[int] = request.get("totalMem", None)
        self.unchecked_blocks: Optional[int] = request.get("uncheckedBlocks", None)
        self.used_mem: Optional[int] = request.get("usedMem", None)
        self.version: Optional[str] = request.get("version", None)
        self.weight: Optional[float] = request.get("weight", None)

    def __repr__(self) -> str:
        return str(self.__dict__)


class Outage:
    def __init__(self, outage: dict) -> None:
        self.offline_unix_timestamp: Optional[int] = outage.get(
            "offlineUnixTimestamp", None
        )
        self.offline_date: Optional[str] = outage.get("offlineDate", None)
        self.online_unix_timestamp: Optional[int] = outage.get(
            "onlineUnixTimestamp", None
        )
        self.online_date: Optional[str] = outage.get("onlineDate", None)
        self.duration_minutes: Optional[int] = outage.get("durationMinutes", None)

    def __repr__(self) -> str:
        return str(self.__dict__)


class UptimePercentages:
    def __init__(self, uptime_percentages: dict) -> None:
        self.day: Optional[float] = uptime_percentages.get("day", None)
        self.week: Optional[float] = uptime_percentages.get("week", None)
        self.month: Optional[float] = uptime_percentages.get("month", None)
        self.semi_annual: Optional[float] = uptime_percentages.get("semiAnnual", None)
        self.year: Optional[float] = uptime_percentages.get("year", None)

    def __repr__(self) -> str:
        return str(self.__dict__)


class UptimeStats:
    def __init__(self, uptime_stats: dict) -> None:
        self.last_outage: Optional[Outage] = (
            Outage(uptime_stats["lastOutage"])
            if uptime_stats.get("lastOutage", None)
            else None
        )
        self.uptime_percentages: Optional[UptimePercentages] = (
            UptimePercentages(uptime_stats["uptimePercentages"])
            if uptime_stats.get("uptimePercentages", None)
            else None
        )
        self.ping_stats: Optional[list] = uptime_stats.get("pingStats", None)
        self.tracking_start_date: str = uptime_stats["trackingStartDate"]
        self.tracking_start_unix_timestamp: int = uptime_stats[
            "trackingStartUnixTimestamp"
        ]

    def __repr__(self) -> str:
        return str(self.__dict__)


class Representative:
    def __init__(self, request: dict) -> None:
        self.address: str = request["address"]
        self.alias: Optional[str] = request.get("alias", None)
        self.delegators_count: Optional[int] = request.get("delegatorsCount", None)
        self.node_monitor_stats: Optional[MonitoredRepresentative] = (
            MonitoredRepresentative(request["nodeMonitorStats"])
            if request.get("nodeMonitorStats", None)
            else None
        )
        self.online: bool = request["online"]
        self.uptime_stats: Optional[UptimeStats] = (
            UptimeStats(request["uptimeStats"])
            if request.get("uptimeStats", None)
            else None
        )
        self.weight = request["weight"]

    def __repr__(self) -> str:
        return str(self.__dict__)


class MonitorStats:
    def __init__(self, monitor_stats: dict) -> None:
        self.has_above_avg_cemented_blocks: bool = monitor_stats[
            "hasAboveAvgCementedBlocks"
        ]
        self.has_below_avg_unchecked_blocks: bool = monitor_stats[
            "hasBelowAvgUncheckedBlocks"
        ]
        self.has_min_memory_requirement: bool = monitor_stats["hasMinMemoryRequirement"]
        self.name: str = monitor_stats["name"]

    def __repr__(self) -> str:
        return str(self.__dict__)


class Score:
    def __init__(self, request: dict) -> None:
        self.address: str = request["address"]
        self.alias: Optional[str] = request.get("alias", None)
        self.monitor_stats: Optional[MonitorStats] = (
            MonitorStats(request["monitorStats"])
            if request.get("monitorStats", None)
            else None
        )
        self.online: bool = request["online"]
        self.principal: bool = request["principal"]
        self.score: int = request["score"]
        self.uptime_percentages: Optional[UptimePercentages] = (
            UptimePercentages(request["uptimePercentages"])
            if request.get("uptimePercentages", None)
            else None
        )
        self.weight: int = request["weight"]
        self.weight_percentage: float = request["weightPercentage"]

    def __repr__(self) -> str:
        return str(self.__dict__)


class Uptime:
    def __init__(self, request: dict) -> None:
        self.address: str = request["address"]
        self.last_outage: Optional[Outage] = (
            Outage(request["lastOutage"]) if request.get("lastOutage", None) else None
        )
        self.uptime_percentages: UptimePercentages = UptimePercentages(
            request["uptimePercentages"]
        )
        self.online: bool = request["online"]
        self.ping_stats: Optional[list] = request.get("pingStats", None)
        self.tracking_start_date: str = request["trackingStartDate"]
        self.tracking_start_unix_timestamp: int = request["trackingStartUnixTimestamp"]

    def __repr__(self) -> str:
        return str(self.__dict__)
