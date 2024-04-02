from time import sleep

from pyglass import PyglassClient
from tests.dataclass_type_check import check

client = PyglassClient("https://api.spyglass.eule.wtf/banano")


def test_accounts():
    sleep(2)
    for subject in client.known.get_accounts(True, True):
        check(subject)
    sleep(2)
    for subject in client.known.get_accounts():
        check(subject)


def test_vanities():
    for subject in client.known.get_vanities():
        assert isinstance(subject, str)
