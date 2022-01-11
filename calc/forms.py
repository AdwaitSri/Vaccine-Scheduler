from django import forms
from django.core import validators
import mysql.connector as sqlcon
#creating ur own validator

def check_for_z(value):
    if value[0].lower() !='z':
        raise forms.ValidationError("Needs to start with Z")
class FormName(forms.Form):
    # name=forms.CharField(validators=[check_for_z])
    name=forms.CharField()
    phone_no=forms.IntegerField()
    age=forms.IntegerField()
    gender=forms.CharField(max_length=1)
    pwd=forms.CharField()
    # print(name,phno,age,gender,pwd)
    # mycon = sqlcon.connect(host="localhost", user="root", passwd="", database="Covid_Vaccination")
    # if mycon.is_connected():
    #     print("Successfully connected")
    # cursor = mycon.cursor()
    #
    #
    # data_in = "INSERT INTO Personal_Details (name,phno,age,gender,pwd) VALUES ('{}', {}, {}, '{}', '{}')".format(name, phno, age, gender, pwd)
    # cursor.execute(data_in)
    # mycon.commit()
