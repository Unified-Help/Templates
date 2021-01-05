from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
import shelve
from ForumForm import Form
import datetime

class ForumPost:
    def __init__(self):
        self.__username = ''
        self.__post_subject = ''
        self.__category = ''
        self.__post_message = ''
        self.__post_reply = ''
        self.__upvotes = 0
        self.__downvotes = 0
        self.__datetime = datetime.datetime.now()

    def set_username(self, username):
        self.__username = username

    def set_post_subject(self, post_subject):
        self.__post_subject = post_subject

    def set_category(self, category):
        self.__category = category

    def set_post_message(self, post_message):
        self.__post_message = post_message

    def set_post_reply(self, post_reply):
        self.__post_reply = post_reply

    def set_upvotes(self, upvotes):
        self.__upvotes = upvotes

    def set_downvotes(self, downvotes):
        self.__downvotes = downvotes

    def set_date_time(self, datetime):
        self.__datetime = datetime


    def get_username(self):
        return self.__username

    def get_post_subject(self):
        return self.__post_subject

    def get_category(self):
        return self.__category

    def get_post_message(self):
        return self.__post_message

    def get_post_reply(self):
        return self.__post_reply

    def get_upvotes(self):
        return self.__upvotes

    def get_downvotes(self):
        return self.__downvotes

    def get_date_time(self):
        return self.__datetime

class ForumPinnedPostsCounter(ForumPost):
    forum_pinned_post_id_counter = 0

    def __init__(self):
        super().__init__()
        ForumPinnedPostsCounter.forum_pinned_post_id_counter += 1
        self.__forum_pinned_post_id = ForumPinnedPostsCounter.forum_pinned_post_id_counter

    def set_forum_pinned_post_id(self, forum_pinned_post_id):
        self.__forum_pinned_post_id = forum_pinned_post_id

    def get_forum_pinned_post_id(self):
        return self.__forum_pinned_post_id


class ForumAnnoucementsPostCounter(ForumPost):
    forum_announcements_id_counter = 0

    def __init__(self):
        super().__init__()
        ForumAnnoucementsPostCounter.forum_announcements_id_counter += 1
        self.__forum_announcements_post_id = ForumAnnoucementsPostCounter.forum_announcements_id_counter

    def set_forum_announcements_post_id(self, forum_announcements_post_id):
        self.__forum_announcements_post_id = forum_announcements_post_id

    def get_forum_announcements_post_id(self):
        return self.__forum_announcements_post_id


class ForumUHCPostCounter(ForumPost):
    forum_uhc_id_counter = 0

    def __init__(self):
        super().__init__()
        ForumUHCPostCounter.forum_uhc_id_counter += 1
        self.__forum_uhc_post_id = ForumUHCPostCounter.forum_uhc_id_counter

    def set_forum_uhc_post_id(self, forum_uhc_post_id):
        self.__forum_uhc_post_id = forum_uhc_post_id

    def get_forum_uhc_post_id(self):
        return self.__forum_uhc_post_id
