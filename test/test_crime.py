'''
file:   test_crime.py
author: Keith Helsabeck

This is the file for testing crime (using pytest).
Run tests with: "pytest --cov=src --cov-report term-missing"
'''
import pytest
from datetime import date, datetime, timedelta
import typing
import uuid

from src.crime import Crime

def test_initialization():
    '''This tests an initialization.'''
    crime = Crime()
    assert None == crime.id
    assert None == crime.unique_id
    assert "" == crime.statute
    assert "" == crime.description
    assert "" == crime.crimeclass
    assert [
        "Infraction", "Class 3 Misdemeanor", "Class 2 Misdemeanor", 
        "Class 1 Misdemeanor", "Class A1 Misdemeanor",
        "Class I Felony", "Class H Felony", "Class G Felony", 
        "Class F Felony", "Class E Felony", "Class D Felony",
        "Class C Felony", "Class B1 Felony", "Class B2 Felony",
        "Class A Felony",
    ] == Crime.valid_classes


def test_setters():
    '''This tests setters with valid data.'''
    crime = Crime()
    crime.set_crimeclass("Class A1 Misdemeanor")
    crime.set_statute("§14-72")
    crime.set_description("Larceny")
    crime.set_id(1)
    crime.set_uid( uuid.uuid4() )
    assert "Class A1 Misdemeanor" == crime.crimeclass
    assert "§14-72" == crime.statute
    assert "Larceny" == crime.description
    assert 1 == crime.id
    assert type(uuid.uuid4()) == type(crime.unique_id)

def test_invalid_crimeclasses():
    '''This tests crimeclass setter with invalid data.'''
    crime = Crime()
    with pytest.raises(ValueError, match="crimeclass invalid.") as exc_info:
        crime.set_crimeclass(
            "012345678901234567890123456789012345678901234567890"
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

def test_invalid_statute():
    '''This tests statute setter with invalid data.'''
    crime = Crime()
    with pytest.raises(ValueError, match="A statute must be str lte 50 chars.") \
        as exc_info:
        crime.set_statute(
            "012345678901234567890123456789012345678901234567890"
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)
    crime = Crime()
    with pytest.raises(ValueError, match="A statute must be str lte 50 chars.") \
        as exc_info:
        crime.set_statute(
            42
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

def test_invalid_descriptions():
    '''This tests description setter with invalid data.'''
    crime = Crime()
    with pytest.raises(ValueError, match="A description must be str lte 50 chars.") \
        as exc_info:
        crime.set_description(
            "012345678901234567890123456789012345678901234567890"
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)
    crime = Crime()
    with pytest.raises(ValueError, match="A description must be str lte 50 chars.") \
        as exc_info:
        crime.set_description(
            42
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

def test_invalid_id():
    '''This tests id setter with invalid data.'''
    crime = Crime()
    with pytest.raises(ValueError, match='An id must be a valid int.')\
         as exc_info:
        crime.set_id(
            "purple polkadots"
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)

def test_invalid_uid():
    '''This tests uid setter with invalid data.'''
    crime = Crime()
    with pytest.raises(ValueError, match='A unique_id must be a valid uuid4.')\
         as exc_info:
        crime.set_uid(
            "purple polkadots"
        )
    exception_raised = exc_info.value
    assert ValueError == type(exception_raised)