'''
file    charge.py
author  Keith Helsabeck

This is the file charge.py, for holding the class Charge. 
Charge represents an instance of a Defendant being charged with a 
particular crime on a particular date. A charge may be either a pending
charge, or a disposed charge (not guilty, dismissed, convicted/guilty).
'''
import typing
import uuid
from defendant import Defendant
from crime import Crime
import datetime

class Charge:
    '''
    Charge represents an instance of a Defendant being charged with a 
    particular crime on a particular date.
    
    A charge should have these fields: 
        :field id: (int) a simple sequential id
        :field unique_id: a uuid4 object 
        :field offense_date: datetime of the alleged crime (datetime.date)
        :field disposition_date: date the case was disposed (datetime.date)
        :field convicted: Boolean val, True if convicted, else False
    '''
    def __init__(self):
        self.id = None
        self.unique_id = None
        self.offense_date = None
        self.disposition_date = None
        self.convicted = None

    def validate_date(self, d: object):
        '''
        validates the potential date as a valid datetime
        date object (or None).

        :param d: an input to validate as a date 

        :returns: True for valid, else False
        :rtype: Bool
        '''
        if ( d == None ) or ( type(d) == type(datetime.date) ):
            return True
        return False