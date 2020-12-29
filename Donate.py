class Donate:
    donor_id = 0

    def __init__(self):
        # Donate.donor_id += 1
        self.__donor_id = Donate.donor_id
        # base donation choices
        # self.__donation_choice = ""
        self.__donate_who = ""
        self.__donate_type = ""

        # money donations
        self.__money_amount = 0
        self.__cardInfo_Name = ""
        self.__cardInfo_Number = ""
        self.__cardInfo_CVV = ""
        self.__cardInfo_DateExpiry = ""

        # item donations
        self.__item_type = ""
        self.__item_name = ""
        self.__item_weight = 0
        self.__item_length = 0
        self.__item_width = 0
        self.__item_height = 0

        # collection details
        self.__collection_type = ""
        self.__date = ""
        self.__time = ""

        # Pickup Address
        self.__address1 = ""
        self.__address2 = ""
        self.__address3 = ""
        self.__postal_code = ""
        # self.__donation_confirmation = ""

    # Accessor Methods
    # def get_donation_choice(self):
    #     return self.__donation_choice
    def get_donor_id(self):
        return self.__donor_id

    def get_donate_who(self):
        return self.__donate_who

    def get_donate_type(self):
        return self.__donate_type

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

    def get_date_day(self):
        return self.__date_day

    def get_date_month(self):
        return self.__date_month

    def get_date_year(self):
        return self.__date_year

    def get_date_time(self):
        return self.__date_time

    def get_address1(self):
        return self.__address1

    def get_address2(self):
        return self.__address2

    def get_address3(self):
        return self.__address3

    def get_postal_code(self):
        return self.__postal_code

    # def get_donation_confirmation(self):
    #     return self.__donation_confirmation

    # Mutator Methods
    # def set_donation_choice(self, donation_choice):
    #     self.__donation_choice = donation_choice

    def set_donor_id(self, donor_id):
        self.__donor_id = donor_id

    def set_donate_who(self, donate_who):
        self.__donate_who = donate_who

    def set_donate_type(self, donate_type):
        self.__donate_type = donate_type

    def set_money_amount(self, money_amount):
        self.__money_amount = money_amount

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

    def set_date_day(self, date_day):
        self.__date_day = date_day

    def set_date_month(self, date_month):
        self.__date_month = date_month

    def set_date_year(self, date_year):
        self.__date_year = date_year

    def set_date_time(self, date_time):
        self.__date_time = date_time

    def set_address1(self, address1):
        self.__address1 = address1

    def set_address2(self, address2):
        self.__address2 = address2

    def set_address3(self, address3):
        self.__address3 = address3

    def set_postal_code(self, postal_code):
        self.__postal_code = postal_code

    # def set_donation_confirmation(self, donation_confirmation):
    #     self.__donation_confirmation = donation_confirmation
