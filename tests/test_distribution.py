from pyglass.distribution import (
    get_buckets,
    get_burn,
    get_developer_funds,
    get_rich_list,
    get_rich_list_snapshot,
    get_supply,
)
from time import sleep

from .dataclass_type_check import check


def test_buckets():
    sleep(2)
    subject = get_buckets()
    check(subject)


def test_burn():
    sleep(2)
    subject = get_burn()
    check(subject)


def test_developer_funds():
    sleep(2)
    subject = get_developer_funds()
    check(subject)


def test_rich_list():
    sleep(2)
    rich_list = get_rich_list(True, 0, 420)
    assert len(rich_list) == 420
    for subject in rich_list:
        check(subject)


def test_rich_list_snapshot():
    sleep(2)
    rich_list = get_rich_list_snapshot()
    assert len(rich_list)
    for subject in rich_list:
        check(subject)


def test_supply():
    sleep(2)
    subject = get_supply()
    check(subject)
