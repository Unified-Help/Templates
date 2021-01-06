from wtforms import Form, StringField, FloatField, IntegerField, RadioField, SelectField, TextAreaField, validators
from wtforms.widgets import TextArea

class createForumPost(Form):
    username = StringField('Username', [validators.Length(min=1, max=150), validators.DataRequired()])
    post_subject = StringField('Post Subject:', [validators.Length(min=1, max=150), validators.DataRequired()], render_kw={"placeholder": "Give your topic a title."})
    category = SelectField('Category', [validators.DataRequired()], choices=[('', 'Select'), ('Pinned Posts', 'Pinned Posts'), ('Announcements', 'Announcements'), ('Unified Help Community', 'Unified Help Community')], default='')
    post_message = StringField('Post Message', [validators.Length(min=1, max=10000), validators.DataRequired()], id='contentcode', render_kw={"placeholder": "Write your comment here."})
