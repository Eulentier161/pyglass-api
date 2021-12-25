from requests import get, post

from .representatives_types import (
    Alias,
    MonitoredRepresentative,
    Representative,
    Score,
    Uptime,
)

REPRESENTATIVE_URL = "https://api.spyglass.pw/banano/v1/representatives/"


def get_aliases() -> list[Alias]:
    """https://spyglass-api.web.app/representatives/aliased"""
    request = get(f"{REPRESENTATIVE_URL}aliases")
    return [Alias(rep) for rep in request.json()]


def get_monitored() -> list[MonitoredRepresentative]:
    """https://spyglass-api.web.app/representatives/monitored"""
    request = get(f"{REPRESENTATIVE_URL}monitored")
    return [MonitoredRepresentative(rep) for rep in request.json()]


def get_online() -> list[str]:
    """https://spyglass-api.web.app/representatives/online"""
    request = get(f"{REPRESENTATIVE_URL}online")
    return request.json()


def get_pr_weight() -> float:
    """https://spyglass-api.web.app/representatives/pr-weight"""
    request = get(f"{REPRESENTATIVE_URL}pr-weight")
    return request.json()["weight"]


def get_representatives(
    addresses: list[str] = None,
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
    `include_uptime_pings`: Append raw data used to calculate ping stats; only applicable when
    `include_uptime_stats` is enabled\n
    `include_uptime_stats`: Only reps with >10K BAN weight will have uptime stats available\n
    `is_monitored`: Filter to only show monitored representatives\n
    `is_online`: Filter to only show online representatives\n
    `is_principal`: Filter to only show representatives with >0.1% of the total online voting weight\n
    `minimum_weight`: Default of 10000 and minimum if 1000\n
    `uptime_threshold_day`: Filter to only show representatives with an uptime that exceeds this percentage.
    Only applicable when `include_uptime_stats` is enabled\n
    https://spyglass-api.web.app/representatives/representatives
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
    request = post(f"{REPRESENTATIVE_URL}", json=data)
    return [Representative(rep) for rep in request.json()]


def get_scores() -> list[Score]:
    """https://spyglass-api.web.app/representatives/scores"""
    request = get(f"{REPRESENTATIVE_URL}scores")
    return [Score(score) for score in request.json()]


def get_uptime(
    include_pings: bool = None, representatives: list[str] = None
) -> list[Uptime]:
    """https://spyglass-api.web.app/representatives/uptime"""
    data = {"includePings": include_pings, "representatives": representatives}
    request = post(f"{REPRESENTATIVE_URL}uptime", json=data)
    return [Uptime(rep) for rep in request.json()]
