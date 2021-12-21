import pytest
from datetime import date, datetime, timedelta
import typing
import uuid

from src.charge import Charge
from src.crime import Crime
from src.convictiondate import ConvictionDate

def test_initialization():
    '''This tests an initialization.'''
    dt = date(2001,1,1)
    convictiondate = ConvictionDate(dt)
    assert [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] \
        == convictiondate.convictions

def test_adder():
    '''This tests the add method'''
    dt = date(2001,1,1)
    convictiondate = ConvictionDate(dt)
    crime = Crime()
    crime.crimeclass = "Infraction"
    charge = Charge()
    charge.set_dispositiondate(dt)
    charge.set_crime(crime)
    charge.convicted = True
    convictiondate.add(charge)
    assert charge == convictiondate.convictions[0][0]

def test_adder():
    '''This tests the add method'''
    dt = date(2001,1,1)
    convictiondate = ConvictionDate(dt)
    crime = Crime()
    crime.crimeclass = "Class A Felony"
    charge = Charge()
    charge.set_dispositiondate(dt)
    charge.set_crime(crime)
    charge.convicted = True
    convictiondate.add(charge)
    assert charge == convictiondate.convictions[14][0]

def test_validators():
    '''This tests the validation in the adder'''
    dt = date(2001,1,1)
    convictiondate = ConvictionDate(dt)
    crime = Crime()
    crime.crimeclass = "Class A Felony"
    charge = Charge()
    charge.set_dispositiondate(dt)
    charge.set_crime(crime)
    charge.convicted = True

    with pytest.raises(ValueError) \
        as exc_info:
        convictiondate.add(42)  #wrong type
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

    with pytest.raises(ValueError) \
        as exc_info:
        charge.disposition_date = None
        convictiondate.add(charge)
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

    with pytest.raises(ValueError) \
        as exc_info:
        charge.convicted = False
        convictiondate.add(charge)
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

    with pytest.raises(ValueError) \
        as exc_info:
        charge.crime.crime_class = "polka dots"
        convictiondate.add(charge)
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

    with pytest.raises(ValueError) \
        as exc_info:
        charge.disposition_date = date(2011,2,2)
        convictiondate.add(charge)
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)    