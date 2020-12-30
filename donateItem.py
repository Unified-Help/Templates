from wtforms import Form, StringField, FloatField, IntegerField, RadioField, SelectField, TextAreaField, validators
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields.html5 import DateField, TimeField, DecimalField


class donateItem(Form):
    donateToWho = SelectField('Donate to Who*', [validators.DataRequired()],
                              choices=[('', 'Select'), ('Under Privileged', 'Under Privileged'),
                                       ('Physically Handicapped', 'Physically Handicapped'),
                                       ('Natural Disaster Survivors', 'Natural Disaster Survivors'),
                                       ('Special Needs', 'Special Needs')], default='')

    # If donor inputs Item Donation
    # Item Information
    itemType = SelectField('Item Type*', [validators.DataRequired()],
                           choices=[('Clothes', 'Clothes'), ('Furniture', 'Furniture'), ('Electronics', 'Electronics'),
                                    ('Books', 'Books')], default='C')
    itemName = StringField("Name of Item (T-Shirt, Laptop etc.)*",
                           [validators.Length(min=1, max=150), validators.DataRequired()])
    itemWeight = FloatField("Weight of Item (kg)*", [validators.NumberRange(min=1, max=150), validators.DataRequired()])
    itemHeight = FloatField("Height of Item (m)*", [validators.NumberRange(min=1, max=150), validators.Optional()])
    itemLength = FloatField("Length of Item (m)*", [validators.NumberRange(min=1, max=150), validators.Optional()])
    itemWidth = FloatField("Width of Item (m)*", [validators.NumberRange(min=1, max=150), validators.Optional()])
    itemImage = FileField('Picture of Item', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])

    # Collection Types and Information
    collectionDate = DateField('Pick a Date (dd/mm/yyyy)*', format='%Y-%m-%d')
    collectionTime = TimeField("Pick a Time (24hr format, e.g. 0000)*", format='%H:%M')
    collectionType = RadioField('Type of Collection*', choices=[('Drop Off', 'Drop Off'), ('We Pick Up', 'We Pick Up')],
                                default='Drop Off')

    # Pick Up Collection information
    pickupAddress1 = StringField("Address Line 1", [validators.Length(min=1, max=150), validators.Optional()])
    pickupAddress2 = StringField("Address Line 2", [validators.Length(min=1, max=150), validators.Optional()])
    pickupAddress3 = StringField("Address Line 3", [validators.Length(min=1, max=150), validators.Optional()])
    pickupPostalCode = StringField("Postal Code", [validators.Length(min=1, max=6), validators.Optional()])
