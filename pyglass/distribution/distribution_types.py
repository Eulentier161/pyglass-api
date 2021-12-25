from typing import Optional


class BurnAccount:
    def __init__(self, burn_account: dict) -> None:
        self.address: str = burn_account["address"]
        self.pending: int = burn_account["pending"]


class Burn:
    def __init__(self, request: dict) -> None:
        self.total_amount: int = request["totalAmount"]
        self.burn_accounts: list[BurnAccount] = [
            BurnAccount(burn_account) for burn_account in request["burnAccounts"]
        ]


class Buckets:
    def __init__(self, request: dict) -> None:
        self.number0_0001: int = request["number0_0001"]
        self.number0_001: int = request["number0_001"]
        self.number0_01: int = request["number0_01"]
        self.number0_1: int = request["number0_1"]
        self.number1: int = request["number1"]
        self.number10: int = request["number10"]
        self.number100: int = request["number100"]
        self.number100_000: int = request["number100_000"]
        self.number100_000_000: int = request["number100_000_000"]
        self.number10_000: int = request["number10_000"]
        self.number10_000_000: int = request["number10_000_000"]
        self.number1_000: int = request["number1_000"]
        self.number1_000_000: int = request["number1_000_000"]
        self.total_accounts: int = request["totalAccounts"]


class DeveloperWallet:
    def __init__(self, wallet: dict) -> None:
        self.address: str = wallet["address"]
        self.balance: int = wallet["balance"]


class DeveloperFunds:
    def __init__(self, request: dict) -> None:
        self.total_balance: int = request["totalBalance"]
        self.wallets: list[DeveloperWallet] = [
            DeveloperWallet(wallet) for wallet in request["wallets"]
        ]


class RichListItem:
    def __init__(self, request: dict) -> None:
        self.address: str = request["address"]
        self.amount: float = request["amount"]
        self.representative: Optional[str] = request.get("representative", None)


class Supply:
    def __init__(self, request: dict) -> None:
        self.burned_amount: int = request["burnedAmount"]
        self.circulating_amount: int = request["circulatingAmount"]
        self.circulating_percent: float = request["circulatingPercent"]
        self.dev_fund_amount: int = request["devFundAmount"]
        self.dev_fund_percent: float = request["devFundPercent"]
        self.total_amount: int = request["totalAmount"]
