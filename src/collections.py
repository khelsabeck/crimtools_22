'''
file    convictiondate.py
author  Keith Helsabeck

These are the collections (for a D's pending charges and crim record). 

NB: a D can be charged more than once with crimes/charges having 
identical data. IE: John Doe is charged with two counts of larceny on 
the same date from the same incident, or Jane Doe is charged with 
resisting two officers out of the same incident, and with assaulting 
a third.
'''
import typing
from .charge import Charge
from .convictiondate import ConvictionDate

class Charge_Collection:
    '''Custom collection for making and storing charges. 
    
    ATTRIBUTES:
    ____________________________________________________________________
    :attr charges: a list of charges

    METHODS:
    ____________________________________________________________________
    :method add_charge: adds a charge to the list
    :method remove_charge: removes a charge from list by index
    :method reset_charges: resets charges as blank list
    :method is_in: takes charge, returns T if charge in charges else F
    '''

    def __init__(self):
        self.reset_charges()    #new empty list (self.charges)

    def reset_charges(self):
        '''This sets charges as an empty list.'''
        self.charges = []
    
    def add_charge(self, charge : object):
        '''This adds a pending charge after validation.'''
        if Charge == type(charge):
            self.charges.append(charge)
        else:
            raise ValueError("Only valid Charge objects may be added.")

    def remove_charge(self, index : int):
        '''This deletes a charge from the charges by index. 

        There is no remove by value because there can be multiple 
        identical charges  with same data for a given defendant. 
        IE: John Doe is charged with two counts of larceny on the same 
        date and location.

        PARAMETERS
        ________________________________________________________________
        :param index: the index/position in self.charges
        '''
        try:
            del self._charges[index]
        except:
            raise ValueError("This charge is not in _charges.")

    def is_in( self, charge : object ) -> bool:
        '''This returns True if the charge is present else False.

        PARAMETERS
        ________________________________________________________________
        :param charge: the charge is present already

        RETURNS
        ________________________________________________________________
        :returns: True if charge in, else False
        :rtype: bool
        '''
        if charge in self.charges:
            return True
        else:
            return False

class Pending_Charges( Charge_Collection ):
    '''This is the custom collection model for a defendant's pendings.

    Pending_Charges has all the attributes and methods of the parent,
    and also an extra method for sorting  self.charges list by offense
    date. It holds charges not yet resolved.
    
    ATTRIBUTES:
    ____________________________________________________________________
    :attr charges: a list of charges

    METHODS:
    ____________________________________________________________________
    :method add_charge: adds a charge to the list
    :method remove_charge: removes a charge to the list
    :method reset_charges: resets charges as blank list
    :method is_in: takes charge, returns true if charge in charges
    :method sort_byoffensedate: sorts self.charges by date offense
    '''

    def __init__(self):
        super().__init__(self)

    def sort_byoffensedate(self):
        '''This sorts the collection by the dates of offense of the 
        charges from earliest to latest and returns a copy.
        '''
        self.charges.sort(key=lambda x: x.offense_date)

class Charges_Convicted(Charge_Collection):
    '''This is the custom collection model for convictions.
    
    Charges_Convicted has all of the attributes and methods of the 
    parent, and also has a method for sorting by conviction dates, 
    and another for grouping by conviction dates.
    These are convicted charges, and should (mostly) have conviction
    dates.
    
    ATTRIBUTES:
    ____________________________________________________________________
    :attr charges: a list of charges
    :attr unique_dates: a list of unique non-null conviction dates
    :attr convictions: a list of convictiondates, each with charges 

    METHODS:
    ____________________________________________________________________
    :method add_charge: adds a charge to the list 
    :method remove_charge: removes a charge from the list 
    :method reset_charges: resets charges as blank list 
    :method is_in: takes charge, returns true if charge in charges 
    :method sortby_conviction: sorts self.charges by conviction date
    :method datemaker: helper for groupby_convictiondate
    :method groupby_convictiondate: groups convs to convictiondates
    '''

    def __init__(self):
        super().__init__(self)

    def sortby_conviction(self):
        '''This sorts the collection by the conviction dates of the 
        charges from earliest to latest.
        '''
        self.charges.sort( key=lambda x: x.conviction_date )

    def datemaker(self):
        '''Helper for groupby_convictiondate().
        
        This creates a list of all the unique conviction dates.
        '''
        self.sortby_conviction()    # sorted in order
        self.unique_dates = [ 
            charge.disposition_date for  charge in sorted_charges \
            ( if charge.disposition_date != None and \
            charge.disposition_date not in self.unique_dates )
        ]

    def groupby_convictiondate(self):
        '''This groups the convicted charges in the collection by 
        the conviction dates and makes a list of convictiondate objects,
        one for each unique date. It populates these with the matching 
        convictions.'''
        self.datemaker()    # now self.unique_dates has uniques
        self.cons_bydate = [ 
            ConvictionDate(date) for date in self.unique_dates 
        ]
        for charge in self.charges:
            for idx, dt in self.unique_dates:
                if charge.disposition_date == dt:
                    self.cons_bydate[idx].add(charge)