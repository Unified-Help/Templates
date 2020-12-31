from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators

class ForumPost:
    def __init__(self,username,post_subject,category,post_message,upvotes,downvotes):
        self.__username = username
        self.__post_subject = ''
        self.__category = category
        self.__post_message = ''
        self.__upvotes = 0
        self.__downvotes = 0

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
