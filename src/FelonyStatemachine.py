'''
file    FelonyStatemachine
author  Keith Helsabeck

This calculates a felony record in NC for the project/repo crimtools_22.

In order to calculate a felony record, we first count the number of 
points. 

1-point crimes: {Cl 1 misdemeanor under Ch 14,Cl A1 in Ch 14, 
Misdemeanor DWI (Ch 20), Misdemeanor Driving withLicense Revoked 
(revocation for impaired fffense) (Ch 20) }

2-point crimes: {H Felonies, I felonies}

4-point crimes: {E, F, and G felonies}

6-point crimes: {D, C, and B2 felonies}

9-point: {B1 felonies}

10-points: { A felonies }

Once the points are tallied from the record, determine the record
level according to this chart:

Points:         Level:
0-1 points      1
2-5             2
6-9             3
10-13           4
14-17           5
18+             6
'''

import typing
from .collections import Charge_Collection

class FelonyPointChart:
    '''Has a dict of crimes that qualify for felony record points.
    
    CLASS ATTRIBUTES:
    ____________________________________________________________________
    :class_attr crimes: list of crime classes that are eligible for pts
    :class_attr pointvals: dict of eligible classes & their point vals
    '''
    crimes = [  
                "Class 1 Misdemeanor", "Class A1 Misdemeanor", 
                "Class I Felony", "Class H Felony", "Class G Felony", 
                "Class F Felony", "Class E Felony", "Class D Felony", 
                "Class C Felony", "Class B1 Felony", "Class B2 Felony", 
                "Class A Felony" 
    ]
    pointvals = {
        "Class 1 Misdemeanor": 1,
        "Class A1 Misdemeanor": 1,
        "Class I Felony": 2,
        "Class H Felony": 2,
        "Class G Felony": 4,
        "Class F Felony": 4,
        "Class E Felony": 4,
        "Class D Felony": 6,
        "Class C Felony": 6,
        "Class B2 Felony": 6,
        "Class B1 Felony": 9,
        "Class A Felony": 10,
    }

#states: 
class State:
    '''
    This is the base state for a felony record. 

    Felony records for a person with no NC criminal history start at 
    Level 1 with 0 points.

    ATTRIBUTES:
    ____________________________________________________________________
    :attr pts: num of points for felony records (starting at 0)
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

    def on_event(self, colx: object, pts: int, index: int): 
        '''
        Determines next trans: 1+ convictions->HubState; 0->Finished

        PARAMETERS:
        ________________________________________________________________
        :param colx: the Charge_Collection Instance
        :param pts: num of felony pts
        :param index: index of convictiondate in colx.cons_bydate
        '''
        pass 

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__

# #------- These are the concrete states:------------------
class StartState(State):
    '''
    Start of FSM for running felony record.

    If there are no prior convictions, return FinishedState 
    If there are priors, ret ScreeningState (ditches ineligibles)

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
    def on_event(self, colx: object, pts: int, index: int)->object: 
        '''
        Determines next transition: 1+ convictions->HubState. 0->Finished

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
            and len(cons_bydate) >= 1: 
            return HubState().on_event(colx, pts, index)

        else:
            e = ErrorState()
            e.error = "There was an exception in the StartState. The \
parameter values are likely invalid."
            return e.on_event(colx, pts, index)

class HubState(State):
    '''
    This is the hub for choosing what to do with the next
    convictiondate.

    If the conviction at the convictiondate is M or Inf -> M_State 
    If the conviction at the convictiondate is F -> F_State 

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
    def on_event(self, colx: object, pts: int, index: int):
        '''
        Determines next transition: M -> M_State; F -> F_State

        PARAMETERS:
        ________________________________________________________________
        :param colx: the Charge_Collection Instance
        :param pts: num of felony points
        :param index: index of convictiondate in colx.cons_bydate
        '''
        if len(colx.cons_bydate) == index: #last conviction hit
            return FinishedState().on_event(colx, pts, index)

        con_date = colx.cons_bydate[index]
        for charge in con_date.convictions:
            if "Felony" in charge.crime_class:
                return F_State().on_event(colx, pts, index)

        return M_State().on_event(colx, pts, index) # no felonies

class M_State(State):
    '''
    This is the M_State for handling non-felony cases.

    If the conviction is eligible, index++, pts++ -> HubState 
    If the conviction is not, index++ -> HubState

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
    def on_event(self, colx:list, pts:int, index: int):
        convictions = colx.cons_bydate[index].highest()
        for c in convictions:
            if self.is_eligible(c):
                return HubState().on_event(sliced, pts + 1, index + 1)
        return HubState().on_event(sliced, pts, index + 1)
    
    def is_eligible(self, charge: object) -> bool:
        '''
        This tests whether a misdemeanor is eligible for a felony
        record point.

        PARAMETERS:
        ________________________________________________________________
        :param charge: the charge to test

        RETURNS:
        ________________________________________________________________
        :returns: True for eligible, else False
        :rtype: bool
        '''
        if type(charge) == None:
            return False
        if type(charge.crime) == Crime \
            and "A1" or "1" in charge.crime.crimeclass \
            and "20-" not in charge.crime.crimeclass:
            return True
        if type(charge.crime) == Crime \
            and ("20-141.4(a2)" in charge.crime.statute \
                or "20-138.1" in charge.crime.statute)\
                or "20-138.1" in charge.crime.statute:
            return True
        return False


class F_State(State):
    '''An eligible misdemeanor (Class 1 or A1) is worth one point. Multiple 
    misdemeanors on the same conviction date are capped at 1 point per day. 
    This state class should add a point to points and return to HubState.'''
    def on_event(self, colx: list, pts: int, index: int):
        convictions = colx.cons_bydate[index].highest()
        pts += FelonyPointChart.pointvals[convictions.crime.crimeclass]
        index += 1
        return HubState(colx, pts, index)

class FinishedState(State):
    '''This is the end of counting up the felonies'''
    def on_event(self, colx: object, pts: int, index: int):
        self.level = self.leveler(pts)
        self.colx = colx
        self.pts = pts
        return self

    def leveler(selt, pts: int):
        if pts < 2:
            return 1
        elif pts < 6:
            return 2
        elif pts < 10:
            return 3
        elif pts < 14:
            return 4
        elif pts < 18:
            return 5
        elif pts >= 18:
            return 6

class ErrorState(State):
    '''If there is an error in one of the states, ErrorState is likely 
    called.'''
    def on_event(self, convictions:list, points:int):
        self.level = "An error occured while caluclating the record."
        self.points = "An error occured while caluclating the record."
        return self

#--------- The State Machine:-----------------
class Felony_RecordMachine:
    '''
    FSM for calculating felony record level.

    ATTRIBUTES:
    ____________________________________________________________________
    :attr state: This is the state the FSM is in now
    :attr points: (property) number of points in record
    :attr level: (property) felony record level (1-6)
    '''
    def __init__(self):
        self.state = StartState() # starting state set
    
    def on_event(self, colx:object):
        self.state = self.state.on_event(colx, 0, 0)

    @property
    def points(self):
        return self.state.points

    @property
    def level(self):
        return self.state.level