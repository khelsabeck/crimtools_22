import pytest
from datetime import date, datetime, timedelta
import typing
import uuid

from src.defendant import Defendant

def test_initialization():
    '''This tests an initialization.'''
    my_defendant = Defendant()
    assert "" == my_defendant.firstname
    assert "" == my_defendant.lastname
    assert "Defendant" == my_defendant.fullname
    assert None == my_defendant.birthdate

def test_setters():
    '''This tests setters with valid data.'''
    my_defendant = Defendant()
    my_defendant.set_firstname("John")
    my_defendant.set_lastname("Smith")
    my_defendant.set_birthdate( date(2010,1, 1) )
    my_defendant.set_id(1)
    my_defendant.set_uid( uuid.uuid4() )
    assert "John" == my_defendant.firstname
    assert "Smith" == my_defendant.lastname
    assert "John Smith" == my_defendant.fullname
    assert date(2010,1, 1) == my_defendant.birthdate
    assert 1 == my_defendant.id
    assert type(uuid.uuid4()) == type(my_defendant.unique_id)

def test_invalid_namesetters():
    '''This tests name setters with invalid data.'''
    my_defendant = Defendant()
    with pytest.raises(ValueError, match='A name must be a string, lte 50 char.')\
         as exc_info:
        my_defendant.set_firstname(
            "012345678901234567890123456789012345678901234567890"
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

    my_defendant = Defendant()
    with pytest.raises(ValueError, match='A name must be a string, lte 50 char.')\
         as exc_info:
        my_defendant.set_firstname(
            42
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

    with pytest.raises(ValueError, match='A name must be a string, lte 50 char.')\
         as exc_info:
        my_defendant.set_lastname(
            "012345678901234567890123456789012345678901234567890"
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

    with pytest.raises(ValueError, match='A name must be a string, lte 50 char.')\
         as exc_info:
        my_defendant.set_lastname(
            42
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

    assert my_defendant.fullname == "Defendant"

def test_invalid_birth():
    '''This tests birthdate setter with invalid data.'''
    my_defendant = Defendant()
    with pytest.raises(ValueError, match='A birthdate must be a datetime.date.')\
         as exc_info:
        my_defendant.set_birthdate(
            "purple polkadots"
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

def test_invalid_id():
    '''This tests id setter with invalid data.'''
    my_defendant = Defendant()
    with pytest.raises(ValueError, match='An id must be a valid int.')\
         as exc_info:
        my_defendant.set_id(
            "purple polkadots"
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

def test_invalid_uid():
    '''This tests uid setter with invalid data.'''
    my_defendant = Defendant()
    with pytest.raises(ValueError, match='A unique_id must be a valid uuid4.')\
         as exc_info:
        my_defendant.set_uid(
            "purple polkadots"
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)