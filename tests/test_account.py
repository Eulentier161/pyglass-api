from time import sleep

from pytest import raises

from pyglass import PyglassClient
from pyglass.exceptions import SpyglassException
from tests.dataclass_type_check import check

ADDRESSES = [
    "ban_1hootubxy68fhhrctjmaias148tz91tsse3pq1pgmfedsm3cubhobuihqnxd",
    "ban_1eu1enkjdd5wgf8sz7tq5xxbo5nqro4k4yz1o4tmk8bs5ejhu9f3yazmreo3",
    "ban_1burnbabyburndiscoinferno111111111111111111111111111aj49sw3w",
]


client = PyglassClient("https://api.spyglass.eule.wtf/banano")


def test_overview():
    for addr in ADDRESSES:
        sleep(2)
        subject = client.account.get_overview(addr)
        check(subject)


def test_confirmed_tx():
    for addr in ADDRESSES:
        sleep(2)
        if addr != ADDRESSES[-1]:
            for subject in client.account.get_confirmed_transactions(addr):
                check(subject)
        else:
            with raises(SpyglassException):
                client.account.get_confirmed_transactions(addr)


def test_delegators():
    for addr in ADDRESSES:
        sleep(2)
        subject = client.account.get_delegators(addr)
        check(subject)
        for delegator in subject.delegators:
            check(delegator)


def test_insights():
    for addr in ADDRESSES:
        sleep(2)
        if addr != ADDRESSES[-1]:
            subject = client.account.get_insights(addr, include_height_balances=True)
            check(subject)
        else:
            with raises(SpyglassException):
                client.account.get_insights(addr, True)


def test_representative():
    for addr in ADDRESSES:
        sleep(2)
        if addr is not ADDRESSES[-1]:
            subject = client.account.get_representative(addr)
            assert isinstance(subject, str)
        else:
            with raises(SpyglassException):
                client.account.get_representative(addr)


def test_receivable_transactions():
    for addr in ADDRESSES:
        sleep(2)
        for subject in client.account.get_receivable_transactions(addr):
            check(subject)
