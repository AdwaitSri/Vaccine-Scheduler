from django.shortcuts import render
from django.http import HttpResponse
from .models import PersonalDetails, VaccinationDetails


# Create your views here.
def index(request):
    return render(request, 'calc/sign-in-page.html')


def user_details(request):
    details_list = PersonalDetails.objects.all()
    detail = {'details':details_list}
    return render(request,'calc/user_details.html', context = detail)

def signup(request):
    return render(request,'calc/sign-up-page.html')


# from django.shortcuts import render
# from . import forms
# import mysql.connector as sqlcon
#
# from decouple import config
# # Create your views here.


# def index(request):
#     return render(request,'calc/index.html')
# # Get- From database to html
# # Post- From html to database
# passwd=config('password',default='')
# def form_name_view(request):
#     form=forms.FormName()
#
#     if request.method =='POST':
#
#         form=forms.FormName(request.POST)
#         if form.is_valid():
#             mycon = sqlcon.connect(passwd,host="localhost", user="root", database="Covid_Vaccination")
#             if mycon.is_connected():
#                 print("Successfully connected")
#                 cursor = mycon.cursor()
#
#
#                 data_in = "INSERT INTO Personal_Details (name,phone_no,age,gender,pwd) VALUES ('{}', {}, {}, '{}', '{}')".format(form.cleaned_data['name'], form.cleaned_data['phone_no'],form.cleaned_data['age'],form.cleaned_data['gender'], form.cleaned_data['pwd'])
#                 cursor.execute(data_in)
#                 mycon.commit()
#
#         # if form.is_valid():
#         #     #valid in the sense all the stuff is complete, email is fine , fields are filled etc
#         #     print('Validation complete')
#         #     print("Name:"+form.cleaned_data['name'])
#         #     print("Phno:",form.cleaned_data['phno'])
#         #     print("age:",form.cleaned_data['age'])
#         #     print("gender:"+form.cleaned_data['gender'])
#         #     print("pwed:"+form.cleaned_data['pwd'])
#     return render(request,'calc/form_page.html',{'form':form})
