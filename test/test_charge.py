import pytest
from datetime import date, datetime, timedelta
import typing
import uuid

from src.charge import Charge
from src.crime import Crime

def test_initialization():
    '''This tests an initialization.'''
    charge = Charge()
    assert None == charge.id
    assert None == charge.unique_id
    assert None == charge.offense_date
    assert None == charge.crime
    assert None == charge.disposition_date
    assert False == charge.convicted

def test_setters():
    '''This tests setters with valid data.'''
    crime = Crime()
    charge = Charge()
    charge.set_id(1)
    charge.set_uid( uuid.uuid4() )
    charge.set_offensedate( date(2010,1, 1) )
    charge.set_dispositiondate( date(2010,2, 2) )
    charge.convicted = True
    charge.set_crime(crime)
    assert date(2010,1, 1) == charge.offense_date
    assert date(2010,2, 2) == charge.disposition_date
    assert 1 == charge.id
    assert type(uuid.uuid4()) == type(charge.unique_id)
    assert True == charge.convicted
    assert crime == charge.crime

def test_invalid_dates():
    '''This tests date setter with invalid data.'''
    charge = Charge()
    with pytest.raises(ValueError, match='A date must be a datetime.date.')\
         as exc_info:
        charge.set_offensedate(
            "purple polkadots"
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

    charge = Charge()
    with pytest.raises(ValueError, match='A date must be a datetime.date.')\
         as exc_info:
        charge.set_dispositiondate(
            "purple polkadots"
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

def test_invalid_id():
    '''This tests id setter with invalid data.'''
    charge = Charge()
    with pytest.raises(ValueError, match='An id must be a valid int.')\
         as exc_info:
        charge.set_id(
            "purple polkadots"
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

def test_invalid_uid():
    '''This tests uid setter with invalid data.'''
    charge = Charge()
    with pytest.raises(ValueError, match='A unique_id must be a valid uuid4.')\
         as exc_info:
        charge.set_uid(
            "purple polkadots"
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

def test_invalid_crime():
    '''This tests the crime setter with invalid data.'''
    charge = Charge()
    with pytest.raises(ValueError, match='A crime must be a valid Crime instance.')\
         as exc_info:
        charge.set_crime(
            "purple polkadots"
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)