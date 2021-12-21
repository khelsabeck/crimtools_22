# crimtools_22
This is a an open source repo for lawyers, and the purpose is to help
attorneys visually explain and model criminal justice issues such as
calculating jail credit, sentencing, and whether a Defendant is elligible
for special statuses such as habitual felon.

__CONTENTS:__
--Defendant: a model for a Defendant accused of a crime
--Crime: a model of a crime the State charges against a Defendant
--Charge: a model of a criminal charge (count) against D (has crime)
--ConvictionDate: a date with 1+ charges that have been convicted
--Charge_Collection: Collection for charges/convictiondates

__TESTING:__
I am using pytest and pytest-cov in testing this library, especially the
following command:
pytest --cov=src --cov-report term-missing

