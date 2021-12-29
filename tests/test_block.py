from time import sleep

from pyglass import SpyglassException
from pyglass.block import get_block
from pytest import raises

from tests.dataclass_type_check import check

BLOCKS = [
    "AA189A6E06553FB55D915590D4137EF300A0B241E368A6F868C6A325003612BE",  # receive
    "E9CCCF14E52C303393A997EA1342090510856DED105D6046B14C67D838923F86",  # send
    "F435AB7C227C495C128EBA791EAA29F2594B327D5B65D607F2E1B310733CD31C",  # change
    "LmaoNotARealBlock123",  # nonsense
]


def test_block():
    for block in BLOCKS:
        sleep(2)
        if block != BLOCKS[-1]:
            subject = get_block(block)
            check(subject)
            check(subject.contents)
        else:
            with raises(SpyglassException):
                get_block(block)
