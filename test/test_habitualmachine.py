'''
file    test_habitualmachine.py
author  Keith Helsabeck

________________________________________________________________________
This tests the habitualmachine module using pytest.
'''
from itertools import chain
import pytest
from datetime import date, datetime, timedelta
import typing
import uuid

from src.crime import Crime
from src.charge import Charge
from src.collections import Charge_Collection
from src.dumbwaiter import Dumbwaiter
from src.habitualmachine import *

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

@pytest.fixture
def record_disqualified(
    ch_disqualified1: object,
    ch_disqualified2: object, 
    ch_disqualified3: object
    ) -> object:
    '''
    This represents a record with only diqualified felonies. 

    PARAMETERS:
    ____________________________________________________________________
    :ch_disqualified1: a Charge instance with a disqualed felony
    :ch_disqualified2: a Charge instance with a disqualed felony
    :ch_disqualified3: a Charge instance with a disqualed felony

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection not resulting in habitual
    :rtype: ChargeCollection
    '''
    record_disqualified = Charge_Collection()
    record_disqualified.add_charge(ch_disqualified1)
    record_disqualified.add_charge(ch_disqualified2)
    record_disqualified.add_charge(ch_disqualified3)
    return record_disqualified

@pytest.fixture
def record_disqualified2(
    ch_disqualified1: object,
    charge_robD: object, 
    ) -> object:
    '''
    This represents a record with a diqualified felony after
    one qualified felony. Testing the strike 2 transitions

    PARAMETERS:
    ____________________________________________________________________
    :ch_disqualified1: a Charge instance with a disqualed felony
    :charge_robD: a Charge instance with a qualified felony (D robbery)

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection not resulting in habitual
    :rtype: ChargeCollection
    '''
    record_disqualified2 = Charge_Collection()
    record_disqualified2.add_charge(charge_robD)
    record_disqualified2.add_charge(ch_disqualified1)
    return record_disqualified2

@pytest.fixture
def record_strike2_thendisqual(
    ch_disqualified1: object,
    charge_robD: object, 
    ch5_larcH_2pt: object
    ) -> object:
    '''
    This represents a record with a diqualified felony after
    one qualified felony. Testing the strike 2 transitions

    PARAMETERS:
    ____________________________________________________________________
    :ch_disqualified1: a Charge instance with a disqualed felony
    :charge_robD: a Charge instance with a qualified felony (D robbery)
    :ch5_larcH_2pt: a Charge instance with a qualified felony (H larc)

    RETURN:
    ____________________________________________________________________
    :return: a ChargeCollection not resulting in habitual
    :rtype: ChargeCollection
    '''
    record_strike2_thendisqual = Charge_Collection()
    record_strike2_thendisqual.add_charge(charge_robD)
    record_strike2_thendisqual.add_charge(ch_disqualified1)
    record_strike2_thendisqual.add_charge(ch5_larcH_2pt)
    return record_strike2_thendisqual


def test_initialization():
    '''This tests an initialization of a HabtualMachine.'''
    colx = Charge_Collection()
    colx.groupby_convictiondate()
    habmachine = HabitualMachine(colx, date(1983,8,24))
    assert FinishedState == type(habmachine.state)
    assert False == habmachine.habeligible

def test_baseState():
    '''test of base state's values'''
    state = State()
    dw = Dumbwaiter(date(1983,8,24))
    colx = Charge_Collection()
    assert 0 == state.on_event(colx, dw, 0)
    assert "State" == str(state)
    assert "State" == repr(state)

def test_startToFinish(level1_0points: object):
    '''
    Test of a record with no felonies

    INTEGRATION TEST
    ____________________________________________________________________
    This takes a record with only a single misdemeanor and no felonies,
    and it should run the analysis without hitting the strike states and
    give an output of non-habitual.

    PARAMETERS:
    ____________________________________________________________________
    :param level1_0points: a charge with a single

    '''
    colx = level1_0points
    colx.groupby_convictiondate()
    habmachine = HabitualMachine(colx, date(1983,8,24))
    assert FinishedState == type(habmachine.state)
    assert False == habmachine.habeligible

def test_OneStrike(level2_5points: object):
    '''
    Test of a record with a single felony mixed w misdemeanors

    INTEGRATION TEST
    ____________________________________________________________________
    This takes a record with only a single felony with misdemeanors,
    and it should run the analysis and give an output of non-habitual.

    PARAMETERS:
    ____________________________________________________________________
    :param level2_5points: a charge with a single

    '''
    colx = level2_5points
    colx.groupby_convictiondate()
    habmachine = HabitualMachine(colx, date(1983,8,24))
    assert FinishedState == type(habmachine.state)
    assert False == habmachine.habeligible

def test_TwoStrikes(level4_10points: object):
    '''
    Test of a record with two felonies in sequence.

    INTEGRATION TEST
    ____________________________________________________________________
    This takes a record with two felonies,and it should run the analysis
    and give an output of non-habitual.

    PARAMETERS:
    ____________________________________________________________________
    :param level4_10points: a charge with a single

    '''
    colx = level4_10points
    colx.groupby_convictiondate()
    habmachine = HabitualMachine(colx, date(1983,8,24))
    assert FinishedState == type(habmachine.state)
    assert False == habmachine.habeligible

def test_Habitual(level3_9points: object):
    '''
    Test of a record with three felonies in sequence (all over 18).

    INTEGRATION TEST
    ____________________________________________________________________
    This takes a record with 3 felonies in sequence, and it should run 
    the analysis and give an output of habitual felony.

    PARAMETERS:
    ____________________________________________________________________
    :param level3_9points: a charge with a single
    '''
    colx = level3_9points
    colx.groupby_convictiondate()
    habmachine = HabitualMachine(colx, date(1983,8,24))
    assert FinishedState == type(habmachine.state)
    assert True == habmachine.habeligible

def test_OneUnder18(level3_9points: object):
    '''
    Test of a record with three felonies in sequence (2 over 18).
    This should qualify

    INTEGRATION TEST
    ____________________________________________________________________
    This takes a record with 3 felonies in sequence, 2 of which were 
    when the D was 18+, and it should run the analysis and give an 
    output of habitual felony.

    PARAMETERS:
    ____________________________________________________________________
    :param level3_9points: a charge with a single
    '''
    colx = level3_9points
    colx.groupby_convictiondate()
    habmachine = HabitualMachine(colx, date(1995,1,3))
    assert FinishedState == type(habmachine.state)
    assert True == habmachine.habeligible
    assert date(2015, 2, 2) == habmachine.date_eligible
    assert True == habmachine.date_iseligible(date(2015, 2, 2))
    assert False == habmachine.date_iseligible(date(2015, 1, 2))

def test_2of3Under18(level3_9points: object):
    '''
    Test of a record with three felonies in sequence (1 over 18).
    This should not qualify (only 1 felony conviction after 18).

    INTEGRATION TEST
    ____________________________________________________________________
    This takes a record with 3 felonies in sequence, 1 of which was 
    when the D was 18+, and it should run the analysis and give an 
    output of habitual felony False.

    PARAMETERS:
    ____________________________________________________________________
    :param level3_9points: a charge with a single
    '''
    colx = level3_9points
    colx.groupby_convictiondate()
    habmachine = HabitualMachine(colx, date(1995,2,4))
    assert FinishedState == type(habmachine.state)
    assert False == habmachine.habeligible

def test_disqualified(record_disqualified: object):
    '''
    Test of a record with three felonies all disqualified.

    INTEGRATION TEST
    ____________________________________________________________________
    This takes a record with 3 felonies, none of which qualify

    PARAMETERS:
    ____________________________________________________________________
    :param record_disqualified: a record with no qualified felonies
    '''
    colx = record_disqualified
    colx.groupby_convictiondate()
    habmachine = HabitualMachine(colx, date(1995,2,4))
    assert FinishedState == type(habmachine.state)
    assert False == habmachine.habeligible


def test_disqualified2(record_disqualified2: object):
    '''
    Test of a record with 2 felonies, one disqualified.

    INTEGRATION TEST
    ____________________________________________________________________
    This takes a record with 2 felonies, one qualified

    PARAMETERS:
    ____________________________________________________________________
    :param record_disqualified2: a record that should not be habitual
    '''
    colx = record_disqualified2
    colx.groupby_convictiondate()
    habmachine = HabitualMachine(colx, date(1995,2,4))
    assert FinishedState == type(habmachine.state)
    assert False == habmachine.habeligible

def test_strike2(record_strike2_thendisqual: object):
    '''
    Test of a record with 3 felonies, one disqualified.

    INTEGRATION TEST
    ____________________________________________________________________
    This takes a record with 3 felonies, one disqualified. 

    PARAMETERS:
    ____________________________________________________________________
    :param record_strike2_thendisqual: record not be habitual
    '''
    colx = record_strike2_thendisqual
    colx.groupby_convictiondate()
    habmachine = HabitualMachine(colx, date(1995,2,4))
    assert FinishedState == type(habmachine.state)
    assert False == habmachine.habeligible