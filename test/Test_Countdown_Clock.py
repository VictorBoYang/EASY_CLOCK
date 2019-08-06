import pytest
import sys
sys.path.append("..")
from class_clock import *
from Countdown_Clock import *

def test_CountdownClock_1():
    Clock_1 = Countdown_Clock(12,50,11)
    Clock_1.Tick()
    assert Clock_1.show() == "12:50:10"

def test_CountdownClock_2():
    Clock_2 = Countdown_Clock(12,50,1)
    Clock_2.Tick()
    assert Clock_2.show() == "12:50:00"

def test_CountdownClock_3():
    Clock_3 = Countdown_Clock(12,0,0)
    Clock_3.Tick()
    assert Clock_3.show() == "11:59:59"

def test_CountdownClock_4():
    Clock_4 = Countdown_Clock(0,0,0)
    Clock_4.Tick()
    assert Clock_4.show() == "00:00:00"
