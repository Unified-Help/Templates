class DonationID:
    donation_id_counter = 0

    def __init__(self):
        self.__donation_id = 0
        # DonationID.donation_id += 1
        # self.__donation_id = DonationID.donation_id

    # Accessor
    def get_donation_id(self):
        return self.__donation_id

    # Mutator
    def set_donation_id(self):
        donation_id = DonationID.donation_id_counter
        donation_id += 1
        self.__donation_id = donation_id
        return self.__donation_id

# Test Codes for DonationID()
# if __name__ == "__main__":
#     donorid = DonationID()
#     makedonorid = donorid.set_donation_id()
#     print(makedonorid)


# Donor's Base Choices
class DonateBaseChoice:
    def __init__(self, donate_who, donate_type):
        self.__donate_who = donate_who
        self.__donate_type = donate_type

    # Accessor Methods
    def get_donate_who(self):
        return self.__donate_who

    def get_donate_type(self):
        return self.__donate_type

    # Mutator Methods
    def set_donate_who(self, donate_who):
        self.__donate_who = donate_who

    def set_donate_type(self, donate_type):
        self.__donate_type = donate_type


# Monetary Donations
class DonateMoney:
    def __init__(self, money_amount, cardInfo_Name, cardInfo_Number, cardInfo_CVV, cardInfo_DateExpiry):
        # money donations
        self.__money_amount = money_amount
        self.__cardInfo_Name = cardInfo_Name
        self.__cardInfo_Number = cardInfo_Number
        self.__cardInfo_CVV = cardInfo_CVV
        self.__cardInfo_DateExpiry = cardInfo_DateExpiry

    # Accessors
    def get_money_amount(self):
        return self.__money_amount

    def get_cardInfo_Name(self):
        return self.__cardInfo_Name

    def get_cardInfo_Number(self):
        return self.__cardInfo_Number

    def get_cardInfo_CVV(self):
        return self.__cardInfo_CVV

    def get_cardInfo_DateExpiry(self):
        return self.__cardInfo_DateExpiry

    # Mutators
    def set_money_amount(self, money_amount):
        self.__money_amount = money_amount

    def set_cardInfo_Name(self, cardInfo_Name):
        self.__cardInfo_Name = cardInfo_Name

    def set_cardInfo_Number(self, cardInfo_Number):
        self.__cardInfo_Number = cardInfo_Number

    def set_cardInfo_CVV(self, cardInfo_CVV):
        self.__cardInfo_CVV = cardInfo_CVV

    def set_cardInfo_DateExpiry(self, cardInfo_DateExpiry):
        self.__cardInfo_DateExpiry = cardInfo_DateExpiry


# Item Donations
class DonateItem:
    def __init__(self, item_type, item_name, collection_type, date, time):
        self.__item_type = item_type
        self.__item_name = item_name
        self.__item_weight = 0
        self.__item_length = 0
        self.__item_width = 0
        self.__item_height = 0

        # Collection Details
        self.__collection_type = collection_type
        self.__date = date
        self.__time = time

    # Accessors
    def get_item_type(self):
        return self.__item_type

    def get_item_name(self):
        return self.__item_name

    def get_item_weight(self):
        return self.__item_weight

    def get_item_length(self):
        return self.__item_length

    def get_item_width(self):
        return self.__item_width

    def get_item_height(self):
        return self.__item_height

    def get_collection_type(self):
        return self.__collection_type

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    # Mutators
    def set_item_type(self, item_type):
        self.__item_type = item_type

    def set_item_name(self, item_name):
        self.__item_name = item_name

    def set_item_weight(self, item_weight):
        self.__item_weight = item_weight

    def set_item_length(self, item_length):
        self.__item_length = item_length

    def set_item_width(self, item_width):
        self.__item_width = item_width

    def set_item_height(self, item_height):
        self.__item_height = item_height

    def set_collection_type(self, collection_type):
        self.__collection_type = collection_type

    def set_date(self, date):
        self.__date = date

    def set_time(self, time):
        self.__time = time


# Item Pick Up
class CollectionItemPickUp:
    def __init__(self, address1, address2, postal_code):
        self.__address1 = address1
        self.__address2 = address2
        self.__address3 = ""
        self.__postal_code = postal_code

    # Accessors
    def get_address1(self):
        return self.__address1

    def get_address2(self):
        return self.__address2

    def get_address3(self):
        return self.__address3

    def get_postal_code(self):
        return self.__postal_code

    # Mutators
    def set_address1(self, address1):
        self.__address1 = address1

    def set_address2(self, address2):
        self.__address2 = address2

    def set_address3(self, address3):
        self.__address3 = address3

    def set_postal_code(self, postal_code):
        self.__postal_code = postal_code
