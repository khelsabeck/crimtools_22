'''
file:   test_misdemeanor_machine
author: Keith Helsabeck

This is the file for testing misdemeanor_machine (using pytest).
Run tests with: "pytest --cov=src --cov-report term-missing"
________________________________________________________________________
'''
import pytest
from datetime import date, datetime, timedelta
import typing

from src.misdemeanor_machine import *
from src.crime import Crime
from src.charge import Charge
from src.collections import Charge_Collection

@pytest.fixture
def rec_infraction(ch_infraction: object) -> object:
    '''
    This is a record with just one conviction (an infraction)
    (expected value is level 1 with 0 pts).
    
    PARAMETERS:
    ____________________________________________________________________
    :ch_infraction: a Charge instance worth 0 misd rec pts (infraction)

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection instance with 1 infraction (0 pts)
    :rtype: ChargeCollection
    '''
    rec_infraction = Charge_Collection()
    rec_infraction.add_charge(ch_infraction)
    return rec_infraction

@pytest.fixture
def level2_onepoint(ch1_larc1: object) -> object:
    '''
    This represents a low-level criminal with 1 point for misds 
    (expected value is Level 2).
    
    PARAMETERS:
    ____________________________________________________________________
    :ch1_larc1: a Charge instance with 1 pt

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection instance with 1 cl 1 Misd (1 pt)
    :rtype: ChargeCollection
    '''
    level2_onepoint = Charge_Collection()
    level2_onepoint.add_charge(ch1_larc1)
    return level2_onepoint

@pytest.fixture
def charge_methI(crime_meth_classI: object) -> object:
    '''This is a class I meth -- 1 misdemeanor points.
    
    PARAMETERS:
    ____________________________________________________________________
    :crime_meth_classI: a Crime instance w a class I Felo (1 pts)

    RETURN:
    ____________________________________________________________________
    :return: a Charge instance with a class I -- F Meth
    :rtype: Charge
    '''
    charge_methI = Charge()
    charge_methI.id = 15
    charge_methI.offense_date = date(2015, 1, 1)
    charge_methI.disposition_date = date(2015, 2, 2)
    charge_methI.crime = crime_meth_classI
    charge_methI.convicted = True
    return charge_methI

@pytest.fixture
def ch3_cl2_0pt(crime_assault2: object) -> object:
    '''
    This is a class 2 assault -- no felo points.

    PARAMETERS:
    ____________________________________________________________________
    :crime_assault2: a Crime instance w a class 2 misd (0 pts)

    RETURN:
    ____________________________________________________________________
    :return: a Charge instance with a class 2 -- 0 pts
    :rtype: Charge
    '''
    ch3_cl2_0pt = Charge()
    ch3_cl2_0pt.id = 3
    ch3_cl2_0pt.offense_date = date(2011, 1, 1)
    ch3_cl2_0pt.disposition_date = date(2012, 3, 3)
    ch3_cl2_0pt.crime = crime_assault2
    ch3_cl2_0pt.convicted = True
    return ch3_cl2_0pt


@pytest.fixture
def level2_1points(ch3_cl2_0pt: object) -> object:
    '''
    This represents a low-level criminal with just a class 3 misd'r.
    It should be worth one misdemeanor point.
    
    PARAMETERS:
    ____________________________________________________________________
    :ch3_cl2_0pt: a Charge instance with 0 pts (class 2 is too low)

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection instance with 1 cl 2 Misd (0 pts)
    :rtype: ChargeCollection
    '''
    level2_1points = Charge_Collection()
    level2_1points.add_charge(ch3_cl2_0pt)
    return level2_1points

@pytest.fixture
def ch1_larc1(crime_larceny1: object) -> object:
    '''
    This represents a class 1 larceny charge. 1 pt for misdems
    
    PARAMETERS:
    ____________________________________________________________________
    :crime_larceny1: a Crime instance w a class 1 larceny (1 point)

    RETURN:
    ____________________________________________________________________
    :returns: a Charge instance with a class 1 larceny
    :rtype: Charge
    '''
    ch1_larc1 = Charge()
    ch1_larc1.id = 1
    ch1_larc1.offense_date = date(2009,1, 1)
    ch1_larc1.disposition_date = date(2010,1, 1)
    ch1_larc1.crime = crime_larceny1
    ch1_larc1.convicted = True
    return ch1_larc1

@pytest.fixture
def ch2_aof_1pt(crime_aof: object) -> object:
    '''
    This is a class A1 AoF charge. 1 misd point
    
    PARAMETERS:
    ____________________________________________________________________
    :crime_aof: a Crime instance w a class A1 misd (AOF) (1 point)

    RETURN:
    ____________________________________________________________________
    :returns: a Charge instance with a class A1-- AOF
    :rtype: Charge
    '''
    ch2_aof_1pt = Charge()
    ch2_aof_1pt.id = 2
    ch2_aof_1pt.offense_date = date(2010,1, 2)
    ch2_aof_1pt.disposition_date = date(2011,1, 1)
    ch2_aof_1pt.crime = crime_aof
    ch2_aof_1pt.convicted = True
    return ch2_aof_1pt


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
def level2m_4pts(
    ch1_larc1: object, # 1 pt
    ch_clone_larc1: object, # 0 (more) pts
    ch2_aof_1pt: object, # 1 pt
    ch_infraction: object, # 0 pts
    ch3_cl2_0pt: object, # 1 pt
    charge_methI: object, # 1 pt
    ) -> object:
    '''
    This represents a mid-level misdemeanant with 4 pts for misds 
    (expected value is Level 2). 

    PARAMETERS:
    ____________________________________________________________________
    :ch1_larc1: object, # 1 pt
    :ch_clone_larc1: object, # 0 (more) pts
    :ch2_aof_1pt: object, # 1 pt
    :ch_infraction: object, # 0 pts
    :ch3_cl2_0pt: object, # 1 pt
    :charge_methI: object, # 1 pt

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection instance with 1 cl 1 Misd (1 pt)
    :rtype: ChargeCollection
    '''
    level2m_4pts = Charge_Collection()
    level2m_4pts.add_charge(ch1_larc1)
    level2m_4pts.add_charge(ch_clone_larc1)
    level2m_4pts.add_charge(ch2_aof_1pt)
    level2m_4pts.add_charge(ch_infraction)
    level2m_4pts.add_charge(ch3_cl2_0pt)
    level2m_4pts.add_charge(charge_methI)
    return level2m_4pts

def test_initialization():
    '''This tests an initialization of a Felony_RecordMachine.'''
    emptyrecord = Charge_Collection()
    misdemeanormachine = MisdemeanorRecordMachine(emptyrecord)
    assert FinishedState == type(misdemeanormachine.state)
    assert 0 == misdemeanormachine.points
    assert 1 == misdemeanormachine.level

def test_infraction(rec_infraction: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes rec_infraction (record with just 1 infraction) and 
    confirms the fsm runs it and returns the correct values.

    PARAMETERS:
    ____________________________________________________________________
    :rec_infraction: a conviction collection -- level 1 w 1 point
    '''
    misdemeanormachine = MisdemeanorRecordMachine(rec_infraction)
    assert FinishedState == type(misdemeanormachine.state)
    assert 0 == misdemeanormachine.points
    assert 1 == misdemeanormachine.level

def test_recordlevel2(level2_onepoint: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level2_onepoint as a fixture (misd lv 2, 1 pt) and 
    confirms the fsm runs it and returns the correct values.

    PARAMETERS:
    ____________________________________________________________________
    :level2_onepoint: a conviction collection -- level 1 w 1 point
    '''
    misdemeanormachine = MisdemeanorRecordMachine(level2_onepoint)
    assert FinishedState == type(misdemeanormachine.state)
    assert 1 == misdemeanormachine.points
    assert 2 == misdemeanormachine.level

def test_recolev2_samedate(level1_1pt_withclone: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level1_1pt_withclone as a fixture (misd record level 2), 
    and confirms that two class 1 misdemeanors on the same date only 
    calculate one point.

    PARAMETERS:
    ____________________________________________________________________
    :level1_1pt_withclone: a conviction collection -- m-lev 2 w 1 point
    '''
    misdemeanormachine = MisdemeanorRecordMachine(level1_1pt_withclone)
    assert FinishedState == type(misdemeanormachine.state)
    assert 1 == misdemeanormachine.points
    assert 2 == misdemeanormachine.level

def test_recordlevel2_1pts(level2_1points: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level2_1points as a fixture (mids record lv 2, 1 pts) and
    confirms the fsm runs it and returns the correct values.

    PARAMETERS:
    ____________________________________________________________________
    :level2_1points: a conviction collection -- level 2 w 1 pts
    '''
    misdemeanormachine = MisdemeanorRecordMachine(level2_1points)
    assert FinishedState == type(misdemeanormachine.state)
    assert 1 == misdemeanormachine.points
    assert 2 == misdemeanormachine.level

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
    misdemeanormachine = MisdemeanorRecordMachine(level2_2points)
    assert FinishedState == type(misdemeanormachine.state)
    assert 2 == misdemeanormachine.points
    assert 2 == misdemeanormachine.level

def test_recordlevel2m_4pts(level2m_4pts: object):
    '''
    INTEGRATION TEST:
    ____________________________________________________________________
    This takes level2m_4pts as a fixture (record lv 2, 4 pts) and 
    confirms the fsm runs it and returns the correct values.

    PARAMETERS:
    ____________________________________________________________________
    :level2m_4pts: a conviction collection -- level 2 w 4 pts
    '''
    misdemeanormachine = MisdemeanorRecordMachine(level2m_4pts)
    assert FinishedState == type(misdemeanormachine.state)
    assert 4 == misdemeanormachine.points
    assert 2 == misdemeanormachine.level



# def test_level2_4pts_edges(level2_4pts_edges: object):
#     '''
#     INTEGRATION TEST:
#     ____________________________________________________________________
#     This takes level2_4pts_edges as a fixture (record lv 2, 4 pts) and 
#     confirms the fsm runs it and returns the correct values. Here, we 
#     specifically test the edge cases from Chapter 20 (vehicle statutes)

#     PARAMETERS:
#     ____________________________________________________________________
#     :level2_4pts_edges: conviction collection -- lev 2 w 4 (edge cases)
#     '''
#     felofsm = Felony_RecordMachine()

#     felofsm.on_event(level2_4pts_edges)
#     assert FinishedState == type(felofsm.state)
#     assert 4 == felofsm.points
#     assert 2 == felofsm.level

# def test_recordlevel2_5pts(level2_5points: object):
#     '''
#     INTEGRATION TEST:
#     ____________________________________________________________________
#     This takes level2_5points as a fixture (record lv 2, 5 pts) and 
#     confirms the fsm runs it and returns the correct values.

#     PARAMETERS:
#     ____________________________________________________________________
#     :level2_5points: a conviction collection -- level 2 w 5 pts
#     '''
#     felofsm = Felony_RecordMachine()

#     felofsm.on_event(level2_5points)
#     assert FinishedState == type(felofsm.state)
#     assert 5 == felofsm.points
#     assert 2 == felofsm.level

# def test_recordlevel3_6pts(level3_6points: object):
#     '''
#     INTEGRATION TEST:
#     ____________________________________________________________________
#     This takes level3_6points as a fixture (record lv 3, 6 pts) and 
#     confirms the fsm runs it and returns the correct values.

#     PARAMETERS:
#     ____________________________________________________________________
#     :level3_6points: a conviction collection -- level 3 w 6 pts
#     '''
#     felofsm = Felony_RecordMachine()

#     felofsm.on_event(level3_6points)
#     assert FinishedState == type(felofsm.state)
#     assert 6 == felofsm.points
#     assert 3 == felofsm.level    

# def test_recordlevel3_9pts(level3_9points: object):
#     '''
#     INTEGRATION TEST:
#     ____________________________________________________________________
#     This takes level3_9points as a fixture (record lv 3, 9 pts) and 
#     confirms the fsm runs it and returns the correct values.

#     PARAMETERS:
#     ____________________________________________________________________
#     :level3_9points: a conviction collection -- level 3 w 9 pts
#     '''
#     felofsm = Felony_RecordMachine()

#     felofsm.on_event(level3_9points)
#     assert FinishedState == type(felofsm.state)
#     assert 9 == felofsm.points
#     assert 3 == felofsm.level

# def test_recordlevel4_10pts(level4_10points: object):
#     '''
#     INTEGRATION TEST:
#     ____________________________________________________________________
#     This takes level4_10points as a fixture (record lv 4, 10 pts) and 
#     confirms the fsm runs it and returns the correct values.

#     PARAMETERS:
#     ____________________________________________________________________
#     :level4_10points: a conviction collection -- level 4 w 10 pts
#     '''
#     felofsm = Felony_RecordMachine()

#     felofsm.on_event(level4_10points)
#     assert FinishedState == type(felofsm.state)
#     assert 10 == felofsm.points
#     assert 4 == felofsm.level


# def test_recordlevel4_13pts(level4_13points: object):
#     '''
#     INTEGRATION TEST:
#     ____________________________________________________________________
#     This takes level4_13points as a fixture (record lv 4, 13 pts) and 
#     confirms the fsm runs it and returns the correct values.

#     PARAMETERS:
#     ____________________________________________________________________
#     :level4_13points: a conviction collection -- level 4 w 13 pts
#     '''
#     felofsm = Felony_RecordMachine()

#     felofsm.on_event(level4_13points)
#     assert FinishedState == type(felofsm.state)
#     assert 13 == felofsm.points
#     assert 4 == felofsm.level

# def test_recordlevel5_14pts(level5_14points: object):
#     '''
#     INTEGRATION TEST:
#     ____________________________________________________________________
#     This takes level5_14points as a fixture (record lv 5, 14 pts) and 
#     confirms the fsm runs it and returns the correct values.

#     PARAMETERS:
#     ____________________________________________________________________
#     :level5_14points: a conviction collection -- level 5 w 14 pts
#     '''
#     felofsm = Felony_RecordMachine()

#     felofsm.on_event(level5_14points)
#     assert FinishedState == type(felofsm.state)
#     assert 14 == felofsm.points
#     assert 5 == felofsm.level

# def test_recordlevel5_17pts(level5_17points: object):
#     '''
#     INTEGRATION TEST:
#     ____________________________________________________________________
#     This takes level5_17points as a fixture (record lv 5, 17 pts) and 
#     confirms the fsm runs it and returns the correct values.

#     PARAMETERS:
#     ____________________________________________________________________
#     :level5_17points: a conviction collection -- level 5 w 17 pts
#     '''
#     felofsm = Felony_RecordMachine()

#     felofsm.on_event(level5_17points)
#     assert FinishedState == type(felofsm.state)
#     assert 17 == felofsm.points
#     assert 5 == felofsm.level


# def test_recordlevel6_18pts(level6_18points: object):
#     '''
#     INTEGRATION TEST:
#     ____________________________________________________________________
#     This takes level6_18points as a fixture (record lv 6, 18 pts) and 
#     confirms the fsm runs it and returns the correct values.

#     PARAMETERS:
#     ____________________________________________________________________
#     :level6_18points: a conviction collection -- level 6 w 18 pts
#     '''
#     felofsm = Felony_RecordMachine()

#     felofsm.on_event(level6_18points)
#     assert FinishedState == type(felofsm.state)
#     assert 18 == felofsm.points
#     assert 6 == felofsm.level

# def test_basestate():
#     '''
#     WHITE BOX TEST:
#     ____________________________________________________________________
#     This is a test of the base state and its methods and returns.
#     '''
#     base = State()
#     colx = Charge_Collection()
#     assert 0 == base.on_event(colx, 0, 0)
#     assert "State" == str(base)
#     assert "State" == repr(base)

# def test_startstate():
#     '''
#     WHITE BOX TEST:
#     ____________________________________________________________________
#     This is a test of the start state and its methods and returns.
#     '''
#     start = StartState()
#     colx = Charge_Collection()
#     assert FinishedState == type(start.on_event(colx, 0, 0))
