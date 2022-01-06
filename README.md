# crimtools_22 <br />

__SUMMARY:__ <br />
This is a an open source repo for lawyers, and the purpose is to help
attorneys visually explain and model criminal justice issues such as
calculating jail credit, sentencing, and whether a Defendant is elligible
for special statuses such as habitual felony status.<br />

__CONTENTS:__ <br />
--Defendant: a model for a Defendant accused of a crime<br />
--Crime: a model of a crime the State charges against a Defendant<br />
--Charge: a model of a criminal charge (count) against D (has crime)<br />
--ConvictionDate: a date (collection) with 1+ convicted charges<br />
--Charge_Collection: Collection for charges/convictiondates<br />
--Dumbwaiter: context object for FSMs<br />
--FelonyStatemachine: State machine for Running felony records<br />

__TESTING:__ <br />
I am using pytest and pytest-cov in testing this library, especially the
following command:<br />
pytest --cov=src --cov-report term-missing<br />

__DOCUMENTATION:__<br />
The documentation in the docs file includes UML diagrams for the data<br /> 
structures as well as the FSMs.
