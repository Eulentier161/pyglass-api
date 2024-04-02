from pyglass.account.main import Account
from pyglass.block.main import Block
from pyglass.distribution.main import Distribution
from pyglass.known.main import Known
from pyglass.network.main import Network
from pyglass.representatives.main import Representatives


class PyglassClient:
    def __init__(self, _base_url: str = "https://api.spyglass.pw/banano") -> None:
        _base_url = _base_url.rstrip("/")
        self.account = Account(_base_url)
        self.block = Block(_base_url)
        self.distribution = Distribution(_base_url)
        self.known = Known(_base_url)
        self.network = Network(_base_url)
        self.representatives = Representatives(_base_url)
