from flask_wtf import FlaskForm
from wtforms import FileField,HiddenField
# from wtforms import *

# from wtforms.fields.html5 import DateField,DateTimeField,IntegerRangeField
# from wtforms.validators import InputRequired, Email, DataRequired, Length, NumberRange,EqualTo,Length
from flask_wtf.file import FileRequired
from werkzeug.utils import secure_filename

class UploadFile(FlaskForm):
    inputFile = FileField('inputFile', validators=[FileRequired()])