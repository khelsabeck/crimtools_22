import pytest
from datetime import date, datetime, timedelta
import typing
# import uuid

from src.misdemeanor_machine import *
from src.collections import Charge_Collection
from src.crime import Crime
from src.charge import Charge

@pytest.fixture(scope="package")
def crime_speeding() -> object:
    '''This represents simple speed infraction.'''
    crime_speeding = Crime()
    crime_speeding.statute = "§20-141"
    crime_speeding.description = "Speeding"
    crime_speeding.crimeclass = "Infraction"
    return crime_speeding

@pytest.fixture(scope="package")
def crime_shoplift3() -> object:
    '''This represents cl 3 misdemeanor shoplifting charge.'''
    crime_shoplift3 = Crime()
    crime_shoplift3.statute = "§14-72"
    crime_shoplift3.description = "Shoplifting"
    crime_shoplift3.crimeclass = "Class 3 Misdemeanor"
    return crime_shoplift3

@pytest.fixture(scope="package")
def crime_assault2() -> object:
    '''This represents cl 2 misdemeanor assault.'''
    crime_assault2 = Crime()
    crime_assault2.statute = "§14-33"
    crime_assault2.description = "Simple Assault"
    crime_assault2.crimeclass = "Class 2 Misdemeanor"
    return crime_assault2

@pytest.fixture(scope="package")
def crime_larceny1() -> object:
    '''This represents cl 1 misdemeanor larceny.'''
    crime_larceny1 = Crime()
    crime_larceny1.statute = "§14-72"
    crime_larceny1.description = "Larceny"
    crime_larceny1.crimeclass = "Class 1 Misdemeanor"
    return crime_larceny1

@pytest.fixture(scope="package")
def crime_aof() -> object:
    '''This represents cl A1 misdemeanor Assault on Female.'''
    crime_aof = Crime()
    crime_aof.statute = "§14-33"
    crime_aof.description = "Assault on a Female"
    crime_aof.crimeclass = "Class A1 Misdemeanor"
    return crime_aof

@pytest.fixture(scope="package")
def crime_meth_classI() -> object:
    '''This represents cl I felony -- Possess Meth, 2 pts.'''
    crime_meth_classI = Crime()
    crime_meth_classI.statute = "§90-95(d)(2)"
    crime_meth_classI.description = "Possession of Meth"
    crime_meth_classI.crimeclass = "Class I Felony"
    return crime_meth_classI

@pytest.fixture(scope="package")
def crime_larc_classH() -> object:
    '''This represents cl H felony Larceny, 2 pts.'''
    crime_larc_classH = Crime()
    crime_larc_classH.statute = "§14-72"
    crime_larc_classH.description = "Felony Larceny"
    crime_larc_classH.crimeclass = "Class H Felony"
    return crime_larc_classH

@pytest.fixture(scope="package")
def crime_hackg_classG() -> object:
    '''This represents cl G Telecom Hacking, 4 pts.'''
    crime_hackg_classG = Crime()
    crime_hackg_classG.statute = "§14-113.5"
    crime_hackg_classG.description = "Telecom Hacking"
    crime_hackg_classG.crimeclass = "Class G Felony"
    return crime_hackg_classG

@pytest.fixture(scope="package")
def crime_mans_classF() -> object:
    '''This represents cl E 2d deg kidnap, 4 pts.'''
    crime_mans_classF = Crime()
    crime_mans_classF.statute = "§14-18"
    crime_mans_classF.description = "Involuntary Manslaughter"
    crime_mans_classF.crimeclass = "Class F Felony"
    return crime_mans_classF

@pytest.fixture(scope="package")
def crime_kidnap_classE() -> object:
    '''This represents cl E 2d deg kidnap, 4 pts.'''
    crime_kidnap_classE = Crime()
    crime_kidnap_classE.statute = "§14-39"
    crime_kidnap_classE.description = "2d Deg Kidnapping"
    crime_kidnap_classE.crimeclass = "Class E Felony"
    return crime_kidnap_classE

@pytest.fixture(scope="package")
def crime_rob_classD() -> object:
    '''This represents cl D robberyw dang weap, 6 pts.'''
    crime_rob_classD = Crime()
    crime_rob_classD.statute = "§14-87"
    crime_rob_classD.description = "Robbery with Dangerous Weapon"
    crime_rob_classD.crimeclass = "Class D Felony"
    return crime_rob_classD

@pytest.fixture(scope="package")
def crime_awdwikisi_C() -> object:
    '''This represents a cl C assault w intent to kill or 
    inflict serious inj -- 6 pts'''
    crime_awdwikisi_C = Crime()
    crime_awdwikisi_C.statute = "§14-32(a)"
    crime_awdwikisi_C.description = "Assault w Deadly WIKISI"
    crime_awdwikisi_C.crimeclass = "Class C Felony"
    return crime_awdwikisi_C

@pytest.fixture(scope="package")
def crime_murder2_b2() -> object:
    '''This represents a cl B2 murder 2d deg -- 6 pts'''
    crime_murder2_b2 = Crime()
    crime_murder2_b2.statute = "§14-17(c)"
    crime_murder2_b2.description = "Murder 2d Deg"
    crime_murder2_b2.crimeclass = "Class B2 Felony"
    return crime_murder2_b2

@pytest.fixture(scope="package")
def crime_murder2_B1() -> object:
    '''This represents a cl B1 murder 2d deg -- 9 pts'''
    crime_murder2_B1 = Crime()
    crime_murder2_B1.statute = "§14-17(b)"
    crime_murder2_B1.description = "Murder 2d Deg"
    crime_murder2_B1.crimeclass = "Class B1 Felony"
    return crime_murder2_B1

@pytest.fixture(scope="package")
def crime_murder1_A() -> object:
    '''This represents a cl A murder 1st deg -- 10 pts'''
    crime_murder1_A = Crime()
    crime_murder1_A.statute = "§14-17(a)"
    crime_murder1_A.description = "Murder 1st Deg"
    crime_murder1_A.crimeclass = "Class A Felony"
    return crime_murder1_A

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
def cr_disqualified1() -> object:
    '''
    This represents an edge case crime for hab felony, a 
    crime of habitual breaking and entering.
    By statute (14-7.28), it does not count towards hab felon.
    '''
    cr_disqualified1 = Crime()
    cr_disqualified1.statute = "§14-7.28"
    cr_disqualified1.description = "Habitual break/enter"
    cr_disqualified1.crimeclass = "Class E Felony"
    return cr_disqualified1

@pytest.fixture
def cr_disqualified2() -> object:
    '''
    This represents an edge case crime for hab felony, a 
    crime of armed habitual felon.
    By statute (14-7.36), it does not count towards hab felon.
    '''
    cr_disqualified2 = Crime()
    cr_disqualified2.statute = "§14-7.36"
    cr_disqualified2.description = "Armed habitual felon"
    cr_disqualified2.crimeclass = "Class C Felony"
    return cr_disqualified2

@pytest.fixture
def cr_disqualified3() -> object:
    '''
    This represents an edge case crime for hab felony, a 
    crime of Habitual M Assault.
    By statute (14-7.33), it does not count towards hab felon.
    '''
    cr_disqualified3 = Crime()
    cr_disqualified3.statute = "§14-7.33"
    cr_disqualified3.description = "Habitual M Assault"
    cr_disqualified3.crimeclass = "Class H Felony"
    return cr_disqualified3

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
    This is a class 1 larc -- 1 felo point, 1 misd pt.

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
    ch1_larc1.offense_date = date(2009, 1, 1)
    ch1_larc1.disposition_date = date(2010, 1, 1)
    ch1_larc1.crime = crime_larceny1
    ch1_larc1.convicted = True
    return ch1_larc1

@pytest.fixture
def ch_clone_larc1(crime_larceny1: object) -> object:
    '''
    This is a class 1 larc charge with the same date as ch1_larc1, 
    so we can test that only one charge counts. 
    *NB: 2 convictions on same date for habitual -> only one counts.
    
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
def ch_infraction(crime_speeding: object) -> object:
    '''
    This is a simple speed infraction charge (convicted).
    
    PARAMETERS:
    ____________________________________________________________________
    :crime_speeding: a Crime instance for speeding (0 fel-pts, 0 m-pts)

    RETURN:
    ____________________________________________________________________
    :returns: a Charge instance with just an infraction for speeding
    :rtype: Charge
    '''
    ch_infraction = Charge()
    ch_infraction.id = 2
    ch_infraction.offense_date = date(2010, 1, 2)
    ch_infraction.disposition_date = date(2011, 1, 1)
    ch_infraction.crime = crime_speeding
    ch_infraction.convicted = True
    return ch_infraction

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
def ch_disqualified1(cr_disqualified1: object) -> object:
    '''
    Edge case--disqualified felony conviction (does not count for hab).
    
    PARAMETERS:
    ____________________________________________________________________
    :cr_disqualified1: a Crime instance that does not count for habitual

    RETURN:
    ____________________________________________________________________
    :return: a Charge instance that will not count for habitual felon
    :rtype: Charge
    '''

    ch_disqualified1 = Charge()
    ch_disqualified1.id = 100
    ch_disqualified1.offense_date = date(2022, 1, 1)
    ch_disqualified1.disposition_date = date(2022, 1, 2)
    ch_disqualified1.crime = cr_disqualified1
    ch_disqualified1.convicted = True
    return ch_disqualified1

@pytest.fixture
def ch_disqualified2(cr_disqualified2: object) -> object:
    '''
    Edge case--disqualified felony conviction (does not count for hab).
    
    PARAMETERS:
    ____________________________________________________________________
    :cr_disqualified2: a Crime instance that does not count for habitual

    RETURN:
    ____________________________________________________________________
    :return: a Charge instance that will not count for habitual felon
    :rtype: Charge
    '''

    ch_disqualified2 = Charge()
    ch_disqualified2.id = 101
    ch_disqualified2.offense_date = date(2022, 3, 1)
    ch_disqualified2.disposition_date = date(2022, 3, 2)
    ch_disqualified2.crime = cr_disqualified2
    ch_disqualified2.convicted = True
    return ch_disqualified2

@pytest.fixture
def ch_disqualified3(cr_disqualified3: object) -> object:
    '''
    Edge case--disqualified felony conviction (does not count for hab).
    
    PARAMETERS:
    ____________________________________________________________________
    :cr_disqualified3: a Crime instance that does not count for habitual

    RETURN:
    ____________________________________________________________________
    :return: a Charge instance that will not count for habitual felon
    :rtype: Charge
    '''

    ch_disqualified3 = Charge()
    ch_disqualified3.id = 102
    ch_disqualified3.offense_date = date(2022, 4, 1)
    ch_disqualified3.disposition_date = date(2022, 4, 2)
    ch_disqualified3.crime = cr_disqualified3
    ch_disqualified3.convicted = True
    return ch_disqualified3

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
