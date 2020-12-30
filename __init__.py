from flask import Flask, render_template, request, redirect, url_for, session
from donateForm import donationForm, donateMoney, donateItem, itemPickUp
import shelve
from Donate import DonationID, DonateBaseChoice, DonateMoney, DonateItem, CollectionItemPickUp

app = Flask(__name__)


# Home
@app.route("/")
def home():
    return render_template('index.html')


# Transaction Processing (Donations)
@app.route("/donate")
def donate():
    return render_template('Donate.html')


@app.route("/donate/details", methods=['GET', 'POST'])
def donateDetails():
    donateForm = donationForm(request.form)

    if request.method == "POST" and donateForm.validate():

        donor_basechoice = {}

        dbBCID = shelve.open("donorBaseChoicesID", "c")

        try:
            donor_basechoice = dbBCID["Donors BCID"]
        except:
            print("Error in retrieving Donors BCID from donorBaseChoicesID")

        donor = DonateBaseChoice(donateForm.donateToWho.data, donateForm.donationType.data)
        donorid = DonationID()
        getdonorid = donorid.set_donation_id()

        donor_basechoice[getdonorid] = donor

        dbBCID["Donors BCID"] = donor_basechoice

        dbBCID.close()

        donation_type = donateForm.donationType.data
        # Checks to see which choice is selected and will bring the user to the specific part of the form (money or
        # item)
        if donation_type == "M":
            return redirect(url_for('donate_Money'))
        if donation_type == "I":
            return redirect(url_for('donate_Item'))
    return render_template('donateDetails.html', form=donateForm)


@app.route("/donate/details/money", methods=['GET', 'POST'])
def donate_Money():
    donate_money = donateMoney(request.form)
    if request.method == "POST" and donate_money.validate():
        donor_moneychoices = {}

        dbMC = shelve.open("donorMoneyChoices", "c")

        try:
            donor_moneychoices = dbMC["Donors MC"]
        except:
            print("Error in retrieving Donors MC from donorMoneyChoices")

        donor = DonateMoney(donateMoney.moneyAmount.data, donateMoney.cardInfo_Name.data,
                            donateMoney.cardInfo_Number.data, donateMoney.cardInfo_CVV.data,
                            donateMoney.cardInfo_DateExpiry.data)
        donorid = DonationID()
        getdonorid = donorid.set_donation_id()

        donor_moneychoices[getdonorid] = donor

        dbMC["Donors MC"] = donor_moneychoices

    return render_template('donateMoney.html', form=donate_money)


@app.route("/donate/details/item", methods=['GET', 'POST'])
def donate_Item():
    donate_item = donateItem(request.form)
    if request.method == "POST":
        donor_itemchoices = {}

        dbIM = shelve.open("donorItemChoices", "c")

        try:
            donor_itemchoices = dbIM["Donors IM"]
        except:
            print("Error in retrieving Donors IM from donorItemChoices")

        donor = DonateItem(donateItem.itemName.data, donateItem.itemName.data, donateItem.collectionType.data,
                           donateItem.collectionDate.data, donateItem.collectionTime)
        donorid = DonationID()
        getdonorid = donorid.set_donation_id()

        if donateItem.itemWeight.data > 0:
            donor.set_item_weight(donateItem.itemWeight.data)
        if donateItem.itemLength.data > 0:
            donor.set_item_length(donateItem.itemLength.data)
        if donateItem.itemWidth.data > 0:
            donor.set_item_width(donateItem.itemWidth.data)
        if donateItem.itemHeight.data > 0:
            donor.set_item_height(donateItem.itemHeight.data)
        # Still have to upload images into shelve (watch keysha's vid)

        donor_itemchoices[getdonorid] = donor

        dbIM["Donors IM"] = donor_itemchoices

        # Checks to see if user picked pickup and will bring them to the address portion of the form to fill
        if donate_item.collectionType.data == "WP":
            return redirect(url_for('collection_pickup'))
    return render_template('donateItem.html', form=donate_item)


@app.route("/donate/details/item/pickup", methods=['GET', 'POST'])
def collection_pickup():
    collection_pick_up = itemPickUp(request.form)
    if request.method == "POST" and collection_pick_up.validate():
        donor_pickupchoices = {}

        dbPUC = shelve.open("donorPickUpChoices", "c")

        try:
            donor_pickupchoices = dbPUC["Donors PUC"]
        except:
            print("Error in retrieving Donors PUC from donorPickUpChoices")

        donor = CollectionItemPickUp(itemPickUp.pickupAddress1.data, itemPickUp.pickupAddress2.data,
                                     itemPickUp.pickupPostalCode.data)
        donorid = DonationID()
        getdonorid = donorid.set_donation_id()

        if itemPickUp.pickupAddress3.data != "":
            donor.set_address2(itemPickUp.pickupAddress3.data)

        donor_pickupchoices[getdonorid] = donor

        dbPUC["Donors PUC"] = donor_pickupchoices

    return render_template('donateItemPickup.html', form=collection_pick_up)


# Customer Support
@app.route("/forum")
def forum():
    return render_template('Forum.html')


@app.route("/faq")
def faq():
    return render_template('FAQ.html')


# Account Management
@app.route("/account")
def account():
    return render_template('Account.html')


# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
