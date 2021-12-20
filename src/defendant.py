'''
file    defendant.py
author  Keith Helsabeck

This is the file defendant.py, for holding the class Defendant. 
Defendant represents a person charged with crime(s).

'''
import typing
import uuid
import datetime

class Defendant:
    '''
    Defendant represents a person charged with (a) crime(s).
    
    ATTRIBUTES:
    ____________________________________________________________________
    :attr id: (int) a simple sequential id
    :attr unique_id: a uuid4 object 
    :attr firstname: 50-char max str for first name
    :attr lastname: 50-char max str for last name
    :attr birthdate: datetime date obj for bday

    METHODS
    ____________________________________________________________________
    :birthdate_isvalid: True if a birthdate valid, else False
    :name_isvalid: True if name valid, else False

    '''
    def __init__(self):
        self.id = None
        self.unique_id = None
        self.firstname = ""
        self.lastname = ""
        self.birthdate = None

    def name_isvalid(self, s:str) -> bool:
        '''This confirms that a name is a valid string of valid length

        PARAMETERS
        ________________________________________________________________
        :param s: a string to validate as a firstname 

        RETURNS
        ________________________________________________________________
        :returns: True for valid, else False
        :rtype: bool'''
        if ( type(s) == str ) and len(s) <= 50:
            return True
        return False

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def birthdate_isvalid(self, bd: object) -> bool:
        '''This validates the birthdate as a datetime.date.

        PARAMETERS
        ________________________________________________________________
        :param bd: an input to validate as a (birth)date 

        RETURNS
        ________________________________________________________________
        :returns: True for valid, else False
        :rtype: bool
        '''
        if type(bd) == type(datetime.date):
            return True
        return False