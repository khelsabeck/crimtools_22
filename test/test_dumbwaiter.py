'''
file:   test_dumbwaiter.py
author: Keith Helsabeck

This is the file for testing dumbwaiter (using pytest).
Run tests with: "pytest --cov=src --cov-report term-missing"
'''

import pytest
from datetime import date, datetime, timedelta
import typing
import uuid

from src.dumbwaiter import Dumbwaiter


def test_init():
    '''Simple test of the init values.
    ____________________________________________________________________
    Expected:
    habcons -- list of habitual felony convictions (starts empty);
    habeligible --boolean of whether eligible (starts false);
    date_eligible -- date when eligible (starts as None);
    birthdate -- the defendant's birthdate (starts set as input);
    has_run -- False on init (True when run in FSM)
    '''
    dw = Dumbwaiter(date(1983,8,24))
    assert [] == dw.habcons
    assert False == dw.habeligible
    assert None == dw.date_eligible
    assert date(1983,8,24) == dw.birthdate 
    assert False == dw.has_run

def test_birthdate_setter():
    '''test of the birthdate setter's value exception'''
    dw = Dumbwaiter(date(1983,8,24))
    with pytest.raises(ValueError) \
        as exc_info:
        dw.set_birthdate(42)  #wrong type
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

def test_habeligible_setter():
    '''Test of the exception.'''
    dw = Dumbwaiter(date(1983,8,24))
    with pytest.raises(ValueError) \
        as exc_info:
        dw.set_habeligible(42)  #wrong type
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

def test_over18():
    '''Test of the function over18_on_date. 
    
    Expected: works for a valid datetime.date, and throws
    value error with improper data type'''
    dw = Dumbwaiter(date(1983,8,24))
    with pytest.raises(ValueError) \
        as exc_info:
        dw.over18_on_date(42)  #wrong type
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)
    assert True == dw.over18_on_date(date(2001,8,24)) 
    assert False == dw.over18_on_date(date(2001,8,23))

def test_date_elgible_setter():
    '''Test of set_date_eligible.
    
    Expected: should take a valid datetime.date and set date_eligible.
    If wrong type of input, raises value error.'''
    dw = Dumbwaiter(date(1983,8,24))
    with pytest.raises(ValueError) \
        as exc_info:
        dw.set_date_eligible(42)  #wrong type
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)
    dw.set_date_eligible(date(2002, 5, 5))
    assert date(2002, 5, 5) == dw.date_eligible 

def test_offensedate_iseligible():
    '''Tests whether an input date (offense) comes after the
    defendant became eligible.'''
    dw = Dumbwaiter(date(1983,8,24))
    dw.set_date_eligible(date(2002, 5, 5))
    assert date(2002, 5, 5) == dw.date_eligible 
    assert False == dw.offensedate_iseligible(date(2002, 5, 4))
    assert True == dw.offensedate_iseligible(date(2002, 5, 5))

