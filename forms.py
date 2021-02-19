from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):

    username = StringField("Username", validators = [DataRequired()],render_kw={"placeholder": "Username"})
    room = StringField("Chat Room ID", validators = [DataRequired()],render_kw={"placeholder": "Chat Room ID"})
    submit = SubmitField("Chat")
