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
def crime_edge1() -> object:
    '''This represents an edge case crime, a non-Chapter 14
    midemeanor that counts for 1 felony point.'''
    crime_edge1 = Crime()
    crime_edge1.statute = "§20-141.4(a2)"
    crime_edge1.description = "misdemeanor death by vehicle"
    crime_edge1.crimeclass = "Class 1 Misdemeanor"
    return crime_edge1

@pytest.fixture
def crime_edge2() -> object:
    '''This represents an edge case crime, a non-Chapter 14
    midemeanor that counts for 1 felony point.'''
    crime_edge2 = Crime()
    crime_edge2.statute = "§20-138.1"
    crime_edge2.description = "impaired driving"
    crime_edge2.crimeclass = "Class 1 Misdemeanor"
    return crime_edge2

@pytest.fixture
def crime_edge3() -> object:
    '''This represents an edge case crime, a non-Chapter 14
    midemeanor that counts for 1 felony point.'''
    crime_edge3 = Crime()
    crime_edge3.statute = "§20-138.2"
    crime_edge3.description = "Commercial impaired driving"
    crime_edge3.crimeclass = "Class 1 Misdemeanor"
    return crime_edge3

@pytest.fixture
def crime_edge4() -> object:
    '''This represents an edge case crime, a non-Chapter 14
    midemeanor that counts for 1 felony point.'''
    crime_edge4 = Crime()
    crime_edge4.statute = "§20-28(a1)"
    crime_edge4.description = "Driving While Revoked After an \
Impaired Offense"
    crime_edge4.crimeclass = "Class 1 Misdemeanor"
    return crime_edge4

@pytest.fixture
def ch1_larc1(crime_larceny1: object) -> object:
    '''
    This represents a class 1 larceny charge.
    
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
def ch_clone_larc1(crime_larceny1: object) -> object:
    '''
    This is a class 1 larc charge with the same date as the other, 
    so we can test that only one charge counts.
    
    PARAMETERS:
    ____________________________________________________________________
    :crime_larceny1: a Crime instance w a class 1 larceny (1 point)

    RETURN:
    ____________________________________________________________________
    :returns: a Charge instance with a class 1 larceny
    :rtype: Charge
    '''
    ch_clone_larc1 = Charge()
    ch_clone_larc1.id = 50
    ch_clone_larc1.offense_date = date(2009,1, 1)
    ch_clone_larc1.disposition_date = date(2010,1, 1)
    ch_clone_larc1.crime = crime_larceny1
    ch_clone_larc1.convicted = True
    return ch_clone_larc1

@pytest.fixture
def ch2_aof_1pt(crime_aof: object) -> object:
    '''
    This is a class A1 AoF charge.
    
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
def ch4_cl1_1pt(crime_larceny1: object) -> object:
    '''
    This is a class 1 larc -- 1 felo point.

    PARAMETERS:
    ____________________________________________________________________
    :crime_larceny1: a Crime instance w a class 1 misd (1 pt)

    RETURN:
    ____________________________________________________________________
    :return: a Charge instance with a class 1-- larceny
    :rtype: Charge
    '''
    ch4_cl1_1pt = Charge()
    ch4_cl1_1pt.id = 4
    ch4_cl1_1pt.offense_date = date(2011, 1, 1)
    ch4_cl1_1pt.disposition_date = date(2012, 3, 3)
    ch4_cl1_1pt.crime = crime_larceny1
    ch4_cl1_1pt.convicted = True
    return ch4_cl1_1pt

@pytest.fixture
def charge_methI(crime_meth_classI: object) -> object:
    '''This is a class I meth -- 2 felo points.
    
    PARAMETERS:
    ____________________________________________________________________
    :crime_meth_classI: a Crime instance w a class I Felo (2 pts)

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
def ch5_larcH_2pt(crime_larc_classH: object) -> object:
    '''This is a class H larc -- 2 felo points.

    PARAMETERS:
    ____________________________________________________________________
    :crime_larc_classH: a Crime instance w a class H Felo (2 pts)

    RETURN:
    ____________________________________________________________________
    :return: a Charge instance with a class H -- F larceny
    :rtype: Charge
    '''
    ch5_larcH_2pt = Charge()
    ch5_larcH_2pt.id = 5
    ch5_larcH_2pt.offense_date = date(2013, 1, 1)
    ch5_larcH_2pt.disposition_date = date(2013, 1, 2)
    ch5_larcH_2pt.crime = crime_larc_classH
    ch5_larcH_2pt.convicted = True
    return ch5_larcH_2pt

@pytest.fixture
def charge_hackG(crime_hackg_classG: object) -> object:
    '''This is a class G hacking telecoms -- 4 felo points.
    
    PARAMETERS:
    ____________________________________________________________________
    :crime_hackg_classG: a Crime instance w a class G Felo (4 pts)

    RETURN:
    ____________________________________________________________________
    :return: a Charge instance with a class G -- F hacking telecoms
    :rtype: Charge
    '''
    charge_hackG = Charge()
    charge_hackG.id = 6
    charge_hackG.offense_date = date(2013, 2, 2)
    charge_hackG.disposition_date = date(2013, 2, 3)
    charge_hackG.crime = crime_hackg_classG
    charge_hackG.convicted = True
    return charge_hackG

@pytest.fixture
def charge_robD(crime_rob_classD: object) -> object:
    '''This represents a Class D Felony Robbery
    
    PARAMETERS:
    ____________________________________________________________________
    :crime_rob_classD: a Crime instance w a class D Felo (6 pts)

    RETURN:
    ____________________________________________________________________
    :return: a Charge instance with a class D -- Armed Robbery
    :rtype: Charge
    '''
    charge_robD = Charge()
    charge_robD.id = 16
    charge_robD.offense_date = date(2016, 1, 1)
    charge_robD.disposition_date = date(2016, 2, 3)
    charge_robD.crime = crime_rob_classD
    charge_robD.convicted = True
    return charge_robD

@pytest.fixture
def charge_murd2_B2(crime_murder2_b2: object) -> object:
    '''
    This represents a Class B2 Felony Murder 2. 
    NB: Murder 2 comes in a B2 and a B1.

    
    PARAMETERS:
    ____________________________________________________________________
    :crime_murder2_b2: a Crime instance w a class B2 Felo (6 pts)

    RETURN:
    ____________________________________________________________________
    :return: a Charge instance with a class B2 -- Murder 2
    :rtype: Charge
    '''
    charge_murd2_B2 = Charge()
    charge_murd2_B2.id = 17
    charge_murd2_B2.offense_date = date(2017, 1, 1)
    charge_murd2_B2.disposition_date = date(2017, 2, 3)
    charge_murd2_B2.crime = crime_murder2_b2
    charge_murd2_B2.convicted = True
    return charge_murd2_B2

@pytest.fixture
def charge_murd1_a10(crime_murder1_A: object) -> object:
    '''
    This represents a Class A Felony Murder 1.
    
    PARAMETERS:
    ____________________________________________________________________
    :crime_murder1_A: a Crime instance w a class A Felo (10 pts)

    RETURN:
    ____________________________________________________________________
    :return: a Charge instance with a class A -- Murder 1
    :rtype: Charge
    '''
    charge_murd1_a10 = Charge()
    charge_murd1_a10.id = 18
    charge_murd1_a10.offense_date = date(2018, 1, 1)
    charge_murd1_a10.disposition_date = date(2018, 2, 3)
    charge_murd1_a10.crime = crime_murder1_A
    charge_murd1_a10.convicted = True
    return charge_murd1_a10

@pytest.fixture
def charge_edge1(crime_edge1: object) -> object:
    '''
    Edge case--Chapter 20 misd that counts as a felony point
    for felony record calculations.
    
    PARAMETERS:
    ____________________________________________________________________
    :crime_edge1: a Crime instance from ch 20 (1 pt)

    RETURN:
    ____________________________________________________________________
    :return: a Charge instance with a class 1 Misd
    :rtype: Charge
    '''
    charge_edge1 = Charge()
    charge_edge1.id = 19
    charge_edge1.offense_date = date(2019, 1, 1)
    charge_edge1.disposition_date = date(2019, 2, 3)
    charge_edge1.crime = crime_edge1
    charge_edge1.convicted = True
    return charge_edge1

@pytest.fixture
def charge_edge2(crime_edge2: object) -> object:
    '''
    Edge case--Chapter 20 misd that counts as a felony points
    for felony record calculations.
    
    PARAMETERS:
    ____________________________________________________________________
    :crime_edge2: a Crime instance from ch 20 (1 pt)

    RETURN:
    ____________________________________________________________________
    :return: a Charge instance with a class 1 Misd
    :rtype: Charge
    '''
    charge_edge2 = Charge()
    charge_edge2.id = 20
    charge_edge2.offense_date = date(2020, 1, 1)
    charge_edge2.disposition_date = date(2020, 2, 3)
    charge_edge2.crime = crime_edge2
    charge_edge2.convicted = True
    return charge_edge2

@pytest.fixture
def charge_edge3(crime_edge3: object) -> object:
    '''
    Edge case--a Chapter 20 misd that counts as a felony point
    for felony record calculations.
    
    PARAMETERS:
    ____________________________________________________________________
    :crime_edge3: a Crime instance from ch 20 (1 pt)

    RETURN:
    ____________________________________________________________________
    :return: a Charge instance with a class 1 Misd
    :rtype: Charge
    '''

    charge_edge3 = Charge()
    charge_edge3.id = 21
    charge_edge3.offense_date = date(2021, 1, 1)
    charge_edge3.disposition_date = date(2021, 2, 3)
    charge_edge3.crime = crime_edge3
    charge_edge3.convicted = True
    return charge_edge3

@pytest.fixture
def charge_edge4(crime_edge4: object) -> object:
    '''
    Edge case--a Chapter 20 misd that counts as a felony point
    for felony record calculations.
    
    PARAMETERS:
    ____________________________________________________________________
    :crime_edge4: a Crime instance from ch 20 (1 pt)

    RETURN:
    ____________________________________________________________________
    :return: a Charge instance with a class 1 Misd
    :rtype: Charge
    '''
    charge_edge4 = Charge()
    charge_edge4.id = 22
    charge_edge4.offense_date = date(2022, 1, 1)
    charge_edge4.disposition_date = date(2022, 2, 3)
    charge_edge4.crime = crime_edge4
    charge_edge4.convicted = True
    return charge_edge4

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
