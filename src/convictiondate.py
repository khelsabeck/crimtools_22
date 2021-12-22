'''
file    convictiondate.py
author  Keith Helsabeck

This is the file convictiondate.py, for keeping multiple charges
convicted on a given date in order, grouped as a 2-d list with the 
inner lists holding crimes of the same class in order.
'''
import typing
import uuid
from .charge import Charge
from .crime import Crime
import datetime

class ConvictionDate:
    '''
    Model of a single date with one or more convictions. Each
    conviction needs a disposition_date, and these must all match.

    ATTRIBUTES:
    ____________________________________________________________________
    :attr disposition_date: (datetime.date)--date for all these charges
    :attr convictions: a list containing the convictions

    METHODS:
    ____________________________________________________________________
    :method add: adds a charge in sorted order
    :method highest: returns the highest-level (list of) charges
    '''

    def __init__(self, date: object):
        '''This initializes the conviction date structure.
        
        A new convictiondate should know its date and its charges. The
        purpose of this is not use/reuse as a general-purpose data
        storage object for charges. The only reason for convictiondate
        data objects is in analysis of a person's criminal record. 
        Every time a record is analyzed, a new set of objects should be
        created for the FSM to analyze the record from a clean slate.
        '''
        self.convictions = [ [] for x in Crime.valid_classes ]
        self.set_date( date )
        
    def set_date(self, date: object):
        '''This validates the date is a datetime.date and if so, sets
        the instance var self.disposition_date to date
        
        PARAMETERS:
        ________________________________________________________________
        :param date: the date to set as self.disposition_date in init
        '''
        if ( type(date) == datetime.date ):
            self.disposition_date = date

    def add(self, charge: object):
        '''This adds a charge to the inner list corresponding to the
        crime's class.

        This validates the input's type, and that it has a conviction 
        date & adds the charge to the appropriate inner list (the one 
        corresponding to the crime's class).

        PARAMETERS:
        ________________________________________________________________
        :param charge: a charge to add to self.convictions
        '''
        if  type(charge) != Charge \
            or type(charge.disposition_date) != datetime.date\
            or charge.convicted == False\
            or type(charge.crime) != Crime\
            or charge.crime.crimeclass not in Crime.valid_classes\
            or charge.disposition_date != self.disposition_date:
            raise ValueError("add() needs Charge with right date.")
        count = 0
        for crimeclass in Crime.valid_classes:
            if crimeclass == charge.crime.crimeclass:
                self.convictions[count].append(charge)
                break
            else:
                count += 1

    def highest(self) -> list:
        '''returns a list of the highest-level charges.

        This validates the input's type, and that it has a conviction 
        date & adds the charge to the appropriate inner list (the one 
        corresponding to the crime's class).

        RETURNS:
        ________________________________________________________________
        :returns: Highest charge in this data structure
        :rtype: list (of Charges)
        '''
        reversed = copy(self.convictions).reverse()
        for conlist in reversed:
            if conlist != []:
                return conlist 