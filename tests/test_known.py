from time import sleep

from pyglass.known import get_accounts, get_vanities

from .dataclass_type_check import check


def test_accounts():
    sleep(2)
    for subject in get_accounts(True, True):
        check(subject)
    sleep(2)
    for subject in get_accounts():
        check(subject)


def test_vanities():
    for subject in get_vanities():
        assert isinstance(subject, str)
