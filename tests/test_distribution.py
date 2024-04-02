from time import sleep

from pyglass import PyglassClient
from tests.dataclass_type_check import check

client = PyglassClient("https://api.spyglass.eule.wtf/banano")


def test_buckets():
    sleep(2)
    subject = client.distribution.get_buckets()
    check(subject)


def test_burn():
    sleep(2)
    subject = client.distribution.get_burn()
    check(subject)


def test_developer_funds():
    sleep(2)
    subject = client.distribution.get_developer_funds()
    check(subject)


def test_rich_list():
    sleep(2)
    rich_list = client.distribution.get_rich_list(True, 0, 420)
    assert len(rich_list) == 420
    for subject in rich_list:
        check(subject)


def test_rich_list_snapshot():
    sleep(2)
    rich_list = client.distribution.get_rich_list_snapshot()
    assert len(rich_list)
    for subject in rich_list:
        check(subject)


def test_supply():
    sleep(2)
    subject = client.distribution.get_supply()
    check(subject)
