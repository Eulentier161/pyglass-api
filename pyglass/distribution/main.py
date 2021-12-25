from requests import get, post

from .distribution_types import Buckets, Burn, DeveloperFunds, RichListItem, Supply

DISTRIBUTION_URL = "https://api.spyglass.pw/banano/v1/distribution/"


def get_burn() -> Burn:
    """https://spyglass-api.web.app/distribution/burn"""
    request = get(f"{DISTRIBUTION_URL}burn")
    return Burn(request.json())


def get_buckets() -> Buckets:
    """https://spyglass-api.web.app/distribution/buckets"""
    request = get(f"{DISTRIBUTION_URL}buckets")
    return Buckets(request.json())


def get_developer_funds() -> DeveloperFunds:
    """https://spyglass-api.web.app/distribution/developer-funds"""
    request = get(f"{DISTRIBUTION_URL}developer-funds")
    return DeveloperFunds(request.json())


def get_rich_list(
    include_representative: bool = False, offset: int = 0, size: int = 50
) -> list[RichListItem]:
    """
    `include_representative`: Optionally include the representative for each account.\n
    `offset`: Number of accounts to skip before returning results; used for pagination.\n
    `size`: Number of records to return, with a default of 50 and max of 500.\n
    https://spyglass-api.web.app/distribution/rich-list
    """
    data = {
        "includeRepresentative": include_representative,
        "offset": offset,
        "size": size,
    }
    request = post(f"{DISTRIBUTION_URL}rich-list", json=data)
    return [RichListItem(item) for item in request.json()]


def get_rich_list_snapshot() -> list[RichListItem]:
    """https://spyglass-api.web.app/distribution/rich-list-snapshot"""
    request = get(f"{DISTRIBUTION_URL}rich-list-snapshot")
    return [RichListItem(item) for item in request.json()]


def get_supply() -> Supply:
    """https://spyglass-api.web.app/distribution/supply"""
    request = get(f"{DISTRIBUTION_URL}supply")
    return Supply(request.json())
