from wtforms import Form, StringField, FloatField, IntegerField, RadioField, SelectField, TextAreaField, validators
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields.html5 import DateField, TimeField, DecimalField


class donateMoney(Form):
    donateToWho = SelectField('Donate to Who*', [validators.DataRequired()],
                              choices=[('', 'Select'), ('Under Privileged', 'Under Privileged'),
                                       ('Physically Handicapped', 'Physically Handicapped'),
                                       ('Natural Disaster Survivors', 'Natural Disaster Survivors'),
                                       ('Persons with Intellectual Disabilities', 'Persons with Intellectual Disabilities'),
                                       ('Seniors', 'Seniors'), ('Special Needs', 'Special Needs')], default='')

    # If donor inputs Monetary Donation
    # Money Information
    moneyAmount = IntegerField("Donation Amount (SGD$)*",
                               [validators.NumberRange(min=1, max=1000000), validators.DataRequired()])
    cardInfo_Name = StringField('Full Name*', [validators.Length(min=1, max=150), validators.DataRequired()])
    cardInfo_Number = StringField('Card Number*', [validators.Length(min=1, max=150), validators.DataRequired()])
    cardInfo_CVV = StringField('CVV*', [validators.Length(min=1, max=150), validators.DataRequired()])
    cardInfo_DateExpiry = StringField('Date of Expiry (mm/yy)*',
                                      [validators.Length(min=1, max=150), validators.DataRequired()])
