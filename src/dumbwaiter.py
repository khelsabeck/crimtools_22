'''
file    dumbwaiter.py
author  Keith Helsabeck

This is the module dumbwaiter for serving as a context
object in writing state machines.
'''
import typing
from datetime import date

class Dumbwaiter:
    '''
    Dumbwaiter is a context object for the HabitualMachine to pass
    around between its state objects.

    ATTRIBUTES:
    ____________________________________________________________________
    :attr habcons: a list of habitual felony convictions
    :attr habeligible: boolean of whether eligible for hab felon status
    :attr dateeligible: date when eligible (None by default)
    :attr birthdate: the defendant's birthdate (needed in calculations)
    :attr has_run: boolean -- T if this dumbwaiter has run through FSM

    METHODS:
    ____________________________________________________________________
    :method set_birthdate: validates and sets a birthdate
    :method set_habeligible: validates and sets a birthdate
    :method over18_on_date: validates if d >= 18 on input date
    :method eighteenth_birthdate: property--returns 18th bday
    :method set_date_eligible: takes date (from fsm) sets date eligible
    :method offensedate_iseligible: takes dt & ret T if eligible else F
    '''
    def __init__(self, birthdate: object):
        self.habcons = []
        self.set_hab_eligible(False)
        self.date_eligible = None
        self.set_birthdate(birthdate)
        self.has_run = False  # when run, set True

    def set_birthdate(self, bd: object):
        '''This should set the birthdate value IFF bd is a valid datetime 
        date object.
        
        PARAMETERS:
        ____________________________________________________________________
        :param bd: validates the birthdate's type
        '''
        if (type(bd) == date):
            self.birthdate = bd
        else:
            raise ValueError("The D's birthdate is a prerequisite for \
habitual felon analysis. Must be datetime.date-type.")

    def set_habeligible(self, eligible: bool):
        '''This should set hab_eligible if the input value is a boolean
        
        PARAMETERS:
        ____________________________________________________________________
        :param bd: validates the birthdate's type

        '''
        if type(eligible) == bool:
            self.habeligible = eligible
        else:
            raise ValueError("The eligible value must be a boolean.")

    def over18_on_date(self, dt: object):
        '''This takes a datetime date object and determines if defendant 
        was 18 on that date. Wrong type raises ValueError.
        
        PARAMETERS:
        ____________________________________________________________________
        :param dt: datetime.date obj to run against dumbwaiter's D's bday
        '''
        if type(dt) != date:
            raise ValueError("The method over18_on_date() in Dumbwaiter \
requires a datetime date as a parameter.")
        if dt >= self.eighteenth_birthdate:
            return True
        return False

    @property
    def eighteenth_birthdate(self) -> object:
        '''This uses the birthdate attr and returns the 18th birthdate.
        
         RETURN:
        ______________________________________________________________
        :returns: 18th birthdate (of defendant)
        :rtype: datetime.date

        '''
        eighteenth = date(
            self.birthdate.year + 18, 
            self.birthdate.month, 
            self.birthdate.day
        )
        return eighteenth

    def set_date_eligible(self, dt: object):
        '''sets the date at which defendant is habitual eligible.

        PARAMETERS:
        ____________________________________________________________________
        :param dt: datetime.date obj to determine eligibility
        '''
        if type(dt) == date:
            self.date_eligible = conviction_date
        else:
            raise ValueError("The method set_date_eligible() in Dumbwaiter \
requires a datetime.date input as a parameter.")

    def offensedate_iseligible(self, offense_date: object):
        '''determines whether a conviction eligible for habitual status.
        
        PARAMETERS:
        ____________________________________________________________________
        :param dt: datetime.date of offense to determine whether eligible
        '''
        if self.date_eligible != None and offense_date > self.date_eligible:
            return True
        else:
            return False