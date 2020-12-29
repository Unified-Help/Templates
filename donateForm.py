from wtforms import Form, StringField, FloatField, IntegerField, RadioField, SelectField, TextAreaField, \
    validators, DateField, DateTimeField
from flask_wtf.file import FileField, FileRequired, FileAllowed


class donationForm(Form):
    donateToWho = SelectField('Donate to Who', [validators.DataRequired()],
                              choices=[('', 'Select'), ('UP', 'Under Privileged'), ('PH', 'Physically Handicapped'),
                                       ('NDS', 'Natural Disaster Survivors'), ('SN', 'Special Needs')], default='')
    donationType = RadioField('Type of Donation', choices=[('M', 'Monetary Donation'), ('I', 'Item Donation')],
                              default='M')


class donateMoney(donationForm):
    # If donor inputs Monetary Donation
    # Money Information
    moneyAmount = IntegerField("Donation Amount", [validators.Length(min=1, max=150), validators.DataRequired()])
    cardInfo_Name = StringField('Full Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    cardInfo_Number = StringField('Card Number', [validators.Length(min=1, max=150), validators.DataRequired()])
    cardInfo_CVV = StringField('CVV', [validators.Length(min=1, max=150), validators.DataRequired()])
    cardInfo_DateExpiry = StringField('Date of Expiry (dd/mm/yyyy)',
                                      [validators.Length(min=1, max=150), validators.DataRequired()])


class donateItem(donationForm):
    # If donor inputs Item Donation
    # Item Information
    itemType = SelectField('Item Type', [validators.DataRequired()],
                           choices=[('C', 'Clothes'), ('F', 'Furniture'),
                                    ('E', 'Electronics'), ('B', 'Books')], default='C')
    itemName = StringField("Name of Item (T-Shirt, Laptop etc.)",
                           [validators.Length(min=1, max=150), validators.DataRequired()])
    itemWeight = FloatField("Weight of Item (kg)", [validators.Length(min=1, max=150), validators.DataRequired()])
    itemHeight = FloatField("Height of Item (m)", [validators.Length(min=1, max=150), validators.Optional()])
    itemLength = FloatField("Length of Item (m)", [validators.Length(min=1, max=150), validators.Optional()])
    itemWidth = FloatField("Width of Item (m)", [validators.Length(min=1, max=150), validators.Optional()])
    itemImage = FileField('Picture of Item', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])

    # Collection Types and Information
    collectionDate = DateField('Pick a Date (dd/mm/yy)', format='%d-%m-%y')
    collectionTime = DateTimeField("Pick a Time (24hr format, e.g. 0000)", format='%H:%M')
    collectionType = RadioField('Type of Collection', choices=[('D', 'Drop Off'), ('WP', 'We Pick Up')],
                                default='D')


class itemPickUp(donateItem):
    # If donor picks PickUp as collection type, they are required to input their address.
    pickupAddress1 = StringField("Address Line 1", [validators.Length(min=1, max=150), validators.DataRequired()])
    pickupAddress2 = StringField("Address Line 2", [validators.Length(min=1, max=150), validators.DataRequired()])
    pickupAddress3 = StringField("Address Line 3", [validators.Length(min=1, max=150), validators.Optional()])
    pickupPostal = StringField("Postal Code", [validators.Length(min=1, max=6), validators.DataRequired()])


def donationMoney():
    pass
