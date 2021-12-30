from time import sleep

from pyglass.network import (
    get_ledger_size,
    get_nakamoto_coefficient,
    get_peer_versions,
    get_quorum,
)

from .dataclass_type_check import check


def test_ledger_size():
    sleep(2)
    subject = get_ledger_size()
    assert isinstance(subject, (int, float))


def test_nakamoto_coefficient():
    sleep(2)
    subject = get_nakamoto_coefficient()
    check(subject)


def test_peer_versions():
    sleep(2)
    for subject in get_peer_versions():
        check(subject)


def test_quorum():
    sleep(2)
    subject = get_quorum()
    check(subject)
