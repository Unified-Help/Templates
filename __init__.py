from flask import Flask, render_template, request, redirect, url_for, session, g
from donateMoney import donateMoney
from donateItem import donateItem
from CreateAccountForm import CreateUserForm
from ForumForm import createForumPost
from Forum import ForumPost
import shelve, User
from Donate import DonateMoney, DonateItem

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user


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
    # Displaying Donation History
    donorsM_dict = {}

    db = shelve.open("donorChoices", "r")
    donorsM_dict = db["Donors"]
    db.close()

    donorsM_list = []
    for key in donorsM_dict:
        donorM = donorsM_dict.get(key)
        donorsM_list.append(donorM)

    return render_template('donationHistory.html', countM=len(donorsM_list), donorsM_list=donorsM_list)


@app.route("/donate/details")
def donateDetails():
    return render_template('donateDetails.html')


@app.route("/donate/details/money", methods=['GET', 'POST'])
def donate_Money():
    # Monetary Donations
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
    # Item Donations
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

        donor_itemchoices[donor.get_itemID()] = donor

        dbIM["Donors"] = donor_itemchoices

        dbIM.close()

    return render_template('donateItem.html', form=donate_item)


@app.route("/donate/details/confirmation")
def donate_Confirmation():
    return render_template('donateConfirmation.html')


@app.route("/donate/itemupdate/<string:id>", methods=['GET', 'POST'])
def donate_ItemUpdate(id):
    update_donate_item = donateItem(request.form)
    if request.method == 'POST':
        donors_dict = {}

        dbUP = shelve.open('donorChoices', 'w')
        donors_dict = dbUP['Donors']

        donor = donors_dict.get(id)

        # Item Specifications
        donor.set_item_weight(update_donate_item.itemWeight.data)
        donor.set_item_height(update_donate_item.itemHeight.data)
        donor.set_item_length(update_donate_item.itemLength.data)
        donor.set_item_width(update_donate_item.itemWidth.data)

        # Collection Details
        donor.set_date(update_donate_item.collectionDate.data)
        donor.set_month(update_donate_item.collectionMonth.data)
        donor.set_time(update_donate_item.collectionTime.data)
        donor.set_collection_type(update_donate_item.collectionType.data)

        # If Collection is pickup
        donor.set_address1(update_donate_item.pickupAddress1.data)
        donor.set_address2(update_donate_item.pickupAddress2.data)
        donor.set_address3(update_donate_item.pickupAddress3.data)
        donor.set_postal_code(update_donate_item.pickupPostalCode.data)

        dbUP['Donors'] = donors_dict
        dbUP.close()

        return redirect(url_for('donateHistory'))

    else:
        donors_dict = {}

        dbUP = shelve.open('donorChoices', 'r')
        donors_dict = dbUP["Donors"]
        dbUP.close()

        donor = donors_dict.get(id)

        # Item Specifications
        update_donate_item.itemWeight.data = donor.get_item_weight()
        update_donate_item.itemHeight.data = donor.get_item_height()
        update_donate_item.itemLength.data = donor.get_item_length()
        update_donate_item.itemWidth.data = donor.get_item_width()

        # Collection Details
        update_donate_item.collectionDate.data = donor.get_date()
        update_donate_item.collectionMonth.data = donor.get_month()
        update_donate_item.collectionTime.data = donor.get_time()
        update_donate_item.collectionType.data = donor.get_collection_type()

        # If Collection is pickup
        update_donate_item.pickupAddress1.data = donor.get_address1()
        update_donate_item.pickupAddress2.data = donor.get_address2()
        update_donate_item.pickupAddress3.data = donor.get_address3()
        update_donate_item.pickupPostalCode.data = donor.get_postal_code()

        return render_template('donateItemUpdate.html', form=update_donate_item)


# Customer Support
@app.route("/forum")
def forum():
    forum_dict = {}
    pinned_post_dict = {}
    announcements_dict = {}
    uhc_dict = {}
    db = shelve.open('forumdb', 'c')
    forum_dict = db['Posts']
    pinned_post_dict = db['PinnedPosts']
    announcements_dict = db['Announcements']
    uhc_dict = db['UHC']
    db.close()

    forum_list = []
    pinned_post_list = []
    announcements_list = []
    uhc_list = []
    for key in forum_dict:
        post = forum_dict.get(key)
        forum_list.append(post)
    for key in pinned_post_list:
        post = pinned_post_dict.get(key)
        pinned_post_list.append(post)
    for key in announcements_list:
        post = announcements_dict.get(key)
        announcements_list.append(post)
    for key in uhc_list:
        post = uhc_dict.get(key)
        uhc_list.append(post)
    return render_template('Forum.html', forum_list=forum_list, pinned_post_list=pinned_post_list, announcements_list=announcements_list, uhc_list=uhc_list)


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
        pinned_post_dict = {}
        announcements_dict = {}
        uhc_dict = {}
        db = shelve.open('forumdb', 'c')
        try:
            forum_dict = db['Posts']
            pinned_post_dict = db['PinnedPosts']
            announcements_dict = db['Announcements']
            uhc_dict = db['UHC']

        except:
            print("Error in retrieving data from forumdb.")

        post = ForumPost()
        post.set_username(create_forum_post_form.username.data)
        post.set_category(create_forum_post_form.category.data)
        post.set_post_subject(create_forum_post_form.post_subject.data)
        post.set_post_message(create_forum_post_form.post_message.data)
        if create_forum_post_form.category.data == 'Unified Help Community':
            forum_dict[post.get_forum_post_id()] = post
        elif create_forum_post_form.category.data == 'Pinned Posts':
            pinned_post_dict[post.get_forum_post_id()] = post
        # announcements_dict[post.get_forum_post_id()] = post
        # uhc_dict[post.get_forum_post_id()] = post
        db['Posts'] = forum_dict
        db['PinnedPosts'] = pinned_post_dict
        db['Announcements'] = announcements_dict
        db['UHC'] = uhc_dict
        db.close()

    return render_template('createForumPost.html', form=create_forum_post_form)


@app.route("/faq")
def faq():
    return render_template('FAQ.html')

# Account Management

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Anthony', password='password'))
users.append(User(id=2, username='Becca', password='secret'))
users.append(User(id=3, username='Carlos', password='somethingsimple'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')

@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('storage.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from storage.db.")

        user = User.User(create_user_form.first_name.data, create_user_form.last_name.data, create_user_form.gender.data, create_user_form.username.data, create_user_form.email.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        db.close()

        return redirect(url_for('home'))
    return render_template('createAccount.html', form=create_user_form)



# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
