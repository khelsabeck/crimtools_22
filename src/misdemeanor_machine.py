'''
file    misdemeanor_machine.py
author  Keith Helsabeck

________________________________________________________________________
This calculates a misdemeanor record.

Midemeanor Record in NC:
0 prior convictions (felony or misdemeanor) ---> Misdemeanor Level 1
1-4 conviction (F or M on seperate dates) -----> Misdemeanor Level 2
over 4 convictions (F or M on seperate dates) -> Misdemeanor Level 3
'''
from .collections import Charge_Collection

class State:
    '''
    This is the base state for a misdemeanor record. 

    Misdemeanor records for a person with no NC criminal history start at 
    Level 1 with 0 points.

    ATTRIBUTES:
    ____________________________________________________________________
    :attr pts: num of points for misdemeanor records (starting at 0)
    :attr index: current index (which convictiondate we are analyzing)
    :attr level: current record level (starting at 1)

    METHODS:
    ____________________________________________________________________
    :method on_event: takes colx and pts --> State.on_event()
    :method repr: returns representation of this state's class name
    :method str: returns representation of this state's class name
    '''
    def __init__(self):
        self.pts = 0
        self.index = 0
        self.level = 1

    def on_event(self, colx: object, pts: int, index: int) -> int: 
        '''
        Determines next transition.

        PARAMETERS:
        ________________________________________________________________
        :param colx: the Charge_Collection Instance
        :param pts: num of misdemeanor pts
        :param index: index of convictiondate in colx.cons_bydate

        RETURN:
        ________________________________________________________________
        :return: the integer 0 for the base state
        :rtype: int
        '''
        return 0 

    def is_qualified(self, conv: object) -> bool:
        '''
        Determines whether the conviction qualifies for a misdem point.

        PARAMETERS:
        ________________________________________________________________
        :param conv: a convicted Charge object to analyze

        RETURN:
        ________________________________________________________________
        :return: True if the conviction is qualified for misd points
        :rtype: bool
        '''
        if type(conv) == Charge and \
            conv.convicted == True and \
            conv.crime.crimeclass != "Infraction":
            return True
        return False

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__

# #------- These are the concrete states:------------------
class StartState(State):
    '''
    Start of FSM for running misdemeanor record.

    TRANSITIONS:
    ____________________________________________________________________
    Transition to LevelOne (automatic)

    ATTRIBUTES:
    ____________________________________________________________________
    :attr pts: num of points for misdemeanor records (starting at 0)
    :attr index: current index (which convictiondate we are analyzing)
    :attr level: current record level (starting at 1)

    METHODS:
    ____________________________________________________________________
    :method on_event: takes charge_collection & pts -> State.on_event()
    :method repr: returns representation of this state's class name
    :method str: returns representation of this state's class name
    '''
    def on_event(self, colx: object, pts: int, index: int) -> object: 
        '''
        Determines next transitions (straight to LevelOne)

        PARAMETERS:
        ________________________________________________________________
        :param colx: the Charge_Collection Instance
        :param pts: num of misdemeanor record points
        :param index: index of convictiondate in colx.cons_bydate
        '''
        colx.groupby_convictiondate()
        return LevelOne().on_event(colx, pts, index)

class LevelOne(State):
    '''
    First Level in Misdemeanors. Represents a Defendant with 0 qualified
    prior convictions.

    TRANSITIONS:
    ____________________________________________________________________
    Trans to self if condate has no qualified convs (but more condates)
    Transition to LevelTwo if there's a qualified conviction
    Transition to FinishedState if no quals & no more condates

    ATTRIBUTES:
    ____________________________________________________________________
    :attr pts: num of points for misdemeanor records (starting at 0)
    :attr index: current index (which convictiondate we are analyzing)
    :attr level: current record level (starting at 1)

    METHODS:
    ____________________________________________________________________
    :method on_event: takes charge_collection & pts -> State.on_event()
    :method repr: returns representation of this state's class name
    :method str: returns representation of this state's class name
    '''
    def on_event(self, colx: object, pts: int, index: int) -> object: 
        '''
        Determines next transition (LevelTwo or Finished)

        PARAMETERS:
        ________________________________________________________________
        :param colx: the Charge_Collection Instance
        :param pts: num of misdemeanor record points
        :param index: index of convictiondate in colx.cons_bydate
        '''
        if type(colx.cons_bydate) == list \
            and len(colx.cons_bydate) == 0:
            return FinishedState().on_event(colx, pts, index)
        elif type(colx.cons_bydate) == list \
            and len(colx.cons_bydate) >= 1: 
            c = colx.cons_bydate[index].highest()[0]
            if self.is_qualified(c):
                return LevelTwo().on_event(colx, pts + 1, index + 1)
            return self.on_event(colx, pts, index + 1)

class LevelTwo(State):
    '''
    Second Level in Misdemeanors. Represents a Defendant with 1-4 
    qualified prior convictions.

    TRANSITIONS:
    ____________________________________________________________________
    Transition to self/LevelTwo upon convictions up to 4th
    Transition to LevelThree upon date of the 4th conviction
    Transition to FinishedState if no more qualified convictions

    ATTRIBUTES:
    ____________________________________________________________________
    :attr pts: num of points for misdemeanor records
    :attr index: current index (which convictiondate we are analyzing)
    :attr level: current record level (starting at 1)

    METHODS:
    ____________________________________________________________________
    :method on_event: takes charge_collection & pts -> State.on_event()
    :method repr: returns representation of this state's class name
    :method str: returns representation of this state's class name
    '''
    def on_event(self, colx: object, pts: int, index: int) -> object: 
        '''
        Determines next transition (self, LevelThree, or Finished)

        PARAMETERS:
        ________________________________________________________________
        :param colx: the Charge_Collection Instance
        :param pts: num of misdemeanor record points
        :param index: index of convictiondate in colx.cons_bydate
        '''
        self.level = 2
        if type(colx.cons_bydate) == list \
            and len(colx.cons_bydate) == 0:
            return FinishedState().on_event(colx, pts, index)
        elif type(colx.cons_bydate) == list and \
            len(colx.cons_bydate) > 1 and \
            self.pts < 5: 
            c = colx.cons_bydate[index].highest()[0]
            if self.is_qualified(c):
                return self.on_event(colx, pts + 1, index + 1)
            return self.on_event(colx, 0, index + 1)
        elif type(colx.cons_bydate) == list and \
            len(colx.cons_bydate) > 1 and \
            self.pts >= 5: 
            return FinishedState().on_event(colx, pts, index)

class LevelThree(State):
    '''
    Third Record Level in Misdemeanors. Represents a Defendant with 4 
    qualified prior convictions.

    TRANSITIONS:
    ____________________________________________________________________
    Transition to FinishedState (automatic)

    ATTRIBUTES:
    ____________________________________________________________________
    :attr pts: num of points for misdemeanor records
    :attr index: current index (which convictiondate we are analyzing)
    :attr level: current record level (starting at 1)

    METHODS:
    ____________________________________________________________________
    :method on_event: takes charge_collection & pts -> State.on_event()
    :method repr: returns representation of this state's class name
    :method str: returns representation of this state's class name
    '''
    def on_event(self, colx: object, pts: int, index: int) -> object: 
        '''
        Determines next transition (Finished)

        PARAMETERS:
        ________________________________________________________________
        :param colx: the Charge_Collection Instance
        :param pts: num of misdemeanor record points
        :param index: index of convictiondate in colx.cons_bydate
        '''
        self.level = 3
        if type(colx.cons_bydate) == list \
            and len(colx.cons_bydate) == 0:
            return FinishedState().on_event(colx, pts, index)

class FinishedState(State):
    '''
    This is the state for the FSM when finished.

    TRANSITIONS:
    ____________________________________________________________________
    None

    ATTRIBUTES:
    ____________________________________________________________________
    :attr pts: num of points for misdemeanor records
    :attr index: current index (which convictiondate we are analyzing)
    :attr level: current record level (starting at 1)

    METHODS:
    ____________________________________________________________________
    :method on_event: takes charge_collection & pts -> State.on_event()
    :method repr: returns representation of this state's class name
    :method str: returns representation of this state's class name
    '''
    def on_event(self, colx: object, pts: int, index: int) -> object: 
        '''
        Determines next transition (Finished)

        PARAMETERS:
        ________________________________________________________________
        :param colx: the Charge_Collection Instance
        :param pts: num of misdemeanor record points
        :param index: index of convictiondate in colx.cons_bydate
        '''
        if type(colx.cons_bydate) == list \
            and len(colx.cons_bydate) == 0:
            return self

# --------- The State Machine:-----------------
class MisdemeanorRecordMachine:
    '''
    State machine for calculating misdemeanor record level.

    USE:
    ____________________________________________________________________
    Pass a collection instance for a defendant to the on_event() method.
    It will calculate the points and level of your defendant. Once the 
    FSM has run, the level attr of this machine will be the misd level.

    ATTRIBUTES:
    ____________________________________________________________________
    :attr state: This is the state the FSM is in now
    :attr level: (property) misdemeanor record level (1-3)
    '''
    def __init__(self, colx: object):
        self.state = StartState() # starting state set
        self.state = self.state.on_event(colx, 0, 0)

    @property
    def level(self):
        return self.state.level