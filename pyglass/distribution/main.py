from requests import get, post

from pyglass.distribution import distribution_types
from pyglass.exceptions import SpyglassException


class Distribution:
    def __init__(self, base_url: str) -> None:
        self._distribution_url = f"{base_url}/v1/distribution/"

    def get_burn(self) -> distribution_types.Burn:
        """https://spyglass-api.web.app/distribution/burn"""
        response = get(f"{self._distribution_url}burn")
        if not response.ok:
            raise SpyglassException(response.json())

        burn = response.json()
        return distribution_types.Burn(
            total_amount=burn["totalAmount"],
            burn_accounts=[
                distribution_types.BurnAccount(address=burn_account["address"], pending=burn_account["pending"])
                for burn_account in burn["burnAccounts"]
            ],
        )

    def get_buckets(self) -> distribution_types.Buckets:
        """https://spyglass-api.web.app/distribution/buckets"""
        response = get(f"{self._distribution_url}buckets")
        if not response.ok:
            raise SpyglassException(response.json())

        buckets = response.json()
        return distribution_types.Buckets(
            number0_0001=buckets["number0_0001"],
            number0_001=buckets["number0_001"],
            number0_01=buckets["number0_01"],
            number0_1=buckets["number0_1"],
            number1=buckets["number1"],
            number10=buckets["number10"],
            number100=buckets["number100"],
            number100_000=buckets["number100_000"],
            number100_000_000=buckets["number100_000_000"],
            number10_000=buckets["number10_000"],
            number10_000_000=buckets["number10_000_000"],
            number1_000=buckets["number1_000"],
            number1_000_000=buckets["number1_000_000"],
            total_accounts=buckets["totalAccounts"],
        )

    def get_developer_funds(self) -> distribution_types.DeveloperFunds:
        """https://spyglass-api.web.app/distribution/developer-funds"""
        response = get(f"{self._distribution_url}developer-funds")
        if not response.ok:
            raise SpyglassException(response.json())

        dev_funds = response.json()
        return distribution_types.DeveloperFunds(
            total_balance=dev_funds["totalBalance"],
            wallets=[
                distribution_types.DeveloperWallet(address=wallet["address"], balance=wallet["balance"])
                for wallet in dev_funds["wallets"]
            ],
        )

    def get_rich_list(
        self, include_representative: bool = False, offset: int = 0, size: int = 50
    ) -> list[distribution_types.RichListItem]:
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
        response = post(f"{self._distribution_url}rich-list", json=data)
        if not response.ok:
            raise SpyglassException(response.json())

        rich_list: list[dict] = response.json()
        return [
            distribution_types.RichListItem(
                address=item["address"],
                amount=item["amount"],
                representative=item.get("representative", None),
            )
            for item in rich_list
        ]

    def get_rich_list_snapshot(self) -> list[distribution_types.RichListItem]:
        """https://spyglass-api.web.app/distribution/rich-list-snapshot"""
        response = get(f"{self._distribution_url}rich-list-snapshot")
        if not response.ok:
            raise SpyglassException(response.json())

        rich_list: list[dict] = response.json()
        return [
            distribution_types.RichListItem(
                address=item["address"],
                amount=item["amount"],
                representative=item.get("representative", None),
            )
            for item in rich_list
        ]

    def get_supply(self) -> distribution_types.Supply:
        """https://spyglass-api.web.app/distribution/supply"""
        response = get(f"{self._distribution_url}supply")
        if not response.ok:
            raise SpyglassException(response.json())

        supply: dict = response.json()
        return distribution_types.Supply(
            burned_amount=supply["burnedAmount"],
            circulating_amount=supply["circulatingAmount"],
            circulating_percent=supply["circulatingPercent"],
            dev_fund_amount=supply["devFundAmount"],
            dev_fund_percent=supply["devFundPercent"],
            total_amount=supply["totalAmount"],
        )
