'''
file    crime.py
author  Keith Helsabeck

This is the file crime.py, for holding the class Crime. 
Crime represents a particular criminal statute/law that the State can 
charge a Defendant with committing. A crime should have a simple 
sequential id, a UID,a statute, a description, and its class.
'''
import typing
import uuid

class Crime:
    '''
    Crime represents a statutory/common law crime that the State can 
    charge a Defendant with committing. 

    CLASS ATTRIBUTES: 
    ____________________________________________________________________
    :attr valid_classes: a set {} of all valid classes

    INSTANCE ATTRIBUTES: 
    ____________________________________________________________________
    :attr id: (int) a simple sequential id
    :attr unique_id: a uuid4 object 
    :attr statute: str up to 50 chars (eg: "§14-72")
    :attr description: a string up to 50 chars for the crime's name  
    :attr crimeclass: str lte 50 chars (eg: "Class F Felony")
    :attr valid_classes: strs representing all valid crime classes

    METHODS: 
    ____________________________________________________________________
    :crimeclass_isvalid: ret True if input is a valid class, else False
    :crimestring_isvalid: ret True if input is a valid description/stat

    :set_crimeclass: sets crimeclass and ret T if set, else F
    :set_statute: sets statute and ret T if set, else F
    :set_description: sets description and ret T if set, else F
    :set_id: sets id and ret T if set, else F
    '''

    valid_classes = [
        "Infraction", "Class 3 Misdemeanor", "Class 2 Misdemeanor", 
        "Class 1 Misdemeanor", "Class A1 Misdemeanor",
        "Class I Felony", "Class H Felony", "Class G Felony", 
        "Class F Felony", "Class E Felony", "Class D Felony",
        "Class C Felony", "Class B1 Felony", "Class B2 Felony", 
        "Class A Felony"
    ]

    def __init__(self):
        self.id = None
        self.unique_id = None
        self.statute = ""
        self.description = ""
        self.crimeclass = ""

    def crimeclass_isvalid(self, s:str) -> bool:
        '''
        validates input s as a crime class. 

        PARAMETERS: 
        ______________________________________________________________
        :param s: a string to validate as a crime class (NC) 

        :returns: True for valid, else False
        :rtype: bool
        '''
        if s in Crime.valid_classes:
            return True
        return False

    def set_crimeclass( self, s:str ) -> bool:
        '''
        validates data and sets if valid. Returns T if set, else F

        PARAMETERS: 
        ______________________________________________________________
        :param s: a string to set as the crimeclass

        :returns: True if set, else False
        :rtype: bool
        '''
        if ( self.crimeclass_isvalid( s ) ):
            self.crimeclass = s
            return True
        else:
            raise ValueError(f"crimeclass invalid.")

    def crimestring_isvalid(self, s:str) -> bool:
        '''
        validates input s as a description or statute. 

        PARAMETERS: 
        ______________________________________________________________
        :param s: a string to validate as a description or statute

        :returns: True for valid, else False
        :rtype: bool
        '''
        if type(s) == str and len(s) <= 50:
            return True
        return False

    def set_statute( self, s:str ):
        '''
        validates data and sets if valid, or raises ValueError w msg

        PARAMETERS: 
        ______________________________________________________________
        :param s: a string to set as the statute
        '''
        if ( self.crimestring_isvalid( s ) ):
            self.statute = s
            return True
        else:
            raise ValueError("A statute must be str lte 50 chars.")

    def set_description( self, s:str ):
        '''
        validates data and sets if valid. Returns T if set, else F

        PARAMETERS: 
        ______________________________________________________________
        :param s: a string to set as the description
        '''
        if ( self.crimestring_isvalid( s ) ):
            self.description = s
        else:
            raise ValueError("A description must be str lte 50 chars.")

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
            raise ValueError( "A unique_id must be a valid uuid4." )

