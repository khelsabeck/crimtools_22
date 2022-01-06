'''
file    habitualmachine.py
author  Keith Helsabeck

________________________________________________________________________
This calculates whether a defendant is eligible for habitual felon 
status in NC (see also UML in docs).

Habitual Felony in NC:
Habitual status is an OPTIONAL status in NC sentencing and can allow a 
prosecutor and judge to raise the sentence of a felony crime to a 
sentence corresponding with a felony offense four classes higher 
(up to C at maximum) than the actual crime. 

A defendant is eligible for habitual status if and only if:
(1) The Defendant has had three or more prior sequential felonies 
and convictions for eligible felonies. In each case the offense date 
for crime n+1 must occur after the conviction date of crime n.
(2) Only one of crime can count if the Defendant was under 18.
'''
from .collections import Charge_Collection
from .dumwaiter import Dumbwaiter
from itertools import chain

# #------- Base State:------------------
class State:
    '''
    Base state for the HabitualMachine FSM. 
    
    This is the template from which the states inherit. Each should use
    the on_event function, taking a charge_collection, a dumbwaiter,
    and the index of the conviction date being run.
    '''
    def on_event(self, colx: object, dumbwaiter: object, index: int):
        '''
        PARAMETERS:
        ________________________________________________________________
        :param colx: the Charge_Collection Instance
        :param dumwaiter: a Dumbwaiter instance (context for hab felons)
        :param index: index of convictiondate in colx.cons_bydate

        RETURN:
        ________________________________________________________________
        :return: the integer 0 in base state (for testing)
        :rtype: int
        '''
        return 0

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__

    def is_qualified(self, c: object) -> bool:
        '''
        returns true if conviction is sufficiently serious for habitual
        felony.

        Two of these are pedantic exceptions from within the statutes
        themselves (both habitual misdemeanors whose statutes state
        that they shall not count as felonies for other habitual §s).

        PARAMETERS:
        ________________________________________________________________
        :param c: a Charge object to test

        RETURN:
        ________________________________________________________________
        :return: True if the c is qualified for hab felony
        :rtype: bool
        '''
        if not c.convicted or \ 
            c.crime.valid_classes[c.crime.crimeclass] < 5 or\
            "14-7.31" in c.crime.statuts or\
            "14-33.2" in c.crime.statuts:
            return False
        return True

# # #------- These are the concrete states:------------------
class StartState(State):
    '''
    This is the starting state for a state machine made to determine 
    if a Defendant is eligible for status as a habitual felon in NC. 
    It runs scripts to get rid of any non-eligible crimes. Some of 
    the rules are pedantic (see 
    https://www.sog.unc.edu/sites/www.sog.unc.edu/files/-
    reports/aojb0804.pdf).
    '''
    def on_event(self, colx: object, dumbwaiter: object, index: int): 
        '''
        PARAMETERS:
        ________________________________________________________________
        :param colx: the Charge_Collection Instance
        :param dumwaiter: a Dumbwaiter instance (context for hab felons)
        :param index: index of convictiondate in colx.cons_bydate

        RETURN:
        ________________________________________________________________
        :return: the next state's on_event() method (State object)
        :rtype: State
        '''
        for condate in colx.cons_bydate:
            # get list of felonies from a given date:
            felonylist = chain.from_iterable(condate.convictions[5:])
            for f in felonylist:
                if self.is_qualified(f):
                    dumbwaiter.habcons.append(f)
                    return StrikeOne().on_event(colx, dumbwaiter, index)
            else: # no qualified felony found for THIS date
                index += 1
        return FinishedState().on_event(colx, dumbwaiter, index)

class StrikeOne(State):
    '''
    StrikeOne represents the state where there is one confirmed felony
    conviction. 
    
    METHOD:
    ____________________________________________________________________
    :method on_event: transitions to StrikeTwo or Finished
    '''
    def on_event(self, colx:list, dumbwaiter: object, index: int): 
        '''
        This runs the logic of determining the next transition. 

        Next transition to StrikeTwo requires: 
        (1) a qualified conviction
        (2) the conviction's offense date must happen after the prior 
        conviction date
        (3) the D must be 18 at the time of the second/sequential 
        conviction's offense date.
        Otherwise, transition to FinishedState

        PARAMETERS:
        ________________________________________________________________
        :param colx: the Charge_Collection Instance
        :param dumwaiter: a Dumbwaiter instance (context for hab felons)
        :param index: index of convictiondate in colx.cons_bydate

        RETURN:
        ________________________________________________________________
        :return: the next state's on_event() method (State object)
        :rtype: State
        '''
        for colx.cons_bydate in range(index, len(colx.cons_bydate)):
            # get list of felonies from a given date:
            conlists = colx.cons_bydate[index].convictions[5:]
            felonylist = chain.from_iterable(conlists)
            for f in felonylist:
                if self.is_qualified(f):
                    dumbwaiter.habcons.append(f)
                    return StrikeTwo().on_event(colx, dumbwaiter, index)
            else: # no qualified felony found for THIS date
                index += 1
        return FinishedState().on_event(colx, dumbwaiter, index)

class StrikeTwo(State): 
    '''
    StrikeOne represents the state where there is one confirmed felony
    conviction. 
    
    METHOD:
    ____________________________________________________________________
    :method on_event: transitions to StrikeTwo or Finished
    '''
    def on_event(self, colx: object, dumbwaiter: object, index: int):
        '''
        This runs the logic of determining the next transition. 

        Next transition to StrikeTwo requires: 
        (1) a qualified conviction
        (2) the conviction's offense date must happen after the prior 
        conviction date
        (3) the D must be 18 at the time of the second/sequential 
        conviction's offense date.
        Otherwise, transition to FinishedState

        PARAMETERS:
        ________________________________________________________________
        :param colx: the Charge_Collection Instance
        :param dumwaiter: a Dumbwaiter instance (context for hab felons)
        :param index: index of convictiondate in colx.cons_bydate

        RETURN:
        ________________________________________________________________
        :return: the next state's on_event() method (State object)
        :rtype: State
        '''
        for colx.cons_bydate in range(index, len(colx.cons_bydate)):
            # get list of felonies from a given date:
            conlists = colx.cons_bydate[index].convictions[5:]
            felonylist = chain.from_iterable(conlists)

            for f in felonylist:
                if self.is_qualified(f) and \
                    dumbwaiter.offensedate_iseligible(f.offense_date):
                    dumbwaiter.habcons.append(f)
                    return StrikeThree().on_event(colx, dumbwaiter, index)
            else: # no qualified felony found for THIS date
                index += 1
        return FinishedState().on_event(colx, dumbwaiter, index)

class StrikeThree(State):
    '''
    This is the state where a Defendant is habitual.
        
    METHOD:
    ____________________________________________________________________
    :method on_event: modifies values and transitions to Finished
    '''

    def on_event(self, colx: object, dumbwaiter: object, index: int):
        '''
        Mark the D as habitual and set the date at which D is habitual,
        then transition to the Finished State.

        PARAMETERS:
        ________________________________________________________________
        :param colx: the Charge_Collection Instance
        :param dumwaiter: a Dumbwaiter instance (context for hab felons)
        :param index: index of convictiondate in colx.cons_bydate

        RETURN:
        ________________________________________________________________
        :return: the next state's on_event() method (State object)
        :rtype: State
        '''
        dumbwaiter.set_habeligible(True)
        dispo = colx.cons_bydate[index].disposition_date
        dumbwaiter.set_date_eligible(dispo)

        return FinishedState().on_event(convictions, dumbwaiter)

class FinishedState(State):
    '''
    Processing is finished.
        
    METHOD:
    ____________________________________________________________________
    :method on_event: modifies values and returns self
    '''
    def on_event(self, colx: object, dumbwaiter: object, index: int):
        '''
        mark the dumbwaiter to show the machine ran successfully.

        PARAMETERS:
        ________________________________________________________________
        :param colx: the Charge_Collection Instance
        :param dumwaiter: a Dumbwaiter instance (context for hab felons)
        :param index: index of convictiondate in colx.cons_bydate

        RETURN:
        ________________________________________________________________
        :return: the next state's on_event() method (State object)
        :rtype: State
        '''
        self.dumbwaiter = dumbwaiter
        self.dumbwaiter.has_run = True
        return self

#--------- The actual state machine itself:-----------------
class HabitualMachine:
    '''
    HabitualMachine runs the calculation of whether the D is 
    habitual and at what date based on the D and the charges.

    ATTRIBUTES:
    ____________________________________________________________________
    :attr state: This is the state the FSM is in now
    :attr points: (property) number of points in record
    :attr level: (property) felony record level (1-6)

    METHODS:
    ____________________________________________________________________
    :method date_iseligible: takes offense date and ret T if eligible

    USE:
    ____________________________________________________________________
    Make a Charge_Collection with all of a Defendant's convictions, 
    and the Defendant's birthdate (datetime.date). The crime, statute,
    offense date, and disposition date fields must be included and 
    accurate for a complete assessment of whether the D is habitual.
    Then:
    habmachine = HabitualMachine(crim_record, birthdate)
    habmachine.hab_eligible     # will be true if eligible
    habmachine.date_eligible    # will say when D became eligible
    '''
    def __init__(self, colx: object, bd: object):
        self.state = StartState() 
        dumbwaiter = Dumbwaiter(bd)
        self.state.on_event(convictions, dumbwaiter, 0)
        self.hab_eligible = self.state.dumbwaiter.hab_eligible
        self.date_eligible = self.state.dumbwaiter.date_eligible

    def date_iseligible(self, offense_date: object):
        '''
        After running a defendant's record, this takes a subsequent 
        conviction/crime's offense date and returns whether it is eligible 
        for habitual status.'''
        dw = self.state.dumbwaiter
        return dw.offensedate_iseligible(offense_date)