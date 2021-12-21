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
from .defendant import Defendant
from .crime import Crime
import datetime

class Charge:
    '''
    Charge represents an instance of a Defendant being charged with a 
    particular crime on a particular date.
    
    ATTRIBUTES: 
    ____________________________________________________________________
    :attr id: (int) a simple sequential id
    :attr unique_id: a uuid4 object 
    :attr offense_date: datetime of the alleged crime (datetime.date)
    :attr disposition_date: date the case was disposed (datetime.date)
    :attr convicted: Boolean val, True if convicted, else False

    METHODS
    :method date_isvalid: ret T if date valid, else F
    '''
    def __init__(self):
        self.id = None
        self.unique_id = None
        self.offense_date = None
        self.crime = None
        self.disposition_date = None
        self.convicted = False

    def date_isvalid(self, dt: object) -> bool:
        '''
        validates the potential date as a valid datetime
        date object (or None).

        :param d: an input to validate as a date 

        :returns: True for valid, else False
        :rtype: Bool
        '''
        if type(dt) == datetime.date:
            return True
        return False


    def id_isvalid(self, id: int) -> bool:
        '''This validates the id as an int.

        PARAMETERS
        ________________________________________________________________
        :param id: an input to validate as an int for id 

        RETURNS
        ________________________________________________________________
        :returns: True for valid, else False
        :rtype: bool
        '''
        if type(id) == int:
            return True
        return False

    def set_id(self, id : int):
        '''
        This validates the input and sets if valid, else ValueError

        PARAMETERS
        ________________________________________________________________
        :param id: an input to set as an id (int type) 
        '''
        if ( self.id_isvalid(id) ):
            self.id = id
        else:
            raise ValueError("An id must be a valid int.")

    def uniqueid_isvalid(self, uid: object) -> bool:
        '''This validates the uid as an int.

        PARAMETERS
        ________________________________________________________________
        :param uid: an input to validate as a uuid4 for uid 

        RETURNS
        ________________________________________________________________
        :returns: True for valid, else False
        :rtype: bool
        '''
        if type(uid) == type(uuid.uuid4()):
            return True
        return False

    def set_uid(self, uid: object):
        '''
        This validates the input and sets if valid, else ValueError

        PARAMETERS
        ________________________________________________________________
        :param uid: an input to set 
        '''
        if ( self.uniqueid_isvalid(uid) ):
            self.unique_id = uid
        else:
            raise ValueError( "A unique_id must be a valid uuid4." )

    def set_offensedate(self, dt: object):
        '''
        This validates the input and sets if valid, else ValueError

        PARAMETERS
        ________________________________________________________________
        :param d: an input to set as a (offense)date 
        '''
        if ( self.date_isvalid(dt) ):
            self.offense_date = dt
        else:
            raise ValueError("A date must be a datetime.date.")

    def set_dispositiondate(self, dt: object):
        '''
        This validates the input and sets if valid, else ValueError

        PARAMETERS
        ________________________________________________________________
        :param d: an input to set as a (offense)date 
        '''
        if ( self.date_isvalid(dt) ):
            self.disposition_date = dt
        else:
            raise ValueError("A date must be a datetime.date.")

    def crime_isvalid(self, crime: object) -> bool:
        '''This validates the crime as a crime object.

        PARAMETERS
        ________________________________________________________________
        :param crime: an input to validate as a crime 

        RETURNS
        ________________________________________________________________
        :returns: True for valid, else False
        :rtype: bool
        '''
        if type(crime) == Crime:
            return True
        return False

    def set_crime( self, crime: object ):
        '''
        This validates the input and sets if valid, else ValueError

        PARAMETERS
        ________________________________________________________________
        :param crime: an input to set 
        '''
        if self.crime_isvalid(crime):
            self.crime = crime
        else:
            raise ValueError( "A crime must be a valid Crime instance." )
