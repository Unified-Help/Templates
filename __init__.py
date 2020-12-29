from flask import Flask, render_template, request, redirect, url_for, session
from donateForm import donationForm, donateMoney, donateItem, itemPickUp
import shelve, Donate

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

        donor_choice = {}

        db = shelve.open("donorStorage", "c")

        try:
            donor_choice = db["Donors"]
        except:
            print("Error in retrieving Donors from donorStorage.db")

        donor = Donate.Donate(donateForm.donateToWho.data, donateForm.donationType.data)

        donor_choice[donor.get_donor_id()] = donor

        db["Donors"] = donor_choice

        db.close()

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
        pass
    return render_template('donateMoney.html', form=donate_money)


@app.route("/donate/details/item", methods=['GET', 'POST'])
def donate_Item():
    donate_item = donateItem(request.form)
    if request.method == "POST":
        # Checks to see if user picked pickup and will bring them to the address portion of the form to fill
        if donate_item.collectionType.data == "WP":
            return redirect(url_for('collection_pickup'))
    return render_template('donateItem.html', form=donate_item)


@app.route("/donate/details/item/pickup", methods=['GET', 'POST'])
def collection_pickup():
    collection_pick_up = itemPickUp(request.form)
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
