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

    def set_firstname( self, s : str ):
        '''
        This validates the input and sets if valid, else ValueError

        PARAMETERS
        ________________________________________________________________
        :param s: an input to validate as a firstname
        '''
        if ( self.name_isvalid(s) ):
            self.firstname = s
        else:
            raise ValueError("A name must be a string, lte 50 char.")

    def set_lastname( self, s : str ):
        '''
        This validates the input and sets if valid, else ValueError

        PARAMETERS
        ________________________________________________________________
        :param s: an input to validate as a lastname

        '''
        if ( self.name_isvalid(s) ):
            self.lastname = s
        else:
            raise ValueError("A name must be a string, lte 50 char.")

    @property
    def fullname(self):
        if type(self.firstname) == str and type(self.lastname) == str \
            and len( self.firstname ) > 0 and len(self.lastname) > 0:
            return f"{self.firstname} {self.lastname}"
        else:
            return "Defendant"

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
        if type(bd) == datetime.date:
            return True
        return False

    def set_birthdate( self, bd : object ):
        '''
        This validates the input and sets if valid, else ValueError

        PARAMETERS
        ________________________________________________________________
        :param bd: an input to set as a (birth)date 
        '''
        if ( self.birthdate_isvalid(bd) ):
            self.birthdate = bd
        else:
            raise ValueError("A birthdate must be a datetime.date.")

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

    def set_id( self, id : int ):
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

    def set_uid( self, uid : object ):
        '''
        This validates the input and sets if valid, else ValueError

        PARAMETERS
        ________________________________________________________________
        :param uid: an input to set 
        '''
        if ( self.uniqueid_isvalid(uid) ):
            self.unique_id = uid
        else:
            raise ValueError("A unique_id must be a valid uuid4.")

