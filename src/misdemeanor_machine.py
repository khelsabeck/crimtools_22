'''
file    misdemeanor_machine.py
author  Keith Helsabeck

________________________________________________________________________
This calculates a misdemeanor record.

Midemeanor Record in NC:
0 prior convictions (felony or misdemeanor) -> Misdemeanor Level 1
1+ conviction (F or M on seperate dates) -> Misdemeanor Level 2
4+ convictions (F or M on seperate dates) -> Misdemeanor Level 3
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
        Determines next trans: 1+ convictions->HubState; 0->Finished

        PARAMETERS:
        ________________________________________________________________
        :param colx: the Charge_Collection Instance
        :param pts: num of misdemeanor pts
        :param index: index of convictiondate in colx.cons_bydate

        RETURN:
        ________________________________________________________________
        :return: the integer 0
        :rtype: int
        '''
        return 0 

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__

# #------- These are the concrete states:------------------
class StartState(State):
    '''
    Start of FSM for running misdemeanor record.

    If there are no prior convictions, return FinishedState 
    If there are priors, transition to 

    ATTRIBUTES:
    ____________________________________________________________________
    :attr pts: num of points for felony records (starting at 0)
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
        Determines next transit'n: convictions-> HubState. 0-> Finished

        PARAMETERS:
        ________________________________________________________________
        :param colx: the Charge_Collection Instance
        :param pts: num of felony points
        :param index: index of convictiondate in colx.cons_bydate
        '''
        colx.groupby_convictiondate()
        if type(colx.cons_bydate) == list \
            and len(colx.cons_bydate) == 0:
            return FinishedState().on_event(colx, pts, index)

        elif type(colx.cons_bydate) == list \
            and len(colx.cons_bydate) >= 1: 
            return HubState().on_event(colx, pts, index)
