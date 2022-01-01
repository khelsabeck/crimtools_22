'''
file:   test_collections.py
author: Keith Helsabeck

This is the file for testing collections (using pytest).
Run tests with: "pytest --cov=src --cov-report term-missing"
'''
import pytest
from datetime import date, datetime, timedelta
import typing
import uuid

from src.charge import Charge
from src.crime import Crime
from src.defendant import Defendant
from src.convictiondate import ConvictionDate
from src.collections import Charge_Collection

@pytest.fixture
def charge1():
    charge1 = Charge()
    crime1 = Crime()
    crime1.set_description("Simple Assault")
    crime1.set_crimeclass("Class 2 Misdemeanor")
    crime1.set_statute("NCGS 14-33")
    charge1.set_id(1)
    charge1.set_offensedate(date(2009,1, 1))
    charge1.set_dispositiondate(date(2010,1, 1))
    charge1.set_crime(crime1)
    charge1.convicted = True 
    return charge1

@pytest.fixture
def charge2():
    charge2 = Charge()
    crime2 = Crime()
    crime2.set_description("Larceny")
    crime2.set_crimeclass("Class 1 Misdemeanor")
    crime2.set_statute("NCGS 14-72")
    charge2.set_id(2)
    charge2.set_offensedate(date(2001, 1, 1))
    charge2.set_dispositiondate(date(2002, 2, 2))
    charge2.set_crime(crime2)
    charge2.convicted = True 
    return charge2


def test_initialization():
    '''This tests an initialization.'''
    collection = Charge_Collection()
    assert [] == collection.charges

def test_adder():
    '''Tests adder with valid&invalid data'''
    charge = Charge()
    collection = Charge_Collection()
    collection.add_charge(charge)
    assert [charge] == collection.charges
    with pytest.raises(ValueError, \
        match="Only valid Charge objects may be added.") as exc_info:
        collection.add_charge(42)  #wrong type
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

def test_remove():
    '''Tests adder with valid/invalid data'''
    charge = Charge()
    collection = Charge_Collection()
    collection.add_charge(charge)
    assert [charge] == collection.charges
    collection.remove_charge(0)
    assert [] == collection.charges
    with pytest.raises(ValueError, \
        match="This charge is not in charges.") as exc_info:
        collection.remove_charge(42)  #wrong type
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

def test_isin():
    '''Tests the is_in--confirms item in collection, not other'''
    charge = Charge()
    collection = Charge_Collection()
    collection.add_charge(charge)
    assert True == collection.is_in(charge)
    charge2 = Charge()
    assert False == collection.is_in(charge2)

def test_sortby_offense(charge1: object, charge2: object):
    '''Tests for sortby_offensedate--confirms order'''
    collection = Charge_Collection()
    collection.add_charge(charge1)
    collection.add_charge(charge2)
    assert [charge1, charge2] == collection.charges
    collection.sortby_offensedate()
    assert [charge2, charge1] == collection.charges

def test_sortby_conviction(charge1: object, charge2: object):
    '''Tests for sortby_convictiondate--confirms order'''
    collection = Charge_Collection()
    collection.add_charge(charge1)
    collection.add_charge(charge2)
    assert [charge1, charge2] == collection.charges
    collection.sortby_conviction()
    assert [charge2, charge1] == collection.charges

def test_datemaker(charge1: object, charge2: object):
    '''Tests for datemaker--confirms order'''
    collection = Charge_Collection()
    collection.add_charge(charge1)
    collection.add_charge(charge2)
    collection.datemaker()
    assert [date(2002,2,2), date(2010,1,1)] == collection.unique_dates

def test_groupy_conviction(charge1: object, charge2: object):
    '''Tests the groupy_convictiondate method and confirms
    that the cons_bydate object is ordered correctly.'''
    collection = Charge_Collection()
    collection.add_charge(charge1)
    collection.add_charge(charge2)
    collection.groupby_convictiondate()
    assert [charge2] == collection.cons_bydate[0].convictions[3]
    assert [charge1] == collection.cons_bydate[1].convictions[2]