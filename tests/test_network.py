from time import sleep

from pyglass import PyglassClient
from tests.dataclass_type_check import check

client = PyglassClient("https://api.spyglass.eule.wtf/banano")


def test_ledger_size():
    sleep(2)
    subject = client.network.get_ledger_size()
    assert isinstance(subject, (int, float))


def test_nakamoto_coefficient():
    sleep(2)
    subject = client.network.get_nakamoto_coefficient()
    check(subject)


def test_peer_versions():
    sleep(2)
    for subject in client.network.get_peer_versions():
        check(subject)


def test_quorum():
    sleep(2)
    subject = client.network.get_quorum()
    check(subject)
