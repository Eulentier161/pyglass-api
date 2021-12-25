from requests import get, post

from .representatives_types import (
    Alias,
    MonitoredRepresentative,
    Representative,
    Score,
    Uptime,
)

rep_url = "https://api.spyglass.pw/banano/v1/representatives/"


def get_aliases() -> list[Alias]:
    request = get(f"{rep_url}aliases")
    return [Alias(rep) for rep in request.json()]


def get_monitored() -> list[MonitoredRepresentative]:
    request = get(f"{rep_url}monitored")
    return [MonitoredRepresentative(rep) for rep in request.json()]


def get_online() -> list[str]:
    request = get(f"{rep_url}online")
    return request.json()


def get_pr_weight() -> float:
    request = get(f"{rep_url}pr-weight")
    return request.json()["weight"]


def get_representatives(
    addresses: list[str] = [],
    include_alias: bool = False,
    include_delegator_count: bool = False,
    include_node_monitor_stats: bool = False,
    include_uptime_pings: bool = False,
    include_uptime_stats: bool = False,
    is_monitored: bool = False,
    is_online: bool = False,
    is_principal: bool = False,
    minimum_weight: int = 10000,
    maximum_weight: int = None,
    uptime_threshold_day: float = 0,
    uptime_threshold_week: float = 0,
    uptime_threshold_month: float = 0,
    uptime_threshold_semi_annual: float = 0,
    uptime_threshold_year: float = 0,
) -> list[Representative]:
    """
    `addresses`: Limit search results to this list of addresses\n
    `include_node_monitor_stats`: Only applicable to monitored representatives\n
    `include_uptime_pings`: Append raw data used to calculate ping stats; only applicable when `include_uptime_stats` is enabled\n
    `include_uptime_stats`: Only reps with >10K BAN weight will have uptime stats available\n
    `is_monitored`: Filter to only show monitored representatives\n
    `is_online`: Filter to only show online representatives\n
    `is_principal`: Filter to only show representatives with >0.1% of the total online voting weight\n
    `minimum_weight`: Default of 10000 and minimum if 1000\n
    `uptime_threshold_day`: Filter to only show representatives with an uptime that exceeds this percentage. Only applicable when `include_uptime_stats` is enabled
    """
    data = {
        "addresses": addresses,
        "includeAlias": include_alias,
        "includeDelegatorCount": include_delegator_count,
        "includeNodeMonitorStats": include_node_monitor_stats,
        "includeUptimePings": include_uptime_pings,
        "includeUptimeStats": include_uptime_stats,
        "isMonitored": is_monitored,
        "isOnline": is_online,
        "isPrincipal": is_principal,
        "minimumWeight": minimum_weight,
        "uptimeThresholdDay": uptime_threshold_day,
        "uptimeThresholdWeek": uptime_threshold_week,
        "uptimeThresholdMonth": uptime_threshold_month,
        "uptimeThresholdSemiAnnual": uptime_threshold_semi_annual,
        "uptimeThresholdYear": uptime_threshold_year,
    }
    if maximum_weight:
        data["maximumWeight"] = maximum_weight
    request = post(f"{rep_url}", json=data)
    return [Representative(rep) for rep in request.json()]


def get_scores() -> list[Score]:
    request = get(f"{rep_url}scores")
    return [Score(score) for score in request.json()]


def get_uptime(
    include_pings: bool = None, representatives: list[str] = None
) -> list[Uptime]:
    data = {"includePings": include_pings, "representatives": representatives}
    request = post(f"{rep_url}uptime", json=data)
    return [Uptime(rep) for rep in request.json()]
