'''
file:   test_felonystatemahine
author: Keith Helsabeck

This is the file for testing FelonyStatemachine (using pytest).
Run tests with: "pytest --cov=src --cov-report term-missing"
________________________________________________________________________
'''
import pytest
from datetime import date, datetime, timedelta
import typing
import uuid

from src.FelonyStatemachine import *
from src.collections import Charge_Collection
from src.crime import Crime
from src.charge import Charge


@pytest.fixture
def level1_onepoint(ch1_larc1: object) -> object:
    '''
    This represents a low-level criminal with 1 point for felonies 
    (expected value is Level 1).
    
    PARAMETERS:
    ____________________________________________________________________
    :ch1_larc1: a Charge instance with 1 pt

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection instance with 1 cl 1 Misd (1 pt)
    :rtype: ChargeCollection
    '''
    level1_onepoint = Charge_Collection()
    level1_onepoint.add_charge(ch1_larc1)
    return level1_onepoint

@pytest.fixture
def level1_1pt_withclone(
    ch1_larc1: object, 
    ch_clone_larc1: object
    ) -> object:
    '''
    This represents a low-level criminal with 1 point for felonies 
    (expected value is Level 1). There are two convicted charges on
    the same date, which should only be one point.

    PARAMETERS:
    ____________________________________________________________________
    :ch1_larc1: a Charge instance with 1 pt
    :ch_clone_larc1: a Charge instance with 1 pt (same date though)

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection instance with 1 cl 1 Misd (1 pt)
    :rtype: ChargeCollection
    '''
    level1_1pt_withclone = Charge_Collection()
    level1_1pt_withclone.add_charge(ch1_larc1)
    level1_1pt_withclone.add_charge(ch_clone_larc1)
    return level1_1pt_withclone

@pytest.fixture
def level1_0points(ch3_cl2_0pt: object) -> object:
    '''
    This represents a low-level criminal with 0 point for felonies 
    (expected value is Level 1). Anything below class 1 cannot be a
    felony point, and this is a level 2 misdemeanor.
    
    PARAMETERS:
    ____________________________________________________________________
    :ch3_cl2_0pt: a Charge instance with 0 pts (class 2 is too low)

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection instance with 1 cl 2 Misd (0 pts)
    :rtype: ChargeCollection
    '''
    level1_0points = Charge_Collection()
    level1_0points.add_charge(ch3_cl2_0pt)
    return level1_0points

@pytest.fixture
def level2_2points(ch1_larc1: object, ch2_aof_1pt: object) -> object:
    '''
    This represents a Level 2 record with 1 class 1 misd & 1 cl A1 
    misd for 2 points.
    
    PARAMETERS:
    ____________________________________________________________________
    :ch1_larc1: a Charge instance with 1 pt (larceny--cl 1)
    :ch2_aof_1pt: a Charge instance with 1 pt (aof--cl A1)

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection with 2 different date misdems (2 pts)
    :rtype: ChargeCollection
    '''
    level2_2points = Charge_Collection()
    level2_2points.add_charge(ch1_larc1)
    level2_2points.add_charge(ch2_aof_1pt)
    return level2_2points

@pytest.fixture
def level2_4pts_edges(
    charge_edge1: object, 
    charge_edge2: object, 
    charge_edge3: object, 
    charge_edge4: object
    ) -> object:
    '''
    This represents a Level 2 record with 4 pts from the edge case
    Chapter 20 statutes (driving charges).

    PARAMETERS:
    ____________________________________________________________________
    :charge_edge1: a Charge instance with 1 pt from chap 20
    :charge_edge2: a Charge instance with 1 pt from chap 20
    :charge_edge3: a Charge instance with 1 pt from chap 20
    :charge_edge4: a Charge instance with 1 pt from chap 20

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection with 4 f-pt misdems (4 pts, level 2)
    :rtype: ChargeCollection
    '''
    level2_4pts_edges = Charge_Collection()
    level2_4pts_edges.add_charge(charge_edge1)
    level2_4pts_edges.add_charge(charge_edge2)
    level2_4pts_edges.add_charge(charge_edge3)
    level2_4pts_edges.add_charge(charge_edge4)
    return level2_4pts_edges

@pytest.fixture
def level2_5points(
    ch1_larc1: object, 
    ch2_aof_1pt: object, 
    ch4_cl1_1pt: object, 
    ch5_larcH_2pt: object
    ) -> object:
    '''
    This represents a Level 2 record with 5 pts (lev 3 is 6).

    PARAMETERS:
    ____________________________________________________________________
    :ch1_larc1: a Charge instance with 1 pt (M larceny)
    :ch2_aof_1pt: a Charge instance with 1 pt (aof)
    :ch4_cl1_1pt: a Charge instance with 1 pt
    :ch5_larcH_2pt: a Charge instance with 2 pts (F larceny)

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection with 5 points (lev 3 is 6)
    :rtype: ChargeCollection
    '''
    level2_5points = Charge_Collection()
    level2_5points.add_charge(ch1_larc1)
    level2_5points.add_charge(ch2_aof_1pt)
    level2_5points.add_charge(ch4_cl1_1pt)
    level2_5points.add_charge(ch5_larcH_2pt)
    return level2_5points

@pytest.fixture
def level3_6points(
    ch5_larcH_2pt: object, 
    charge_hackG: object
    ) -> object:
    '''This represents a Level 3 record with 1 class H & 1 cl G 
    felony (6 pts, lev 3).

    PARAMETERS:
    ____________________________________________________________________
    :ch5_larcH_2pt: a Charge instance with 2 pts (F larceny)
    :charge_hackG: a Charge instance with 4 pts (Hack telecoms--G Felo)

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection with 6 f-pt (lev 3 starts at 6 pts)
    :rtype: ChargeCollection
    '''
    level3_6points = Charge_Collection()
    level3_6points.add_charge(ch5_larcH_2pt)
    level3_6points.add_charge(charge_hackG)
    return level3_6points

@pytest.fixture
def level3_9points(
    charge_hackG: object, 
    ch1_larc1: object, 
    ch5_larcH_2pt: object,
    charge_methI: object
    ) -> object:
    '''
    This represents a Level 3 record with 1 class G 
    felony (4 pts), a class 1 misdemeanor (1 pt), an H (2), and
    an I(2 pts).

    PARAMETERS:
    ____________________________________________________________________
    :charge_hackG: a Charge instance with 4 pts (Hack telecoms--G Felo)
    :ch1_larc1: a Charge instance with 1 pt (M larceny--cl 1)
    :ch5_larcH_2pt: a Charge instance with 2 pts (F larceny)
    :charge_methI: a Charge instance with 2 pts (F meth--cl I)

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection with 9 f-pts (lev 4 starts at 10 pts)
    :rtype: ChargeCollection
    '''
    level3_9points = Charge_Collection()
    level3_9points.add_charge(ch5_larcH_2pt)
    level3_9points.add_charge(ch1_larc1)
    level3_9points.add_charge(charge_hackG)
    level3_9points.add_charge(charge_methI)
    return level3_9points

@pytest.fixture
def level4_10points(
    charge_hackG: object, 
    charge_robD:object
    ) -> object:
    '''
    This represents a Level 4 record with 10 pts. 

    PARAMETERS:
    ____________________________________________________________________
    :charge_hackG: a Charge instance with 4 pts (Hack telecoms--G Felo)
    :charge_robD: a Charge instance with 6 pts (robbery--D Felo)

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection with 10 f-pts (lev 4 starts at 10 pts)
    :rtype: ChargeCollection
    '''
    level4_10points = Charge_Collection()
    level4_10points.add_charge(charge_hackG)
    level4_10points.add_charge(charge_robD)
    return level4_10points

@pytest.fixture
def level4_13points(
    charge_hackG: object, 
    charge_robD:object, 
    ch5_larcH_2pt: object,
    ch1_larc1: object
    ) -> object:
    '''
    This represents a Level 4 record with 13 pts. 

    PARAMETERS:
    ____________________________________________________________________
    :charge_hackG: a Charge instance with 4 pts (Hack telecoms--G Felo)
    :charge_robD: a Charge instance with 6 pts (robbery--D Felo)
    :ch5_larcH_2pt: a Charge instance with 2 pts (F larceny)
    :ch1_larc1: a Charge instance with 1 pt (M larceny--cl 1)

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection with 13 f-pts (lev 5 starts at 14 pts)
    :rtype: ChargeCollection
    '''
    level4_13points = Charge_Collection()
    level4_13points.add_charge(charge_hackG)
    level4_13points.add_charge(charge_robD)
    level4_13points.add_charge(ch5_larcH_2pt)
    level4_13points.add_charge(ch1_larc1)
    return level4_13points

@pytest.fixture
def level5_14points(
    charge_hackG: object, 
    charge_robD:object, 
    ch5_larcH_2pt: object,
    ch1_larc1: object,
    ch2_aof_1pt: object
    ) -> object:
    '''This represents a Level 5 record with 14 pts. 
        
    PARAMETERS:
    ____________________________________________________________________
    :charge_hackG: a Charge instance with 4 pts (Hack telecoms--G Felo)
    :charge_robD: a Charge instance with 6 pts (robbery--D Felo)
    :ch5_larcH_2pt: a Charge instance with 2 pts (F larceny)
    :ch1_larc1: a Charge instance with 1 pt (M larceny--cl 1)
    :ch2_aof_1pt: a Charge instance with 1 pt (M aof--cl A1)

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection with 14 f-pts (lev 5 starts at 14 pts)
    :rtype: ChargeCollection
    '''
    level5_14points = Charge_Collection()
    level5_14points.add_charge(charge_hackG)
    level5_14points.add_charge(charge_robD)
    level5_14points.add_charge(ch5_larcH_2pt)
    level5_14points.add_charge(ch1_larc1)
    level5_14points.add_charge(ch2_aof_1pt)
    return level5_14points

@pytest.fixture
def level5_17points(
    ch1_larc1: object,
    charge_hackG: object, 
    charge_robD:object, 
    charge_murd2_B2: object
    ) -> object:
    '''
    This represents a Level 5 record with 17 pts. 

    PARAMETERS:
    ____________________________________________________________________
    :ch1_larc1: a Charge instance with 1 pt (M larceny--cl 1)
    :charge_hackG: a Charge instance with 4 pts (Hack telecoms--G Felo)
    :charge_robD: a Charge instance with 6 pts (robbery--D Felo)
    :charge_murd2_B2: a Charge instance with 6 pts (Murder2--B2 Felo)

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection with 17 f-pts (lev 6 starts at 18 pts)
    :rtype: ChargeCollection
    '''
    level5_17points = Charge_Collection()
    level5_17points.add_charge(ch1_larc1)
    level5_17points.add_charge(charge_hackG)
    level5_17points.add_charge(charge_robD)
    level5_17points.add_charge(charge_murd2_B2)
    return level5_17points

@pytest.fixture
def level6_18points(
    charge_murd1_a10: object,
    charge_robD: object, 
    ch5_larcH_2pt: object
    ) -> object:
    '''
    This represents a Level 6 record with 18 pts. 

    PARAMETERS:
    ____________________________________________________________________
    :charge_murd1_a10: a Charge instance worth 10 pts (Murder1--A Felo)
    :charge_robD: a Charge instance with 6 pts (robbery--D Felo)
    :ch5_larcH_2pt: a Charge instance with 2 pts (F larceny)

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection with 18 f-pts (lev 6 starts at 18 pts)
    :rtype: ChargeCollection
    '''
    level6_18points = Charge_Collection()
    level6_18points.add_charge(charge_murd1_a10)
    level6_18points.add_charge(charge_robD)
    level6_18points.add_charge(ch5_larcH_2pt)
    return level6_18points

def test_initialization():
    '''This tests an initialization of a Felony_RecordMachine.'''
    felofsm = Felony_RecordMachine()
    assert StartState == type(felofsm.state)
    assert 0 == felofsm.points
    assert 1 == felofsm.level
    assert 0 == felofsm.state.index

def test_recordlevel1(level1_onepoint: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level1_onepoint as a fixture (record lv 1, 1 pt) and 
    confirms the fsm runs it and returns the correct values.

    PARAMETERS:
    ____________________________________________________________________
    :level1_onepoint: a conviction collection -- level 1 w 1 point
    '''
    felofsm = Felony_RecordMachine()
    felofsm.on_event(level1_onepoint)
    assert FinishedState == type(felofsm.state)
    assert 1 == felofsm.points
    assert 1 == felofsm.level

def test_recolev1_samedate(level1_1pt_withclone: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level1_1pt_withclone as a fixture (record lv 1, 1 pt), 
    and confirms that two class 1 misdemeanors on the same date only 
    calculate one point.

    PARAMETERS:
    ____________________________________________________________________
    :level1_1pt_withclone: a conviction collection -- level 1 w 1 point
    '''
    felofsm = Felony_RecordMachine()
    felofsm.on_event(level1_1pt_withclone)
    assert FinishedState == type(felofsm.state)
    assert 1 == felofsm.points
    assert 1 == felofsm.level

def test_recordlevel1_nopts(level1_0points: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level1_0points as a fixture (record lv 1, 0 pts) and 
    confirms the fsm runs it and returns the correct values.

    PARAMETERS:
    ____________________________________________________________________
    :level1_0points: a conviction collection -- level 1 w 0 pts
    '''
    felofsm = Felony_RecordMachine()
    felofsm.on_event(level1_0points)
    assert FinishedState == type(felofsm.state)
    assert 0 == felofsm.points
    assert 1 == felofsm.level

def test_recordlevel2_2pts(level2_2points: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level2_2points as a fixture (record lv 2, 2 pts) and 
    confirms the fsm runs it and returns the correct values.

    PARAMETERS:
    ____________________________________________________________________
    :level2_2points: a conviction collection -- level 2 w 2 pts
    '''
    felofsm = Felony_RecordMachine()

    felofsm.on_event(level2_2points)
    assert FinishedState == type(felofsm.state)
    assert 2 == felofsm.points
    assert 2 == felofsm.level

def test_level2_4pts_edges(level2_4pts_edges: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level2_4pts_edges as a fixture (record lv 2, 4 pts) and 
    confirms the fsm runs it and returns the correct values. Here, we 
    specifically test the edge cases from Chapter 20 (vehicle statutes)

    PARAMETERS:
    ____________________________________________________________________
    :level2_4pts_edges: conviction collection -- lev 2 w 4 (edge cases)
    '''
    felofsm = Felony_RecordMachine()

    felofsm.on_event(level2_4pts_edges)
    assert FinishedState == type(felofsm.state)
    assert 4 == felofsm.points
    assert 2 == felofsm.level

def test_recordlevel2_5pts(level2_5points: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level2_5points as a fixture (record lv 2, 5 pts) and 
    confirms the fsm runs it and returns the correct values.

    PARAMETERS:
    ____________________________________________________________________
    :level2_5points: a conviction collection -- level 2 w 5 pts
    '''
    felofsm = Felony_RecordMachine()

    felofsm.on_event(level2_5points)
    assert FinishedState == type(felofsm.state)
    assert 5 == felofsm.points
    assert 2 == felofsm.level

def test_recordlevel3_6pts(level3_6points: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level3_6points as a fixture (record lv 3, 6 pts) and 
    confirms the fsm runs it and returns the correct values.

    PARAMETERS:
    ____________________________________________________________________
    :level3_6points: a conviction collection -- level 3 w 6 pts
    '''
    felofsm = Felony_RecordMachine()

    felofsm.on_event(level3_6points)
    assert FinishedState == type(felofsm.state)
    assert 6 == felofsm.points
    assert 3 == felofsm.level    

def test_recordlevel3_9pts(level3_9points: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level3_9points as a fixture (record lv 3, 9 pts) and 
    confirms the fsm runs it and returns the correct values.

    PARAMETERS:
    ____________________________________________________________________
    :level3_9points: a conviction collection -- level 3 w 9 pts
    '''
    felofsm = Felony_RecordMachine()

    felofsm.on_event(level3_9points)
    assert FinishedState == type(felofsm.state)
    assert 9 == felofsm.points
    assert 3 == felofsm.level

def test_recordlevel4_10pts(level4_10points: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level4_10points as a fixture (record lv 4, 10 pts) and 
    confirms the fsm runs it and returns the correct values.

    PARAMETERS:
    ____________________________________________________________________
    :level4_10points: a conviction collection -- level 4 w 10 pts
    '''
    felofsm = Felony_RecordMachine()

    felofsm.on_event(level4_10points)
    assert FinishedState == type(felofsm.state)
    assert 10 == felofsm.points
    assert 4 == felofsm.level


def test_recordlevel4_13pts(level4_13points: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level4_13points as a fixture (record lv 4, 13 pts) and 
    confirms the fsm runs it and returns the correct values.

    PARAMETERS:
    ____________________________________________________________________
    :level4_13points: a conviction collection -- level 4 w 13 pts
    '''
    felofsm = Felony_RecordMachine()

    felofsm.on_event(level4_13points)
    assert FinishedState == type(felofsm.state)
    assert 13 == felofsm.points
    assert 4 == felofsm.level

def test_recordlevel5_14pts(level5_14points: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level5_14points as a fixture (record lv 5, 14 pts) and 
    confirms the fsm runs it and returns the correct values.

    PARAMETERS:
    ____________________________________________________________________
    :level5_14points: a conviction collection -- level 5 w 14 pts
    '''
    felofsm = Felony_RecordMachine()

    felofsm.on_event(level5_14points)
    assert FinishedState == type(felofsm.state)
    assert 14 == felofsm.points
    assert 5 == felofsm.level

def test_recordlevel5_17pts(level5_17points: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level5_17points as a fixture (record lv 5, 17 pts) and 
    confirms the fsm runs it and returns the correct values.

    PARAMETERS:
    ____________________________________________________________________
    :level5_17points: a conviction collection -- level 5 w 17 pts
    '''
    felofsm = Felony_RecordMachine()

    felofsm.on_event(level5_17points)
    assert FinishedState == type(felofsm.state)
    assert 17 == felofsm.points
    assert 5 == felofsm.level


def test_recordlevel6_18pts(level6_18points: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level6_18points as a fixture (record lv 6, 18 pts) and 
    confirms the fsm runs it and returns the correct values.

    PARAMETERS:
    ____________________________________________________________________
    :level6_18points: a conviction collection -- level 6 w 18 pts
    '''
    felofsm = Felony_RecordMachine()

    felofsm.on_event(level6_18points)
    assert FinishedState == type(felofsm.state)
    assert 18 == felofsm.points
    assert 6 == felofsm.level

def test_basestate():
    '''
    WHITE BOX TEST:
    ____________________________________________________________________
    This is a test of the base state and its methods and returns.
    '''
    base = State()
    colx = Charge_Collection()
    assert 0 == base.on_event(colx, 0, 0)
    assert "State" == str(base)
    assert "State" == repr(base)

def test_startstate():
    '''
    WHITE BOX TEST:
    ____________________________________________________________________
    This is a test of the start state and its methods and returns.
    '''
    start = StartState()
    colx = Charge_Collection()
    assert FinishedState == type(start.on_event(colx, 0, 0))
