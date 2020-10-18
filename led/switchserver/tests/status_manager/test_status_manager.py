import pytest
from switchserver.status_manager.status_manager import StatusManager


def test_base():
    sm = StatusManager([("A", 0), ("B", 0), ("C", 0)])
    for k in ["A", "B", "C"]:
        assert sm.get_item(k) == 0
    sm.set_item("B", 3)
    assert sm.get_whole_status() == [("A", 0), ("B", 3), ("C", 0)]

