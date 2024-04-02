from typing import Union

from requests import get, post

from pyglass.exceptions import SpyglassException
from pyglass.representatives import representatives_types


class Representatives:
    def __init__(self, base_url: str) -> None:
        self._representatives_url = f"{base_url}/v1/representatives/"

    def get_aliases(self) -> list[representatives_types.Alias]:
        """https://spyglass-api.web.app/representatives/aliased"""
        response = get(f"{self._representatives_url}aliases")
        if not response.ok:
            raise SpyglassException(response.json())

        aliases = response.json()
        return [representatives_types.Alias(address=alias["address"], alias=alias["alias"]) for alias in aliases]

    def get_monitored(self) -> list[representatives_types.MonitoredRepresentative]:
        """https://spyglass-api.web.app/representatives/monitored"""
        response = get(f"{self._representatives_url}monitored")
        if not response.ok:
            raise SpyglassException(response.json())

        monitored = response.json()
        return [
            representatives_types.MonitoredRepresentative(
                address=rep["address"],
                cemented_blocks=rep.get("cementedBlocks", None),
                confirmation_info=(
                    representatives_types.ConfirmationInfo(
                        count=rep["confirmationInfo"].get("count", None),
                        time_span=rep["confirmationInfo"].get("timeSpan", None),
                        average=rep["confirmationInfo"].get("average", None),
                        percentile50=rep["confirmationInfo"].get("percentile50", None),
                        percentile75=rep["confirmationInfo"].get("percentile75", None),
                        percentile90=rep["confirmationInfo"].get("percentile90", None),
                        percentile95=rep["confirmationInfo"].get("percentile95", None),
                        percentile99=rep["confirmationInfo"].get("percentile99", None),
                    )
                    if rep.get("confirmationInfo")
                    else None
                ),
                current_block=rep.get("currentBlock", None),
                ip=rep.get("ip", None),
                location=rep.get("location", None),
                name=rep.get("name", None),
                node_uptime_startup=rep.get("nodeUptimeStartup", None),
                online=rep.get("online", None),
                peers=rep.get("peers", None),
                representative=rep.get("representative", None),
                system_load=rep.get("systemLoad", None),
                total_mem=rep.get("totalMem", None),
                used_mem=rep.get("usedMem", None),
                version=rep.get("version", None),
                weight=rep.get("weight", None),
            )
            for rep in monitored
        ]

    def get_online(self) -> list[str]:
        """https://spyglass-api.web.app/representatives/online"""
        response = get(f"{self._representatives_url}online")
        if not response.ok:
            raise SpyglassException(response.json())

        return response.json()

    def get_pr_weight(self) -> Union[int, float]:
        """https://spyglass-api.web.app/representatives/pr-weight"""
        response = get(f"{self._representatives_url}pr-weight")
        if not response.ok:
            raise SpyglassException(response.json())

        return response.json()["weight"]

    def get_representatives(
        self,
        addresses: list[str] = None,
        include_alias: bool = None,
        include_delegator_count: bool = None,
        include_node_monitor_stats: bool = None,
        include_uptime_pings: bool = None,
        include_uptime_stats: bool = None,
        is_monitored: bool = None,
        is_online: bool = None,
        is_principal: bool = None,
        minimum_weight: int = 10000,
        maximum_weight: int = None,
        uptime_threshold_day: float = None,
        uptime_threshold_week: float = None,
        uptime_threshold_month: float = None,
        uptime_threshold_semi_annual: float = None,
        uptime_threshold_year: float = None,
    ) -> list[representatives_types.Representative]:
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
            "maximumWeight": maximum_weight,
            "uptimeThresholdDay": uptime_threshold_day,
            "uptimeThresholdWeek": uptime_threshold_week,
            "uptimeThresholdMonth": uptime_threshold_month,
            "uptimeThresholdSemiAnnual": uptime_threshold_semi_annual,
            "uptimeThresholdYear": uptime_threshold_year,
        }
        response = post(f"{self._representatives_url}", json=data)
        if not response.ok:
            raise SpyglassException(response.json())

        reps = response.json()
        return [
            representatives_types.Representative(
                address=rep["address"],
                alias=rep.get("alias", None),
                delegators_count=rep.get("delegatorsCount", None),
                node_monitor_stats=(
                    representatives_types.NodeMonitorStats(
                        cemented_blocks=rep["nodeMonitorStats"].get("cementedBlocks", None),
                        confirmation_info=rep["nodeMonitorStats"].get("confirmationInfo", None),
                        current_block=rep["nodeMonitorStats"].get("currentBlock", None),
                        ip=rep["nodeMonitorStats"].get("ip", None),
                        location=rep["nodeMonitorStats"].get("location", None),
                        name=rep["nodeMonitorStats"].get("name", None),
                        node_uptime_startup=rep["nodeMonitorStats"].get("nodeUptimeStartup", None),
                        peers=rep["nodeMonitorStats"].get("peers", None),
                        representative=rep["nodeMonitorStats"].get("representative", None),
                        system_load=rep["nodeMonitorStats"].get("systemLoad", None),
                        total_mem=rep["nodeMonitorStats"].get("totalMem", None),
                        unchecked_blocks=rep["nodeMonitorStats"].get("uncheckedBlocks", None),
                        used_mem=rep["nodeMonitorStats"].get("usedMem", None),
                        version=rep["nodeMonitorStats"].get("version", None),
                        weight=rep["nodeMonitorStats"].get("weight", None),
                    )
                    if rep.get("nodeMonitorStats", None)
                    else None
                ),
                online=rep["online"],
                uptime_stats=(
                    representatives_types.UptimeStats(
                        last_outage=(
                            representatives_types.Outage(
                                offline_unix_timestamp=rep["uptimeStats"]["lastOutage"].get(
                                    "offlineUnixTimestamp", None
                                ),
                                offline_date=rep["uptimeStats"]["lastOutage"].get("offlineDate", None),
                                online_unix_timestamp=rep["uptimeStats"]["lastOutage"].get("onlineUnixTimestamp", None),
                                online_date=rep["uptimeStats"]["lastOutage"].get("onlineDate", None),
                                duration_minutes=rep["uptimeStats"]["lastOutage"].get("durationMinutes", None),
                            )
                            if rep["uptimeStats"].get("lastOutage", None)
                            else None
                        ),
                        ping_stats=rep["uptimeStats"].get("pingStats", None),
                        tracking_start_date=rep["uptimeStats"]["trackingStartDate"],
                        tracking_start_unix_timestamp=rep["uptimeStats"]["trackingStartUnixTimestamp"],
                        uptime_percentages=representatives_types.UptimePercentages(
                            day=rep["uptimeStats"]["uptimePercentages"]["day"],
                            week=rep["uptimeStats"]["uptimePercentages"]["week"],
                            month=rep["uptimeStats"]["uptimePercentages"]["month"],
                            semi_annual=rep["uptimeStats"]["uptimePercentages"]["semiAnnual"],
                            year=rep["uptimeStats"]["uptimePercentages"]["year"],
                        ),
                    )
                    if rep.get("uptimeStats", None)
                    else None
                ),
                weight=rep["weight"],
            )
            for rep in reps
        ]

    def get_scores(self) -> list[representatives_types.Score]:
        """https://spyglass-api.web.app/representatives/scores"""
        response = get(f"{self._representatives_url}scores")
        if not response.ok:
            raise SpyglassException(response.json())

        scores = response.json()
        return [
            representatives_types.Score(
                address=score["address"],
                alias=score.get("alias", None),
                monitor_stats=(
                    representatives_types.MonitorStats(
                        has_above_avg_cemented_blocks=score["monitorStats"]["hasAboveAvgCementedBlocks"],
                        has_below_avg_unchecked_blocks=score["monitorStats"]["hasBelowAvgUncheckedBlocks"],
                        has_min_memory_requirement=score["monitorStats"]["hasMinMemoryRequirement"],
                        name=score["monitorStats"]["name"],
                    )
                    if score.get("monitorStats", None)
                    else None
                ),
                online=score["online"],
                principal=score["principal"],
                score=score["score"],
                uptime_percentages=(
                    representatives_types.UptimePercentages(
                        day=score["uptimePercentages"]["day"],
                        week=score["uptimePercentages"]["week"],
                        month=score["uptimePercentages"]["month"],
                        semi_annual=score["uptimePercentages"]["semiAnnual"],
                        year=score["uptimePercentages"]["year"],
                    )
                    if score.get("uptimePercentages", None)
                    else None
                ),
                weight=score["weight"],
                weight_percentage=score["weightPercentage"],
            )
            for score in scores
        ]

    def get_uptime(self, representatives: list[str], include_pings: bool = None) -> list[representatives_types.Uptime]:
        """https://spyglass-api.web.app/representatives/uptime"""
        data = {"includePings": include_pings, "representatives": representatives}
        response = post(f"{self._representatives_url}uptime", json=data)
        if not response.ok:
            raise SpyglassException(response.json())

        reps = response.json()

        return [
            representatives_types.Uptime(
                address=rep["address"],
                last_outage=(
                    representatives_types.Outage(
                        offline_unix_timestamp=rep["lastOutage"].get("offlineUnixTimestamp", None),
                        offline_date=rep["lastOutage"].get("offlineDate", None),
                        online_unix_timestamp=rep["lastOutage"].get("onlineUnixTimestamp", None),
                        online_date=rep["lastOutage"].get("onlineDate", None),
                        duration_minutes=rep["lastOutage"].get("durationMinutes", None),
                    )
                    if rep.get("lastOutage", None)
                    else None
                ),
                online=rep["online"],
                ping_stats=rep.get("pingStats", None),
                tracking_start_date=rep["trackingStartDate"],
                tracking_start_unix_timestamp=rep["trackingStartUnixTimestamp"],
                uptime_percentages=representatives_types.UptimePercentages(
                    day=rep["uptimePercentages"]["day"],
                    week=rep["uptimePercentages"]["week"],
                    month=rep["uptimePercentages"]["month"],
                    semi_annual=rep["uptimePercentages"]["semiAnnual"],
                    year=rep["uptimePercentages"]["year"],
                ),
            )
            for rep in reps
        ]
