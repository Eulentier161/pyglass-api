from requests import get, post

from .distribution_types import Buckets, Burn, DeveloperFunds, RichListItem, Supply

distribution_url = "https://api.spyglass.pw/banano/v1/distribution/"


def get_burn() -> Burn:
    request = get(f"{distribution_url}burn")
    return Burn(request.json())


def get_buckets() -> Buckets:
    request = get(f"{distribution_url}buckets")
    return Buckets(request.json())


def get_developer_funds() -> DeveloperFunds:
    request = get(f"{distribution_url}developer-funds")
    return DeveloperFunds(request.json())


def get_rich_list(
    include_representative: bool = False, offset: int = 0, size: int = 50
) -> list[RichListItem]:
    """
    `include_representative`: Optionally include the representative for each account.\n
    `offset`: Number of accounts to skip before returning results; used for pagination.\n
    `size`: Number of records to return, with a default of 50 and max of 500.
    """
    data = {
        "includeRepresentative": include_representative,
        "offset": offset,
        "size": size,
    }
    request = post(f"{distribution_url}rich-list", json=data)
    return [RichListItem(item) for item in request.json()]


def get_rich_list_snapshot() -> list[RichListItem]:
    request = get(f"{distribution_url}rich-list-snapshot")
    return [RichListItem(item) for item in request.json()]


def get_supply() -> Supply:
    request = get(f"{distribution_url}supply")
    return Supply(request.json())
