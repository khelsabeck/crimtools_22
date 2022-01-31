import pytest
from datetime import date, datetime, timedelta
import typing
# import uuid

from src.misdemeanor_machine import *
from src.collections import Charge_Collection
from src.crime import Crime
from src.charge import Charge

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
