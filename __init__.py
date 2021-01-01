from flask import Flask, render_template, request, redirect, url_for, session
from donateMoney import donateMoney
from donateItem import donateItem
from CreateAccountForm import CreateAccountForm
from ForumForm import createForumPost
from Forum import ForumPost
import shelve, User
from Donate import DonateMoney, DonateItem

app = Flask(__name__)


# Home
@app.route("/")
def home():
    return render_template('index.html')


# Transaction Processing (Donations)
@app.route("/donate")
def donate():
    return render_template('Donate.html')


@app.route("/donate/history")
def donateHistory():
    # For Monetary Donations
    donorsM_dict = {}
    # donorsI_dict = {}

    db = shelve.open("donorChoices", "r")
    donorsM_dict = db["Donors"]
    # donorsI_dict = db["Donors"]
    db.close()

    donorsM_list = []
    # donorsI_list = []
    for key in donorsM_dict:
        donorM = donorsM_dict.get(key)
        donorsM_list.append(donorM)
        # donorI = donorsI_dict.get(key)
        # donorsI_list.append(donorI)

    # For Item Donations
    # donorsI_dict = {}
    #
    # dbIM = shelve.open("donorItemChoices", "r")
    # donorsI_dict = dbIM["Donors IM"]
    # dbIM.close()
    #
    # donorsI_list = []
    # for key in donorsI_dict:
    #     donorI = donorsI_dict.get(key)
    #     donorsI_list = donorI

    return render_template('donationHistory.html', countM=len(donorsM_list), donorsM_list=donorsM_list
                           )
    # , countI=len(donorsI_list), donorsI_list=donorsI_list


@app.route("/donate/details")
def donateDetails():
    # donateForm = donationForm(request.form)
    #
    # if request.method == "POST" and donateForm.validate():
    #
    #     donor_basechoice = {}
    #
    #     dbBCID = shelve.open("donorBaseChoicesID", "c")
    #
    #     try:
    #         donor_basechoice = dbBCID["Donors BCID"]
    #     except:
    #         print("Error in retrieving Donors BCID from donorBaseChoicesID")
    #
    #     donor = DonateBaseChoice(donateForm.donateToWho.data, donateForm.donationType.data)
    #     donorid = DonationID()
    #     getdonorid = donorid.set_donation_id()
    #
    #     donor_basechoice[getdonorid] = donor
    #
    #     dbBCID["Donors BCID"] = donor_basechoice
    #
    #     dbBCID.close()
    #
    #     donation_type = donateForm.donationType.data
    #     # Checks to see which choice is selected and will bring the user to the specific part of the form (money or
    #     # item)
    #     if donation_type == "Monetary Donation":
    #         return redirect(url_for('donate_Money'))
    #     if donation_type == "Item Donation":
    #         return redirect(url_for('donate_Item'))
    return render_template('donateDetails.html')


@app.route("/donate/details/money", methods=['GET', 'POST'])
def donate_Money():
    donate_money = donateMoney(request.form)
    if request.method == "POST" and donate_money.validate():
        donor_moneychoices = {}

        dbMC = shelve.open("donorChoices", "c")

        try:
            donor_moneychoices = dbMC["Donors"]
        except:
            print("Error in retrieving Donors MC from donorMoneyChoices")

        donor = DonateMoney(donate_money.donateToWho.data, donate_money.moneyAmount.data,
                            donate_money.cardInfo_Name.data,
                            donate_money.cardInfo_Number.data, donate_money.cardInfo_CVV.data,
                            donate_money.cardInfo_DateExpiry.data, donate_money.cardInfo_YearExpiry.data)

        donor_moneychoices[donor.get_moneyID()] = donor

        dbMC["Donors"] = donor_moneychoices

        dbMC.close()

    return render_template('donateMoney.html', form=donate_money)


@app.route("/donate/details/item", methods=['GET', 'POST'])
def donate_Item():
    donate_item = donateItem(request.form)
    if request.method == "POST":
        donor_itemchoices = {}

        dbIM = shelve.open("donorChoices", "c")

        try:
            donor_itemchoices = dbIM["Donors"]
        except:
            print("Error in retrieving Donors IM from donorItemChoices")

        donor = DonateItem(donate_item.donateToWho.data, donate_item.itemName.data, donate_item.itemName.data,
                           donate_item.itemWeight.data, donate_item.itemHeight.data, donate_item.itemLength.data,
                           donate_item.itemWidth.data, donate_item.collectionType.data, donate_item.collectionDate.data,
                           donate_item.collectionMonth.data, donate_item.collectionTime.data,
                           donate_item.pickupAddress1.data, donate_item.pickupAddress2.data,
                           donate_item.pickupAddress3.data, donate_item.pickupPostalCode.data)

        # Still have to upload images into shelve (watch keysha's vid)

        donor_itemchoices[donor.get_itemID()] = donor

        dbIM["Donors"] = donor_itemchoices

        dbIM.close()

        # # Checks to see if user picked pickup and will bring them to the address portion of the form to fill
        # if donate_item.collectionType.data == "We Pick Up":
        #     return redirect(url_for('collection_pickup'))
    return render_template('donateItem.html', form=donate_item)


# @app.route("/donate/details/item/pickup", methods=['GET', 'POST'])
# def collection_pickup():
#     collection_pick_up = itemPickUp(request.form)
#     if request.method == "POST" and collection_pick_up.validate():
#         donor_pickupchoices = {}
#
#         dbPUC = shelve.open("donorPickUpChoices", "c")
#
#         try:
#             donor_pickupchoices = dbPUC["Donors PUC"]
#         except:
#             print("Error in retrieving Donors PUC from donorPickUpChoices")
#
#         donor = CollectionItemPickUp(collection_pick_up.pickupAddress1.data, collection_pick_up.pickupAddress2.data,
#                                      collection_pick_up.pickupAddress3, collection_pick_up.pickupPostalCode.data)
#         donorid = DonationID()
#         getdonorid = donorid.set_donation_id()
#
#         # if len(collection_pick_up.pickupAddress3.data) != 0:
#         #     donor.set_address2(collection_pick_up.pickupAddress3.data)
#
#         donor_pickupchoices[getdonorid] = donor
#
#         dbPUC["Donors PUC"] = donor_pickupchoices
#
#         dbPUC.close()
#
#     return render_template('donateItemPickup.html', form=collection_pick_up)


# Customer Support
@app.route("/forum")
def forum():
    forum_dict = {}
    db = shelve.open('forumdb', 'c')
    forum_dict = db['Posts']
    db.close()

    forum_list = []
    for key in forum_dict:
        post = forum_dict.get(key)
        forum_list.append(post)
    return render_template('Forum.html', forum_list=forum_list)


# @app.route("/retrieveforumpost")
# def retrieveforumpost():
#     forum_dict = {}
#     db = shelve.open('forumdb', 'c')
#     forum_dict = db['Posts']
#     db.close()
#
#     forum_list = []
#     for key in forum_dict:
#         post = forum_dict.get(key)
#         forum_list.append(post)
#
#     return render_template('retrieveforumpost.html',forum_list=forum_list)

@app.route("/forum/createforumpost", methods=['GET', 'POST'])
def create_forum_post():
    create_forum_post_form = createForumPost(request.form)
    if request.method == 'POST' and create_forum_post_form.validate():
        forum_dict = {}
        db = shelve.open('forumdb', 'c')

        try:
            forum_dict = db['ForumPostID']
        except:
            print("Error in retrieving Post from forumdb.")

        post = ForumPost()
        post.set_username(create_forum_post_form.username.data)
        post.set_category(create_forum_post_form.category.data)
        post.set_post_subject(create_forum_post_form.post_subject.data)
        post.set_post_message(create_forum_post_form.post_message.data)
        forum_dict[post.get_forum_post_id()] = post

        db['Posts'] = forum_dict
        db.close()

    return render_template('createForumPost.html', form=create_forum_post_form)


@app.route("/faq")
def faq():
    return render_template('FAQ.html')


# Account Management
@app.route("/account")
def account():
    return render_template('Account.html')


@app.route('/CreateAccount', methods=['GET', 'POST'])
def create_account():
    create_account_form = CreateAccountForm(request.form)
    if request.method == 'POST' and create_account_form.validate():
        users_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from storage.db.")

        user = User.User(create_account_form.first_name.data, create_account_form.last_name.data,
                         create_account_form.gender.data, create_account_form.membership.data,
                         create_account_form.remarks.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        db.close()

        session['user_created'] = user.get_first_name() + ' ' + user.get_last_name()

    return render_template('CreateAccount.html', form=create_account_form)


# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
