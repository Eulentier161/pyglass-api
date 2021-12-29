from pyglass.account import (
    get_confirmed_transactions,
    get_delegators,
    get_insights,
    get_overview,
    get_receivable_transactions,
    get_representative,
)
from pytest import raises
from pyglass import SpyglassException

from tests.dataclass_type_check import check

ADDRESSES = [
    "ban_1hootubxy68fhhrctjmaias148tz91tsse3pq1pgmfedsm3cubhobuihqnxd",
    "ban_1eu1enkjdd5wgf8sz7tq5xxbo5nqro4k4yz1o4tmk8bs5ejhu9f3yazmreo3",
    "ban_1burnbabyburndiscoinferno111111111111111111111111111aj49sw3w",
]


def test_overview():
    for addr in ADDRESSES:
        subject = get_overview(addr)
        check(subject)


def test_confirmed_tx():
    for addr in ADDRESSES:
        if addr != ADDRESSES[-1]:
            for subject in get_confirmed_transactions(addr):
                check(subject)
        else:
            with raises(SpyglassException):
                get_confirmed_transactions(addr)


def test_delegators():
    for addr in ADDRESSES:
        subject = get_delegators(addr)
        check(subject)


def test_insights():
    for addr in ADDRESSES:
        if addr != ADDRESSES[-1]:
            subject = get_insights(addr, include_height_balances=True)
            check(subject)
        else:
            with raises(SpyglassException):
                get_insights(addr, True)


def test_representative():
    for addr in ADDRESSES:
        if addr is not ADDRESSES[-1]:
            subject = get_representative(addr)
            assert isinstance(subject, str)
        else:
            with raises(SpyglassException):
                get_representative(addr)


def test_receivable_transactions():
    for addr in ADDRESSES:
        for subject in get_receivable_transactions(addr):
            check(subject)
