import pytest
import sys
sys.path.append("..")
from class_clock import *
from Normal_Clock import *

def test_NormalClock_1():
    Clock_1 = Normal_Clock(12,50,11)
    Clock_1.Tick()
    assert Clock_1.show() == "12:50:12"

def test_NormalClock_2():
    Clock_2 = Normal_Clock(12,50,0)
    Clock_2.Tick()
    assert Clock_2.show() == "12:50:01"

def test_NormalClock_3():
    Clock_3 = Normal_Clock(12,50,59)
    Clock_3.Tick()
    assert Clock_3.show() == "12:51:00"

def test_NormalClock_4():
    Clock_4 = Normal_Clock(23,59,59)
    Clock_4.Tick()
    assert Clock_4.show() == "00:00:00"
