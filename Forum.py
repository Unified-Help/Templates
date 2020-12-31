from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
import shelve

class ForumPost:
    forum_post_id_counter = 0
    # category_list = ['Pinned Posts','Announcements','Unified Help Community']
    def __init__(self):
        # Forum Post IDs
        ForumPost.forum_post_id_counter += 1
        self.__forum_Post_ID = ForumPost.forum_post_id_counter

        self.__username = ''
        self.__post_subject = ''
        self.__category = ''
        self.__post_message = ''
        self.__upvotes = 0
        self.__downvotes = 0

    def set_forum_post_id(self,forum_post_id):
        self.__forum_Post_ID = forum_post_id
    def set_username(self,username):
        self.__username = username
    def set_post_subject(self,post_subject):
        self.__post_subject = post_subject
    def set_category(self,category):
        self.__category = category
    def set_post_message(self,post_message):
        self.__post_message = post_message
    def set_upvotes(self,upvotes):
        self.__upvotes = upvotes
    def set_downvotes(self,downvotes):
        self.__downvotes = downvotes

    def get_forum_post_id(self):
        return self.__forum_Post_ID
    def get_username(self):
        return self.__username
    def get_post_subject(self):
        return self.__post_subject
    def get_category(self):
        return self.__category
    def get_post_message(self):
        return self.__post_message
    def get_upvotes(self):
        return self.__upvotes
    def get_downvotes(self):
        return self.__downvotes



