# crimtools_22 <br />
This is a an open source repo for lawyers, and the purpose is to help
attorneys visually explain and model criminal justice issues such as
calculating jail credit, sentencing, and whether a Defendant is elligible
for special statuses such as habitual felon.<br />

__CONTENTS:__ <br />
--Defendant: a model for a Defendant accused of a crime<br />
--Crime: a model of a crime the State charges against a Defendant<br />
--Charge: a model of a criminal charge (count) against D (has crime)<br />
--ConvictionDate: a date with 1+ charges that have been convicted<br />
--Charge_Collection: Collection for charges/convictiondates<br />
--Dumbwaiter: context object for FSMs

__TESTING:__ <br />
I am using pytest and pytest-cov in testing this library, especially the
following command:<br />
pytest --cov=src --cov-report term-missing<br />