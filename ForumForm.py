from wtforms import Form, StringField, FloatField, IntegerField, RadioField, SelectField, TextAreaField, validators

class createForumPost(Form):
    username = StringField('Username', [validators.Length(min=1, max=150), validators.DataRequired()])
    post_subject = StringField('Post Subject', [validators.Length(min=1, max=150), validators.DataRequired()])
    category = SelectField('Category', [validators.DataRequired()], choices=[('', 'Select'), ('Unified Help Community', 'Unified Help Community')], default='')
    post_message = StringField('Post Message', [validators.Length(min=1, max=10000), validators.DataRequired()])
